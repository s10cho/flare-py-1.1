import os
import wget
from fabric.api import *
from config import FlareEnv, FlareDeploy, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class GatlingServer():

    SVN_CHECKOUT = [
        'svn checkout',
        '--username {0}'.format(FlareEnv.SVN['ID']),
        '--password {0}'.format(FlareEnv.SVN['PASSWORD']),
        '{0} {1}'
    ]

    def __init__(self): pass


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
            FlareDeploy.DEPLOY_TEMP_GATLING_PATH + '/' + 'gatling*.zip',
            FlareDeploy.REMOTE_HOME
        )
        # cd remote home
        with cd(FlareDeploy.REMOTE_HOME):
            run('unzip {0}'.format(self.gatlingZipName))
            run('rm -rf {0}'.format(self.gatlingZipName))
            run('mv {0} gatling'.format(self.gatlingZipName[0:self.gatlingZipName.rfind('-')]))

        with cd(FlareDeploy.REMOTE_GATLING_HOME + '/user-files/simulations'):
            run('sudo rm -rf *')

        with cd(FlareDeploy.REMOTE_GATLING_HOME + '/user-files/data'):
            run('sudo rm -rf *')

        put(
            FlarePath.FLARE_FRAME + '/deploy/gatling/lib/*',
            FlareDeploy.REMOTE_GATLING_HOME +'/lib'
        )


    def deploy_gatling_script(self):
        checkoutList = [
            [
                FlareEnv.GATLING["GATLING_DATA"],
                FlareDeploy.REMOTE_GATLING_HOME + '/user-files/data'
            ],
            [
                FlareEnv.GATLING["GATLING_SCRIPT"],
                FlareDeploy.REMOTE_GATLING_HOME + '/user-files/simulations'
            ]
        ]

        for checkout in checkoutList:
            command = " ".join(self.SVN_CHECKOUT).format(checkout[0], checkout[1])
            print(command)
            run(command)


