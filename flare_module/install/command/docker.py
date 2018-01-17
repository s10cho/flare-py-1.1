import os
import subprocess
from config import FlarePath

class Docker():

    DOCKER_NAME = 'eer_trunk'
    DOCKER_ENOMIX_HOME = '/home/enomix'
    GATEWAY_PORT = [19010, 19010]
    WEBAPPS_PORT = [19090, 19090]
    WEBROOT_PORT = [17070, 17070]

    DOCKER_RM = [
        'docker', 'rm', '-f', DOCKER_NAME
     ]

    DOCKER_RUN = [
        'docker', 'run', '-it'
        , '--name', DOCKER_NAME
        , '-v', '{0}:{1}'.format(FlarePath.ORACLE_HOME, DOCKER_ENOMIX_HOME)
        , '-p', '{0}:{1}'.format(GATEWAY_PORT[0], GATEWAY_PORT[1])
        , '-p', '{0}:{1}'.format(WEBAPPS_PORT[0], WEBAPPS_PORT[1])
        , '-p', '{0}:{1}'.format(WEBROOT_PORT[0], WEBROOT_PORT[1])
        , '--cpuset-cpus="0-3"'
        , '--memory=8G'
        , 'centos7/eer:1.0'
    ]

    def __init__(self):
        pass

    def rm(self):
        print(' '.join(self.DOCKER_RM))
        p = subprocess.Popen(self.DOCKER_RM, shell=True)
        p.wait()
        pass

    def run(self):
        print(' '.join(self.DOCKER_RUN))
        p = subprocess.Popen(self.DOCKER_RUN, shell=True)
        p.wait()


