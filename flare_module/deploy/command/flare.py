from fabric.api import *
from config import FlarePath, FlareDeploy

class FlareServer():


    def __init__(self): pass

    def execute(self, command):
        run(command)

    def compress(self):
        with lcd(FlarePath.ORACLE_HOME):
            local('ls -al')


        # # temp directory remove
        # local('rm -rf {0}'.format(FlareDeploy.DEPLOY_TEMP_PATH))
        # # create temp directory
        # local('mkdir -p {0}'.format(FlareDeploy.DEPLOY_TEMP_PATH))
        # # tar enomix
        # local('tar -cf {0} {1}'.format(FlareDeploy.DEPLOY_TAR_NAME, FlarePath.ORACLE_HOME))
        # # move enomix.tar
        # local('mv {0} {1}'.format(FlareDeploy.DEPLOY_TAR_NAME, FlareDeploy.DEPLOY_TEMP_PATH))
