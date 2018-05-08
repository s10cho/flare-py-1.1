from flare_module.test.command.gatling import GatlingServer
from flare_module.test.command.eer import EERServer
from config import FlareTest, FlareProcess

class TestService():

    def __init__(self):
        self.gatling = GatlingServer()
        self.eer = EERServer()

    def run(self, param):
        if FlareProcess.TEST == 'Y':
            print(param)
            if len(param) == 0:
                for test_info in ['SETUP', 'INTEGRATION']:
                    self.run_command(test_info)
            else:
                command = param[0].upper()
                self.run_command(command)


    def run_command(self, command):
        if command == 'SETUP':
            self.execute_test(FlareTest.SETUP)
        elif command == 'UNIT':
            self.execute_test(FlareTest.UNIT_TEST)
        elif command == 'INTEGRATION':
            self.execute_test(FlareTest.SPRINT_TEST)


    def execute_test(self, test_info):
        cpu_list = test_info["RESOURCE"]["CPU"]
        memory_list = test_info["RESOURCE"]["MEMORY"]
        test_list = test_info["TEST_LIST"]

        for cpu in cpu_list:
            for memory in memory_list:
                self.eer.docker_restart(cpu, memory)                    # docker restart
                resource_id = '{0}C{1}G'.format(cpu, memory)            # resource Id
                for test in test_list:
                    load_id = self.make_load_id(test["JVM"])
                    self.gatling.test_run(test, resource_id, load_id)   # test start
                    self.gatling.result_download()                      # download result


    def make_load_id(self, jvm):
        load_id = 'WARM'
        check_key_list = [
            'agent.count',
            'customer.count',
            'customer.separate.time',
            'customer.once.count'
        ]

        for option in jvm:
            ops = option.split('=')
            key = ops[0]
            value = ops[1]

            if key in check_key_list:
                add_key = "".join([k[0] for k in key.split('.')])
                load_id = load_id.replace('WARM', '') + add_key + value

        return load_id

