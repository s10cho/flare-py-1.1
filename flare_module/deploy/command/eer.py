from fabric.api import *
from config import FlarePath, FlareEnv, FlareDeploy
from decorator import before, remote

@before(remote(FlareEnv.SERVER["EER"]))
class EERServer():

    def __init__(self): pass

    def execute(self, command):
        run(command)

    def deploy(self):
        run('rm -rf {0}'.format(FlareDeploy.FLARE_DEPLOY_HOME))
        run('mkdir {0}'.format(FlareDeploy.FLARE_DEPLOY_HOME))
        put(FlarePath.TEMP_HOME + '/bin/web.py', FlareDeploy.FLARE_DEPLOY_HOME)
        pass