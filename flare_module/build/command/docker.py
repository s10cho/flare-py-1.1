import subprocess
from config import FlarePath, FlareDocker, FlareEnv

class Docker():

    DOCKER_RM = [
        'docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME)
     ]

    DOCKER_RUN = [
        'docker run -it -d'
        , '--name {0}'.format(FlareDocker.ENOMIX_NAME)
        , '-h {0}/{1}'.format(FlareDocker.ENOMIX_NAME, FlareEnv.SERVER["FLARE"]["HOSTS"][0])
        , '-v {0}:{1}'.format(FlarePath.ORACLE_HOME, FlareDocker.ENOMIX_HOME)
        , '-p {0}:{1}'.format(FlareDocker.PORT['GATEWAY'][0], FlareDocker.PORT['GATEWAY'][1])
        , '-p {0}:{1}'.format(FlareDocker.PORT['WEBAPPS'][0], FlareDocker.PORT['WEBAPPS'][1])
        , '-p {0}:{1}'.format(FlareDocker.PORT['WEBROOT'][0], FlareDocker.PORT['WEBROOT'][1])
        , '--cpuset-cpus=0-3'
        , '--memory=8G'
        , 'centos7/eer:1.1'
    ]

    DOCKER_EER = 'docker exec -t {0} bash -c /home/enomix/bin/flare_eer_{1}.sh'

    def __init__(self): pass

    def rm(self):
        self.execute(self.DOCKER_RM)

    def run(self):
        self.execute(self.DOCKER_RUN)

    def eer_ant(self):
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'ant')
        self.execute(command)

    def eer_run(self):
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'run')
        self.execute(command)

    def eer_scouter(self):
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'scouter')
        self.execute(command)

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)
        subprocess.call(command, shell=True)



