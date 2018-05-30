import uuid
from flare_module.test.command.flare import FlareServer
from flare_module.test.command.gatling import GatlingServer
from flare_module.test.command.eer import EERServer
from config import FlareTest, FlareProcess

class TestService():

    def __init__(self):
        self.flare = FlareServer()
        self.gatling = GatlingServer()
        self.eer = EERServer()
        self.gatling.svn_update()

    def run(self, param):
        if FlareProcess.TEST == 'Y':
            print(param)
            if len(param) == 0:
                testModuleList = [key for key in FlareTest.TEST_MODULE.keys() if FlareTest.TEST_MODULE[key] == 'Y']
                for test_info in testModuleList:
                    self.run_command(test_info)
            else:
                command = param[0].upper()
                self.run_command(command)


    def run_command(self, command):
        if command == 'SETUP':
            self.execute_test(FlareTest.SETUP)
        elif command == 'UNIT':
            self.execute_test(FlareTest.UNIT_TEST)
        elif command == 'SPRINT':
            self.execute_test(FlareTest.SPRINT_TEST)
        elif command == 'PRODUCT':
            self.execute_test(FlareTest.PRODUCT_TEST)


    def execute_test(self, test_info):
        cpu_list = test_info["RESOURCE"]["CPU"]
        memory_list = test_info["RESOURCE"]["MEMORY"]
        test_list = test_info["TEST_LIST"]

        for cpu in cpu_list:
            for memory in memory_list:
                self.eer.docker_restart(cpu, memory)                    # docker restart
                resource_id = '{0}C{1}G'.format(cpu, memory)            # resource Id
                for test in test_list:
                    simulationClass = test["SIMULATION_CLASS"]
                    test_jvm = test["JVM"]
                    load_ids = self.make_load_ids(test_jvm)
                    for load in load_ids:
                        jvm = self.get_jvm(load, test_jvm)
                        outputBaseName = simulationClass[simulationClass.rfind('.') + 1:] + '_' + resource_id + '-' + load

                        self.eer.docker_monitoring_run(outputBaseName)                                      # docker monitoring start
                        self.gatling.test_run(simulationClass, outputBaseName, jvm)                         # test start
                        self.eer.docker_monitoring_stop()                                                   # docker monitoring stop
                        result_path = self.gatling.result_download()                                        # download result
                        log_file_name = self.eer.monitoring_data_download(outputBaseName, result_path)      # docker monitoring data
                        self.flare.convert_docker_monitoring_data(log_file_name, result_path)


    def make_load_ids(self, test_jvm):
        load_ids = ['WARM']
        check_key_list = [
            'agent.count',
            'customer.count',
            'customer.separate.time',
            'customer.once.count',
            'talk.customer.count',
            'scenario.customer.count'
        ]

        load_id = ''
        for option in test_jvm:
            ops = option.split('=')
            key = ops[0]
            value = ops[1]

            if key in check_key_list:
                add_key = "".join([k[0] for k in key.split('.')])
                load_id = load_id.replace('WARM', '') + add_key + value

        if len(load_id) > 0:
            load_ids.append(load_id)

        return load_ids


    def get_jvm(self, load, test_jvm):
        if load == 'WARM':
            jvm = ''
        else:
            jvm = ' '.join(['-D' + jvm for jvm in test_jvm])

        return jvm