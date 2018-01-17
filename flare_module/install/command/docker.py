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
        'docker run -t'
        , '--name {0}'.format(DOCKER_NAME)
        , '-h {0}'.format(DOCKER_NAME)
        , '-v {0}:{1}'.format(FlarePath.ORACLE_HOME, DOCKER_ENOMIX_HOME)
        , '-p {0}:{1}'.format(PORT['GATEWAY'][0], PORT['GATEWAY'][1])
        , '-p {0}:{1}'.format(PORT['WEBAPPS'][0], PORT['WEBAPPS'][1])
        , '-p {0}:{1}'.format(PORT['WEBROOT'][0], PORT['WEBROOT'][1])
        , '--cpuset-cpus="0-3"'
        , '--memory=8G'
        , 'centos7/eer:1.0'
    ]

    def __init__(self):
        pass

    def rm(self):
        self.call(self.DOCKER_RM)

    def run(self):
        self.call(self.DOCKER_RUN)

    def call(self, command):
        cmd = " ".join(command)
        print(cmd)
        subprocess.call(cmd, shell=True)

