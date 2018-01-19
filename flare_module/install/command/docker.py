import subprocess
from config import FlarePath

class Docker():

    DOCKER_NAME = 'eer'
    DOCKER_ENOMIX_HOME = '/home/enomix'
    PORT = {
        'GATEWAY': [19010, 19010],
        'WEBAPPS': [19090, 19090],
        'WEBROOT': [17070, 17070]
    }

    DOCKER_RM = [
        'docker rm -f {0}'.format(DOCKER_NAME)
     ]

    DOCKER_RUN = [
        'docker run -it -d'
        , '--name {0}'.format(DOCKER_NAME)
        , '-h {0}'.format(DOCKER_NAME)
        , '-v {0}:{1}'.format(FlarePath.ORACLE_HOME, DOCKER_ENOMIX_HOME)
        , '-p {0}:{1}'.format(PORT['GATEWAY'][0], PORT['GATEWAY'][1])
        , '-p {0}:{1}'.format(PORT['WEBAPPS'][0], PORT['WEBAPPS'][1])
        , '-p {0}:{1}'.format(PORT['WEBROOT'][0], PORT['WEBROOT'][1])
        , '--cpuset-cpus="0-3"'
        , '--memory=8G'
        , 'centos7/eer:1.3'
    ]

    DOCKER_EER = 'docker exec -it {0} bash -c /home/enomix/bin/flare_{1}.sh'

    def __init__(self):
        pass

    def rm(self):
        self.call(self.DOCKER_RM)

    def run(self):
        self.call(self.DOCKER_RUN)

    def eer_ant(self):
        command = self.DOCKER_EER[0].format(self.DOCKER_NAME, 'ant')
        self.call(command)

    def eer_run(self):
        command = self.DOCKER_EER[0].format(self.DOCKER_NAME, 'run')
        self.call(command)

    def call(self, command):
        if type(command) == str:
            cmd = command
        else:
            cmd = " ".join(command)
        print(cmd)
        subprocess.call(cmd, shell=True)

