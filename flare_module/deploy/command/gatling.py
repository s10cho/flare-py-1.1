from fabric.api import *
from config import FlareEnv, FlareDeploy
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class GatlingServer():

    SVN_CHECKOUT = [
        'svn checkout',
        '--username {0}'.format(FlareEnv.GATLING['ID']),
        '--password {0}'.format(FlareEnv.GATLING['PASSWORD']),
        '{0}'.format(FlareEnv.GATLING['URL'])
    ]

    MVN_CLEAN_COMPILE = 'mvn clean compile'

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

        # cd remote home
        with cd(FlareDeploy.REMOTE_HOME):
            # svn checkout
            self.execute(self.SVN_CHECKOUT)

        # cd gatling home
        with cd(FlareDeploy.REMOTE_GATLING_HOME):
            # maven clean compile
            self.execute(self.MVN_CLEAN_COMPILE)
