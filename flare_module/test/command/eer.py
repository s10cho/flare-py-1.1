from fabric.api import *
from config import FlareEnv, FlareDeploy, FlareDocker, FlarePath
from decorator import before, remote
import datetime

@before(remote(FlareEnv.SERVER["EER"]))
class EERServer():

    DOCKER_RM = 'docker rm -f {0}'.format(FlareDocker.ENOMIX_NAME)

    DOCKER_EER = 'docker exec -it {0} bash -c /home/enomix/bin/flare_eer_{1}.sh'

    DOCKER_MONITORING_RUN = FlareDeploy.REMOTE_DOCKER_MONITORING_HOME + '/bin/docker_monitoring_run.sh {0}'

    DOCKER_MONITORING_STOP = FlareDeploy.REMOTE_DOCKER_MONITORING_HOME + '/bin/docker_monitoring_stop.sh'

    def __init__(self): pass

    def execute(self, command):
        if type(command) == list:
            command = " ".join(command)

        print(command)

        with settings(warn_only=True):
            run(command)

    def background_run(self, command):
        command = 'nohup %s &> /dev/null &' % command
        run(command, pty=False)

    def execute_background(self, command):
        if type(command) == list:
            command = " ".join(command)

        print(command)

        execute(self.background_run, command)

    def change_ecc_shell(self, docker_memory):
        command = [
            'cp'
            , FlareDeploy.REMOTE_ENOMIX_ORACLE_HOME + '/bin/ecc_{0}.sh'.format(docker_memory)
            , FlareDeploy.REMOTE_ENOMIX_ORACLE_HOME + '/bin/ecc.sh'
        ]
        self.execute(command)

    def get_docker_run_command(self, dockerCpu, dockerMemory):
        command = [
            'docker run -it -d'
            , '--name {0}'.format(FlareDocker.ENOMIX_NAME)
            , '-h {0}/{1}'.format(FlareDocker.ENOMIX_NAME, FlareEnv.SERVER["EER"]["HOSTS"][0])
            , '-v {0}:{1}'.format(FlareDeploy.REMOTE_ENOMIX_ORACLE_HOME, FlareDocker.ENOMIX_HOME)
            , '-v /etc/localtime:/etc/localtime:ro'
            , '-p {0}:{1}'.format(FlareDocker.PORT['GATEWAY'][0], FlareDocker.PORT['GATEWAY'][1])
            , '-p {0}:{1}'.format(FlareDocker.PORT['WEBAPPS'][0], FlareDocker.PORT['WEBAPPS'][1])
            , '-p {0}:{1}'.format(FlareDocker.PORT['WEBROOT'][0], FlareDocker.PORT['WEBROOT'][1])
            , '-p {0}:{1}'.format(FlareDocker.PORT['SCOUTER'][0], FlareDocker.PORT['SCOUTER'][1])
            , '-p {0}:{1}/udp'.format(FlareDocker.PORT['SCOUTER'][0], FlareDocker.PORT['SCOUTER'][1])
            , '--cpuset-cpus={0}'.format(dockerCpu)
            , '--memory={0}'.format(dockerMemory)
            , 'centos7/eer:1.1'
        ]
        self.execute(command)

    def docker_restart(self, cpu, memory):
        dockerCpu = '0-{0}'.format(cpu-1)
        dockerMemory = '{0}G'.format(memory)

        # docker rm
        self.execute(self.DOCKER_RM)

        # change ecc shell
        self.change_ecc_shell(dockerMemory)

        # docker run
        self.get_docker_run_command(dockerCpu, dockerMemory)

        # docker scouter run
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'scouter')
        self.execute(command)

        # docker eer run
        command = self.DOCKER_EER.format(FlareDocker.ENOMIX_NAME, 'run')
        self.execute(command)

    def docker_monitoring_run(self, logName):
        command = self.DOCKER_MONITORING_RUN.format(logName)
        self.execute_background(command)

    def docker_monitoring_stop(self):
        command = self.DOCKER_MONITORING_STOP
        self.execute_background(command)

    def monitoring_data_download(self, outputBaseName):
        last_log_info = FlarePath.FLARE_RESULT + '/last_log_info'
        f = open(last_log_info, 'r', encoding='UTF8')
        log_file_path = f.read()
        f.close()

        with cd(FlareDeploy.REMOTE_DOCKER_MONITORING_HOME + '/logs'):
            lsOutput = run('ls')
            fileNames = lsOutput.split()
            for fileName in fileNames:
                if fileName.find(outputBaseName) > -1:
                    get(fileName, log_file_path)

                    last_log_info = FlarePath.FLARE_RESULT + 'last_log_info'
                    f = open(last_log_info, 'w', encoding='UTF8')
                    f.write(log_file_path + '/' + fileName)
                    f.close()



