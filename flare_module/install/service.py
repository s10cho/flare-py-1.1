from flare_module.install.command.setup import Setup
from flare_module.install.command.maven import Maven
from flare_module.install.command.docker import Docker
from flare_module.install.command.logback import Logback
from flare_module.install.command.shell import Shell
from config import FlarePath
import decorator

class InstallService():

    def __init__(self):
        self.setup = Setup()
        self.maven = Maven()
        self.docker = Docker()
        self.logback = Logback()
        self.shell = Shell()

    def run(self, param):
        if len(param) == 0:
            self.docker.rm()
            self.setup.settings()
            self.logback.change_log_level()
            self.shell.create()
            self.maven.database_clean()
            self.docker.run()
            self.docker.eer_ant()
            self.docker.eer_run()
        else:
            # command run
            command = param[0]
            print(command)
            self.docker.rm()
            self.docker.run()
            self.docker.eer_run()
