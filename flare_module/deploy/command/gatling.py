import os
import wget
from fabric.api import *
from config import FlareEnv, FlareDeploy, FlarePath
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class GatlingServer():

    SVN_CHECKOUT = [
        'svn checkout',
        '--username {0}'.format(FlareEnv.GATLING['ID']),
        '--password {0}'.format(FlareEnv.GATLING['PASSWORD']),
        '{0}'.format(FlareEnv.GATLING['URL'])
    ]

    def __init__(self): pass


    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            run(command)


    def deploy_gatling(self):
        # create remote home
        run('mkdir -p {0}'.format(FlareDeploy.REMOTE_HOME))

        # cd remote home
        with cd(FlareDeploy.REMOTE_HOME):
            self.execute(self.SVN_CHECKOUT)




