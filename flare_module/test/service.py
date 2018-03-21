from flare_module.test.command.gatling import GatlingServer
from flare_module.test.command.eer import EERServer
from config import FlareEnv

class TestService():

    # Test Docker Resource Limit
    # [core, memory(G)]
    RESOURCE = FlareEnv.TEST['RESOURCE']

    def __init__(self):
        self.gatling = GatlingServer()
        self.eer = EERServer()
        pass

    def run(self, param):
        print(param)
        if len(param) == 0:
            self.gatling.talk_test()
            pass
        else:
            # command run
            command = param[0]
            print(command)
            if command == 'ready':
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
        if command == 'talk':
            self.gatling.talk_test(resourceId)
        elif command == 'scenario':
            self.gatling.scenario_talk_test(resourceId)
        elif command == 'chatbot':
            self.gatling.chatbot_talk_test(resourceId)
