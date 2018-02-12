import os
from subprocess import call
from fabric.api import *
from config import FlarePath, FlareDocker, FlareDeploy, FlareEnv

class FlareServer():

    EER_SETUP = [
        FlareDeploy.DEPLOY_TEMP_EER_PATH,
        FlareDeploy.DEPLOY_EER_TAR_NAME
    ]

    def __init__(self):
        # create deploy temp directory
        if not os.path.exists(FlareDeploy.DEPLOY_TEMP_PATH):
            os.makedirs(FlareDeploy.DEPLOY_TEMP_PATH)
        if not os.path.exists(self.EER_SETUP[0]):
            os.makedirs(self.EER_SETUP[0])

    def prepare_eer(self):
        # docker rm
        cmd  = 'docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME)
        call(cmd, shell=True)
        # rm logs
        local('sudo rm -rf {0}'.format(FlarePath.ORACLE_HOME + '/logs'))
        with lcd(FlareDeploy.DEPLOY_TEMP_EER_PATH):
            local('rm -rf *')

        # cd oracle home
        with lcd(FlarePath.ORACLE_HOME):
            # tar enomix
            local('tar -cf {0} ../'.format(self.EER_SETUP[1]))
            # move enomix.tar
            local('mv {0} {1}'.format(self.EER_SETUP[1], self.EER_SETUP[0]))

    def prepare_gatling(self): pass
