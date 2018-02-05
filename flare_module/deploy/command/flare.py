import os
import wget
from subprocess import call
from fabric.api import *
from config import FlarePath, FlareDocker, FlareDeploy, FlareEnv

class FlareServer():

    GATLING_SETUP = [
        FlareDeploy.DEPLOY_TEMP_GATLING_PATH,
        FlareEnv.GATLING["DOWNLOAD_URL"],
    ]

    def __init__(self):
        # create deploy temp directory
        if not os.path.exists(FlareDeploy.DEPLOY_TEMP_PATH):
            os.makedirs(FlareDeploy.DEPLOY_TEMP_PATH)
        if not os.path.exists(FlareDeploy.DEPLOY_TEMP_EER_PATH):
            os.makedirs(self.GATLING_SETUP[0])
        if not os.path.exists(self.GATLING_SETUP[0]):
            os.makedirs(self.GATLING_SETUP[0])

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
            local('tar -cf {0} ../'.format(FlareDeploy.DEPLOY_EER_TAR_NAME))
            # move enomix.tar
            local('mv {0} {1}'.format(FlareDeploy.DEPLOY_EER_TAR_NAME, FlareDeploy.DEPLOY_TEMP_EER_PATH))

    def prepare_gatling(self):
        self.gatlingZipName = self.GATLING_SETUP[1][self.GATLING_SETUP[1].rfind('/') + 1:]
        self.gatlingZipPath = self.GATLING_SETUP[0] + '/' + self.gatlingZipName
        if os.path.isfile(self.gatlingZipPath):
            print('Already download gatling : {0}'.format(self.gatlingZipName))
            return

        with lcd(self.GATLING_SETUP[0]):
            local('rm -rf *')

        print('Download gatling: {0}'.format(self.GATLING_SETUP[1]))
        wget.download(self.GATLING_SETUP[1], self.GATLING_SETUP[0])
