from flare_module.deploy.command.eer import EERServer
from flare_module.deploy.command.flare import FlareServer
from flare_module.deploy.command.gatling import GatlingServer

class DeployService():
    def __init__(self):
        self.eer = EERServer()
        self.flare = FlareServer()
        self.gatling = GatlingServer()

    def run(self, param):
        if len(param) == 0:
            self.flare.compress()
            self.eer.deploy()
        else:
            # command run
            command = param[0]
            print(command)



