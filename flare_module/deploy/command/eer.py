from fabric.api import *
from config import FlareEnv, FlareDeploy
from decorator import before, remote

@before(remote(FlareEnv.SERVER["EER"]))
class EERServer():
    EER_DEPOLY = [
        'rm -rf {0}'.format(FlareDeploy.FLARE_DEPLOY_HOME),
        'mkdir {0}'.format(FlareDeploy.FLARE_DEPLOY_HOME)
    ]

    def __init__(self): pass

    def execute(self, command):
        run(command)

    def deploy(self):
        for command in self.EER_DEPOLY:
            run(command)
        pass