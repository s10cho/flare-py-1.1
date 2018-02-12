from flare_module.test.command.test import Test
from config import FlarePath
import decorator

class TestService():

    @decorator.chown_path(FlarePath.ORACLE_HOME)
    def __init__(self):
        self.test = Test()
        pass

    def run(self, param):
        if len(param) == 0:
            self.test.talk_test()
            pass
        else:
            # command run
            command = param[0]
            print(command)
            if command == 'init':
                self.test.init_data()
            elif command == 'talk':
                self.test.talk_test()
            elif command == 'scenario':
                self.test.scenario_talk_test()
            elif command == 'chatbot':
                self.test.chatbot_talk_test()


