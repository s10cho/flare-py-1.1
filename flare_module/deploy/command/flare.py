from fabric.api import *
from config import FlarePath, FlareEnv
from decorator import before, remote

#@before(remote(FlareEnv.SERVER["FLARE"]))
class FlareServer():
    DEPLOY_TEMP_PATH = FlarePath.TEMP_HOME + '/deploy'

    def __init__(self): pass

    def execute(self, command):
        run(command)

    def compress(self):
        local('rm -rf {0}'.format(self.DEPLOY_TEMP_PATH))
        local('mkdir -p {0}'.format(self.DEPLOY_TEMP_PATH))
        local('cd {0}'.format(FlarePath.ORACLE_HOME))
        local('ls -al')
