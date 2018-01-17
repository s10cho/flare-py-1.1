import os
import subprocess
from config import FlarePath

class Docker():

    DOCKER_NAME = 'eer_trunk'
    DOCKER_ENOMIX_HOME = '/home/enomix'

    DOCKER_RM = 'docker rm -f {0}'.format(DOCKER_NAME)

    DOCKER_RUN = [
        'docker run',
        '-it',
        '--name {0}'.format(DOCKER_NAME),
        '-h eer_trunk',
        '-v {0}:{1}'.format(FlarePath.ORACLE_HOME, DOCKER_ENOMIX_HOME),
        '-p 19010:19010 -p 19090:19090 -p 17070:17070'
        '--cpuset-cpus="0-3"',
        '--memory=8G',
        'centos7/eer:1.0'
    ]

    def __init__(self):
        pass

    def rm(self):
        subprocess.call(self.DOCKER_RM, shell=True)
        pass

    def run(self):
        subprocess.call(self.DOCKER_RUN, shell=True)
