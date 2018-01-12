from flare_module.install.command.setup import Setup
from flare_module.install.command.ant import Ant
from flare_module.install.command.maven import Maven

class InstallService():
    def __init__(self):
        self.setup = Setup()
        self.maven = Maven()
        self.ant = Ant()

    def run(self):
        self.setup.setProperties()
        self.setup.setSolr()
        self.maven.database_clean()
        self.ant.build()