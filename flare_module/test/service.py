from flare_module.test.command.gatling import GatlingServer
from flare_module.test.command.eer import EERServer

class TestService():

    # Test Docker Resource Limit
    # [core, memory(G)]
    CPU_RESOURCE = [
        2, 4, 8
    ]

    MEMORY_RESOURCE = [
        4, 8, 16
    ]

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
            elif command == 'talk':
                self.loop_resource_test(self.gatling.talk_test)
            elif command == 'scenario':
                self.gatling.scenario_talk_test()
            elif command == 'chatbot':
                self.gatling.chatbot_talk_test()

    def loop_resource_test(self, method):
        for cpu in self.CPU_RESOURCE:
            for memory in self.MEMORY_RESOURCE:

                # docker restart
                self.eer.docker_restart(cpu, memory)

                # start test
                method()

