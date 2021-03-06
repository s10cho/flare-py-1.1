import os
import wget
import shutil
from fabric.api import *
from config import FlarePath, FlareEnv

class Scouter():

    SCOUTER_SETUP = [
        FlarePath.FLARE_TEMP + '/scouter',
        FlareEnv.SCOUTER["DOWNLOAD_URL"],
        FlarePath.ORACLE_HOME + '/scouter'
    ]

    STORE_SCOUTER_CONF_PATH = [
        FlarePath.FLARE_FRAME + '/build/scouter/conf',
        FlarePath.FLARE_TEMP + '/scouter/agent.java/conf',
    ]

    SERVER_IP = FlareEnv.SERVER["FLARE"]["HOSTS"][0]

    ECC_SH = [
        FlarePath.ORACLE_HOME + '/setup/frame/bin/ecc.sh',
        FlarePath.FLARE_TEMP + '/scouter/ecc_{0}.sh'
    ]

    JVM_OPTIONS = {
        "4G": [
            ['gateway', 256, 256],
            ['router', 256, 256],
            ['engine', 512, 512],
            ['rtis', 256, 256],
            ['webapps', 512, 512],
            ['restapi', 1024, 1024],
            ['webroot', 256, 256],
            ['thirdparty', 256, 256],
            ['legw', 256, 256],
        ],
        "8G": [
            ['gateway', 256, 256],
            ['router', 256, 256],
            ['engine', 1024, 1024],
            ['rtis', 256, 256],
            ['webapps', 1024, 1024],
            ['restapi', 1024, 1024],
            ['webroot', 128, 128],
            ['thirdparty', 256, 256],
            ['legw', 256, 256],
        ],
        "16G": [
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
    }

    def __init__(self):
        tempDir = ['/scouter']
        # create temp directory
        for dir in tempDir:
            path = FlarePath.FLARE_TEMP + dir
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

        for memory in self.JVM_OPTIONS.keys():
            self.create_ecc_sh(self.ECC_SH[0], self.ECC_SH[1], memory)

        # overwrite
        self.deploy_ecc_sh(self.ECC_SH[0], self.ECC_SH[1].format("8G"))
        # copy
        copyPath = self.ECC_SH[0][:self.ECC_SH[0].rfind('/')]
        self.deploy_ecc_sh(copyPath, self.ECC_SH[1].format("4G"))
        self.deploy_ecc_sh(copyPath, self.ECC_SH[1].format("16G"))


    def create_ecc_sh(self, source, temp, memory):
        sourceFile = open(source, 'r', encoding='UTF8')

        if 'SCT_OPTS' in sourceFile.read():
            sourceFile.close()
            print("Already created ecc.sh")
            return

        sourceFile.seek(0, 0)
        temp = temp.format(memory)
        tempFile = open(temp, 'w', encoding='UTF8')
        for line in sourceFile.readlines():
            if 'JVM_OPTS' in line and '-Xms128m -Xmx512m' in line:
                line = line.replace('-Xms128m -Xmx512m', '$SCT_OPTS')

            tempFile.write(line)

            for jvmOpts in self.JVM_OPTIONS[memory]:
                checkLine = 'BASE_RESOURCE=webapps/{0}'.format(jvmOpts[0])
                if checkLine in line:
                    module_jvm = '-Xms{1}m -Xmx{2}m ' \
                       '-javaagent:$ENOMIX_HOME/scouter/agent.java/scouter.agent.jar ' \
                       '-Dscouter.config=$ENOMIX_HOME/scouter/agent.java/conf/scouter_{0}.conf'.format(jvmOpts[0], jvmOpts[1], jvmOpts[2])

                    if jvmOpts[0] == 'webroot':
                        module_jvm = module_jvm + ' -Dproxy.pool.maxTotal=500'

                    scouter_opts = '        SCT_OPTS="{0}"\n'.format(module_jvm)
                    tempFile.write(scouter_opts)

        sourceFile.close()
        tempFile.close()
        shutil.copy(temp.format(), source[:source.rfind('/')])

    def deploy_ecc_sh(self, source, temp):
        shutil.copy(temp, source)
