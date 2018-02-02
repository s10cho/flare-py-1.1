import os
import wget
import shutil
from fabric.api import *
from config import FlarePath, FlareEnv

class Scouter():

    SCOUTER_SETUP = [
        FlarePath.TEMP_HOME + '/scouter',
        FlareEnv.SCOUTER["DOWNLOAD_URL"],
        FlarePath.ORACLE_HOME + '/scouter'
    ]

    STORE_SCOUTER_CONF_PATH = [
        FlareEnv.STORE["PATH"] + '/scouter/conf',
        FlarePath.TEMP_HOME + '/scouter/agent.java/conf',
    ]

    SERVER_IP = FlareEnv.SERVER["FLARE"]["HOSTS"][0]

    ECC_SH = [
        FlarePath.ORACLE_HOME + '/setup/frame/bin/ecc.sh',
        FlarePath.TEMP_HOME + '/scouter/ecc.sh'
    ]

    JVM_OPTION = [
        ['gateway', 256, 256],
        ['router', 256, 256],
        ['engine', 1024, 1024],
        ['rtis', 256, 256],
        ['webapps', 1024, 1024],
        ['restapi', 1024, 1024],
        ['webroot', 128, 128],
        ['thirdparty', 256, 256],
        ['legw', 256, 256],
    ]

    def __init__(self):
        tempDir = [
            '/scouter'
        ]
        # create temp directory
        for dir in tempDir:
            path = FlarePath.TEMP_HOME + dir
            if not os.path.exists(path):
                os.makedirs(path)

        self.scouterTarName = self.SCOUTER_SETUP[1][self.SCOUTER_SETUP[1].rfind('/') + 1:]

    def agent_set(self):
        self.download()
        self.deploy_agent()

    def download(self):
        scouterTarPath = self.SCOUTER_SETUP[0] + '/' + self.scouterTarName
        if os.path.isfile(scouterTarPath):
            return

        with lcd(self.SCOUTER_SETUP[0]):
            local('rm -rf *')

        print('Download scouter: {0}'.format(self.SCOUTER_SETUP[1]))
        wget.download(self.SCOUTER_SETUP[1], self.SCOUTER_SETUP[0])

        with lcd(self.SCOUTER_SETUP[0]):
            local('tar -xf {0}'.format(self.scouterTarName))
            local('mv ./scouter/* .')
            local('rmdir scouter')

        local('cp {0}/* {1}/'.format(self.STORE_SCOUTER_CONF_PATH[0], self.STORE_SCOUTER_CONF_PATH[1]))

        self.modify_conf()


    def modify_conf(self):
        for scouterModule in ['/agent.java', '/agent.host']:
            scouterPath = self.SCOUTER_SETUP[0] + scouterModule
            confFile = scouterPath + '/conf/scouter.conf'
            with open(confFile, "a") as f:
                f.write("net_collector_ip={0}\n".format(self.SERVER_IP))


    def deploy_agent(self):
        if os.path.exists(self.SCOUTER_SETUP[2]):
            with lcd(self.SCOUTER_SETUP[2]):
                local('rm -rf *')

        for scouterModule in ['/agent.java', '/agent.host']:
            scouterPath = self.SCOUTER_SETUP[0] + scouterModule
            deployPath = self.SCOUTER_SETUP[2]
            local('mkdir -p {0}'.format(deployPath))
            local('cp -r {0} {1}'.format(scouterPath, deployPath))

        self.create_ecc_sh()


    def create_ecc_sh(self):
        source = self.ECC_SH[0]
        temp = self.ECC_SH[1]
        sourceFile = open(source, 'r', encoding='UTF8')

        if 'SCT_OPTS' in sourceFile.read():
            sourceFile.close()
            print("Already created ecc.sh")
            return

        sourceFile.seek(0, 0)
        tempFile = open(temp, 'w', encoding='UTF8')
        for line in sourceFile.readlines():
            if 'JVM_OPTS' in line and '-Xms128m -Xmx512m' in line:
                line = line.replace('-Xms128m -Xmx512m', '$SCT_OPTS')

            tempFile.write(line)

            for jvmOpts in self.JVM_OPTION:
                checkLine = 'BASE_RESOURCE=webapps/{0}'.format(jvmOpts[0])
                if checkLine in line:
                    scouter_opts = '        SCT_OPTS="' \
                                   '-Xms{1}m -Xmx{2}m ' \
                                   '-javaagent:$ENOMIX_HOME/scouter/agent.java/scouter.agent.jar ' \
                                   '-Dscouter.config=$ENOMIX_HOME/scouter/agent.java/conf/scouter_{0}.conf' \
                                   '"\n'.format(jvmOpts[0], jvmOpts[1], jvmOpts[2])
                    tempFile.write(scouter_opts)

        sourceFile.close()
        tempFile.close()
        local('sudo cp -r {0} {1}'.format(temp, source))
