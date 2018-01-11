from flare_module.database.command.setup import Setup

class DatabaseService():
    def __init__(self):
        self.setup = Setup()

    def run(self):
        self.setup.setupInfoSet()
        self.setup.setSolr()