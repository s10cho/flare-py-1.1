from fabric.api import *
from config import FlareEnv, FlareDeploy
from decorator import before, remote

@before(remote(FlareEnv.SERVER["EER"]))
class EERServer():

    def __init__(self): pass

    def execute(self, command):
        run(command)

    def deploy(self):
        # rm remote home
        run('rm -rf {0}'.format(FlareDeploy.REMOTE_HOME))
        # create remote home
        run('mkdir {0}'.format(FlareDeploy.REMOTE_HOME))

        # copy enomix.tar
        put(
            FlareDeploy.DEPLOY_TEMP_PATH + '/' + FlareDeploy.DEPLOY_TAR_NAME,
            FlareDeploy.REMOTE_HOME
        )
        # cd remote home
        with cd(FlareDeploy.REMOTE_HOME):
            run('tar -xf {0}'.format(FlareDeploy.DEPLOY_TAR_NAME))
            run('rm -rf {0}'.format(FlareDeploy.DEPLOY_TAR_NAME))
