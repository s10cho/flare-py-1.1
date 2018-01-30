from flare_module.build.command.svn import Svn
from flare_module.build.command.maven import Maven
from config import FlarePath
import decorator

class BuildService():

    @decorator.chown_path(FlarePath.ORACLE_HOME)
    def __init__(self):
        self.svn = Svn()
        self.maven = Maven()

    def run(self, param):
        if len(param) == 0:
            self.svn.checkout()
            self.maven.clean_install()
        else:
            # command run
            command = param[0]
            print(command)



