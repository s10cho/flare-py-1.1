from flare_module.database.command.setup import Setup
from flare_module.database.command.ant import Ant

class DatabaseService():
    def __init__(self):
        self.setup = Setup()
        self.ant = Ant()

    def run(self):
        self.setup.setupInfoSet()
        self.setup.setSolr()
        self.ant.build()