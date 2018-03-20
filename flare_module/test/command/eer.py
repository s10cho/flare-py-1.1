from fabric.api import *
from config import FlareEnv, FlareDeploy, FlareDocker
from decorator import before, remote

@before(remote(FlareEnv.SERVER["EER"]))
class EERServer():

    DOCKER_RM = 'docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME)

    DOCKER_EER = 'docker exec -it {0} bash -c /home/enomix/bin/flare_eer_{1}.sh'

    def __init__(self): pass

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)

        print(command)

        # with settings(warn_only=True):
        #     run(command)

    def change_ecc_shell(self, docker_memory):
        command = [
            'cp'
            , FlareDeploy.REMOTE_ENOMIX_ORACLE_HOME + '/bin/ecc_{0}.sh'.format(docker_memory)
            , FlareDeploy.REMOTE_ENOMIX_ORACLE_HOME + '/bin/ecc.sh'
        ]
        return " ".join(command)

    def get_docker_run_command(self, dockerCpu, dockerMemory):
        command = [
            'docker run -it -d'
            , '--name {0}'.format(FlareDocker.ENOMIX_NAME)
            , '-h {0}/{1}'.format(FlareDocker.ENOMIX_NAME, FlareEnv.SERVER["EER"]["HOSTS"][0])
            , '-v {0}:{1}'.format(FlareDeploy.REMOTE_ENOMIX_ORACLE_HOME, FlareDocker.ENOMIX_HOME)
            , '-p {0}:{1}'.format(FlareDocker.PORT['GATEWAY'][0], FlareDocker.PORT['GATEWAY'][1])
            , '-p {0}:{1}'.format(FlareDocker.PORT['WEBAPPS'][0], FlareDocker.PORT['WEBAPPS'][1])
            , '-p {0}:{1}'.format(FlareDocker.PORT['WEBROOT'][0], FlareDocker.PORT['WEBROOT'][1])
            , '-p {0}:{1}'.format(FlareDocker.PORT['SCOUTER'][0], FlareDocker.PORT['SCOUTER'][1])
            , '-p {0}:{1}/udp'.format(FlareDocker.PORT['SCOUTER'][0], FlareDocker.PORT['SCOUTER'][1])
            , '--cpuset-cpus={0}'.format(dockerCpu)
            , '--memory={0}'.format(dockerMemory)
            , 'centos7/eer:1.1'
        ]
        return " ".join(command)

    def docker_restart(self, cpu, memory):
        dockerCpu = '0-{0}'.format(cpu-1)
        dockerMemory = '{0}G'.format(memory)

        # docker rm
        self.execute(self.DOCKER_RM)

        # change ecc shell
        command = self.change_ecc_shell(dockerMemory)
        self.execute(command)

        # docker run
        command = self.get_docker_run_command(dockerCpu, dockerMemory)
        self.execute(command)

        # docker scouter run
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'scouter')
        self.execute(command)

        # docker eer run
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'run')
        self.execute(command)