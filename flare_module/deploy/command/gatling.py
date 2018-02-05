import os
import wget
from fabric.api import *
from config import FlareEnv, FlareDeploy
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class GatlingServer():
    GATLING_SETUP = [
        FlareDeploy.DEPLOY_TEMP_GATLING_PATH,
        FlareEnv.GATLING["DOWNLOAD_URL"],
    ]

    def __init__(self):
        if not os.path.exists(FlareDeploy.DEPLOY_TEMP_PATH):
            os.makedirs(path)
        if not os.path.exists(self.GATLING_SETUP[0]):
            os.makedirs(path)

        self.gatlingZipName = self.GATLING_SETUP[1][self.GATLING_SETUP[1].rfind('/') + 1:]
        self.gatlingZipPath = self.GATLING_SETUP[0] + '/' + self.gatlingZipName
        if os.path.isfile(self.gatlingZipPath):
            print('Already download gatling : {0}'.format(self.gatlingZipName))
            return

        with lcd(self.GATLING_SETUP[0]):
            local('rm -rf *')

        print('Download gatling: {0}'.format(self.GATLING_SETUP[1]))
        wget.download(self.GATLING_SETUP[1], self.GATLING_SETUP[0])


    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            run(command)


    def deploy_gatling(self):
        # rm remote home
        run('sudo rm -rf {0}'.format(FlareDeploy.REMOTE_HOME))
        # create remote home
        run('mkdir {0}'.format(FlareDeploy.REMOTE_HOME))

        # copy gatling.zip
        put(
            self.gatlingZipPath,
            FlareDeploy.REMOTE_HOME
        )
        # cd remote home
        with cd(FlareDeploy.REMOTE_HOME):
            run('unzip {0}'.format(self.gatlingZipName))
            run('rm -rf {0}'.format(self.gatlingZipName))



