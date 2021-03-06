import decorator
from config import FlarePath, FlareProcess
from flare_module.deploy.command.eer import EERServer
from flare_module.deploy.command.flare import FlareServer
from flare_module.deploy.command.gatling import GatlingServer

class DeployService():

    @decorator.chown_path(FlarePath.ORACLE_HOME)
    def __init__(self):
        self.eer = EERServer()
        self.flare = FlareServer()
        self.gatling = GatlingServer()

    def run(self, param):
        if FlareProcess.DEPLOY == 'Y':
            if len(param) == 0:
                self.flare.prepare_eer()
                self.flare.prepare_gatling()
                self.eer.docker_rm()
                self.eer.deploy()
                self.eer.docker_run()
                self.eer.docker_eer_scouter()
                self.eer.docker_eer_run()
                self.gatling.deploy_gatling()
            else:
                # command run
                command = param[0]
                print(command)
                if command == 'ready':
                    self.flare.prepare_eer()
                    self.flare.prepare_gatling()
                if command == 'eer':
                    self.eer.docker_rm()
                    self.eer.deploy()
                    self.eer.docker_run()
                    self.eer.docker_eer_scouter()
                    self.eer.docker_eer_run()
                if command == 'gatling':
                    self.gatling.deploy_gatling()



