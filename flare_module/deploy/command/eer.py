from fabric.api import *
from config import FlareEnv, FlareDeploy, FlareDocker
from decorator import before, remote

@before(remote(FlareEnv.SERVER["EER"]))
class EERServer():

    DOCKER_RM = 'docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME)

    DOCKER_RUN = [
        'docker run -it -d'
        , '--name {0}'.format(FlareDocker.ENOMIX_NAME)
        , '-h {0}'.format(FlareDocker.ENOMIX_NAME)
        , '-v {0}:{1}'.format(FlareDeploy.REMOTE_ORACLE_HOME, FlareDocker.ENOMIX_HOME)
        , '-p {0}:{1}'.format(FlareDocker.PORT['GATEWAY'][0], FlareDocker.PORT['GATEWAY'][1])
        , '-p {0}:{1}'.format(FlareDocker.PORT['WEBAPPS'][0], FlareDocker.PORT['WEBAPPS'][1])
        , '-p {0}:{1}'.format(FlareDocker.PORT['WEBROOT'][0], FlareDocker.PORT['WEBROOT'][1])
        , '-p {0}:{1}'.format(FlareDocker.PORT['SCOUTER'][0], FlareDocker.PORT['SCOUTER'][1])
        , '-p {0}:{1}/udp'.format(FlareDocker.PORT['SCOUTER'][0], FlareDocker.PORT['SCOUTER'][1])
        , '--cpuset-cpus=0-3'
        , '--memory=8G'
        , 'centos7/eer:1.1'
    ]

    DOCKER_EER = 'docker exec -it {0} bash -c /home/enomix/bin/flare_eer_{1}.sh'

    def __init__(self): pass

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        with settings(warn_only=True):
            result = run(command)
            print(result.stdout)

    def deploy(self):
        # rm remote home
        run('sudo rm -rf {0}'.format(FlareDeploy.REMOTE_HOME))
        # create remote home
        run('mkdir {0}'.format(FlareDeploy.REMOTE_HOME))

        # copy enomix.tar
        put(
            FlareDeploy.DEPLOY_TEMP_EER_PATH + '/' + FlareDeploy.DEPLOY_EER_TAR_NAME,
            FlareDeploy.REMOTE_HOME
        )
        # cd remote home
        with cd(FlareDeploy.REMOTE_HOME):
            run('tar -xf {0}'.format(FlareDeploy.DEPLOY_EER_TAR_NAME))
            run('rm -rf {0}'.format(FlareDeploy.DEPLOY_EER_TAR_NAME))

    def docker_rm(self):
        self.execute(self.DOCKER_RM)

    def docker_run(self):
        self.execute(self.DOCKER_RUN)

    def docker_eer_scouter(self):
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'scouter')
        self.execute(command)

    def docker_eer_run(self):
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'run')
        self.execute(command)
