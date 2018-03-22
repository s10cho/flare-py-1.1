from flare_module.test.command.gatling import GatlingServer
from flare_module.test.command.eer import EERServer
from config import FlareEnv

class TestService():

    # Test Docker Resource Limit
    # [core, memory(G)]
    RESOURCE = FlareEnv.TEST['RESOURCE']

    TEST_SERVICE = ['ready', 'talk', 'scenario', 'chatbot']

    def __init__(self):
        self.gatling = GatlingServer()
        self.eer = EERServer()
        pass

    def run(self, param):
        print(param)
        if len(param) == 0:
            self.all_run()
        else:
            # command run
            command = param[0]
            print(command)
            if command == self.TEST_SERVICE[0]:
                self.gatling.init_data()
            else:
                self.loop_resource_test(command)

    def all_run(self):
        for command in self.TEST_SERVICE:
            if command == self.TEST_SERVICE[0]:
                self.gatling.init_data()
            else:
                self.loop_resource_test(command)

    def loop_resource_test(self, command):
        for resource in self.RESOURCE:
            cpu = resource['CPU']
            for memory in resource['MEMORY']:
                # docker restart
                self.eer.docker_restart(cpu, memory)
                # start test
                resourceId = '{0}C{1}G'.format(cpu, memory)
                self.execute_test(command, resourceId)

    def execute_test(self, command, resourceId):
        if command == self.TEST_SERVICE[1]:
            self.gatling.talk_test(resourceId)
        elif command == self.TEST_SERVICE[2]:
            self.gatling.scenario_talk_test(resourceId)
        elif command == self.TEST_SERVICE[3]:
            self.gatling.chatbot_talk_test(resourceId)
