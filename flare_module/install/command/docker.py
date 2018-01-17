import os
import subprocess
from config import FlarePath

class Docker():

    DOCKER_NAME = 'eer_trunk'
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
        'docker run -it'
        , '--name {0}'.format(DOCKER_NAME)
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
        print(' '.join(self.DOCKER_RM))
        subprocess.Popen(self.DOCKER_RM)

    def run(self):
        print(' '.join(self.DOCKER_RUN))
        subprocess.Popen(self.DOCKER_RUN)


