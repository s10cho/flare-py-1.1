from flare_module.install.command.setup import Setup
from flare_module.install.command.ant import Ant
from flare_module.install.command.maven import Maven
from flare_module.install.command.docker import Docker
from flare_module.install.command.logback import Logback

class InstallService():
    def __init__(self):
        self.setup = Setup()
        self.maven = Maven()
        self.ant = Ant()
        self.docker = Docker()
        self.logback = Logback()

    def run(self, param):
        if len(param) == 0:
            self.docker.rm()
            self.setup.settings()
            self.logback.changeLevel()
            self.maven.database_clean()
            #self.ant.build()
            self.docker.run()
        else:
            # command run
            command = param[0]
            print(command)
            self.docker.rm()
            self.docker.run()
