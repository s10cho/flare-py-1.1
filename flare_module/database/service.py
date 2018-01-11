from flare_module.database.command.setup import Setup
from flare_module.database.command.ant import Ant
from flare_module.database.command.maven import Maven

class DatabaseService():
    def __init__(self):
        self.setup = Setup()
        self.maven = Maven()
        self.ant = Ant()

    def run(self):
        self.setup.modyfySetup()
        self.setup.setSolr()
        self.maven.database_clean()
        self.ant.build()