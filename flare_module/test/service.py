from flare_module.test.command.gatling import GatlingServer

class TestService():

    def __init__(self):
        self.gatling = GatlingServer()
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
                self.gatling.talk_test()
            elif command == 'scenario':
                self.gatling.scenario_talk_test()
            elif command == 'chatbot':
                self.gatling.chatbot_talk_test()


