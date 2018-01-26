from fabric.api import *
from config import FlarePath, FlareDocker, FlareDeploy

class FlareServer():


    def __init__(self): pass

    def execute(self, command):
        run(command)

    def compress(self):
        # docker rm
        local('docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME))
        # rm logs
        local('rm -rf {0}'.format(FlarePath.ORACLE_HOME + '/logs'))
        # temp directory remove
        local('rm -rf {0}'.format(FlareDeploy.DEPLOY_TEMP_PATH))
        # create temp directory
        local('mkdir -p {0}'.format(FlareDeploy.DEPLOY_TEMP_PATH))

        # cd oracle home
        with lcd(FlarePath.ORACLE_HOME):
            # tar enomix
            local('tar -cf {0} ../'.format(FlareDeploy.DEPLOY_TAR_NAME))
            # move enomix.tar
            local('mv {0} {1}'.format(FlareDeploy.DEPLOY_TAR_NAME, FlareDeploy.DEPLOY_TEMP_PATH))

