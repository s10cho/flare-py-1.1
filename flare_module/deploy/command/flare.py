import os
import subprocess
from fabric.api import *
from config import FlarePath, FlareDocker, FlareDeploy

class FlareServer():

    def __init__(self):
        # create deploy temp directory
        path = FlareDeploy.DEPLOY_TEMP_PATH
        if not os.path.exists(path):
            os.makedirs(path)

    def execute(self, command):
        run(command)

    def prepare_eer(self):
        # docker rm
        cmd  = 'docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME)
        subprocess.call(cmd, shell=True)
        # rm logs
        local('sudo rm -rf {0}'.format(FlarePath.ORACLE_HOME + '/logs'))
        # temp directory remove
        local('rm -rf {0}'.format(FlareDeploy.DEPLOY_TEMP_EER_PATH))
        # create temp directory
        local('mkdir -p {0}'.format(FlareDeploy.DEPLOY_TEMP_EER_PATH))

        # cd oracle home
        with lcd(FlarePath.ORACLE_HOME):
            # tar enomix
            local('tar -cf {0} ../'.format(FlareDeploy.DEPLOY_EER_TAR_NAME))
            # move enomix.tar
            local('mv {0} {1}'.format(FlareDeploy.DEPLOY_EER_TAR_NAME, FlareDeploy.DEPLOY_TEMP_EER_PATH))

    def prepare_gatling(self):

        pass
