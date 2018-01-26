from fabric.api import *
from config import FlarePath, FlareEnv
from decorator import before, remote

#@before(remote(FlareEnv.SERVER["FLARE"]))
class FlareServer():
    DEPLOY_TEMP_PATH = FlarePath.TEMP_HOME + '/deploy'
    DEPLOY_TAR_NAME = 'enomix.tar'

    def __init__(self): pass

    def execute(self, command):
        run(command)

    def compress(self):
        local('rm -rf {0}'.format(self.DEPLOY_TEMP_PATH))
        local('mkdir -p {0}'.format(self.DEPLOY_TEMP_PATH))
        local('cd {0}'.format(FlarePath.ORACLE_HOME))
        local('tar -cvf {0} {1}'.format(self.DEPLOY_TAR_NAME, FlarePath.ORACLE_HOME))
        local('mv {0} {1}'.format(self.DEPLOY_TAR_NAME, self.DEPLOY_TEMP_PATH))
