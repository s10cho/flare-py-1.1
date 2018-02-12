from flare_module.test.command.init import Init
from config import FlarePath
import decorator

class TestService():

    @decorator.chown_path(FlarePath.ORACLE_HOME)
    def __init__(self):
        self.init = Init()
        pass

    def run(self, param):
        if len(param) == 0:
            self.init.init_data()
            pass
        else:
            # command run
            command = param[0]
            print(command)



