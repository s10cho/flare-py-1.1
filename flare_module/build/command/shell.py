import os
import shutil
from config import FlarePath

class Shell():
    SHELL_PATH = [
        FlarePath.ORACLE_HOME + '/bin',
        FlarePath.FLARE_TEMP + '/bin'
    ]

    SHELL_FILE_FORMAT = 'flare_eer_{0}.sh'

    SHELL_INFO = [
        {
            'name': SHELL_FILE_FORMAT.format('ant'),
            'contents': '#!/bin/bash\n'
                        'export JAVA_HOME=/usr/java/jdk1.8.0_151\n'
                        'export ANT_HOME=/usr/java/apache-ant-1.10.1\n'
                        'export PATH=$PATH:$HOME/bin:$JAVA_HOME/bin:$ANT_HOME/bin\n'
                        'cd /home/enomix/setup\n'
                        'ant\n'
        },
        {
            'name': SHELL_FILE_FORMAT.format('run'),
            'contents': '#!/bin/bash\n'
                        'cd /home/enomix/bin\n'
                        './all_run.sh\n'
                        'cd /home/enomix/apps/solr\n'
                        './run.sh > /dev/null\n'
                        'cd /home/enomix/apps/bin\n'
                        './dummy_chatbot_run.sh > /dev/null\n'
        },
        {
            'name': SHELL_FILE_FORMAT.format('4G_run'),
            'contents': '#!/bin/bash\n'
                        'cd /home/enomix/bin\n'
                        'cp ecc_4G.sh ecc.sh\n'
                        './all_run.sh\n'
                        'cd /home/enomix/apps/solr\n'
                        './run.sh > /dev/null\n'
                        'cd /home/enomix/apps/bin\n'
                        './dummy_chatbot_run.sh > /dev/null\n'
        },
        {
            'name': SHELL_FILE_FORMAT.format('8G_run'),
            'contents': '#!/bin/bash\n'
                        'cd /home/enomix/bin\n'
                        'cp ecc_8G.sh ecc.sh\n'
                        './all_run.sh\n'
                        'cd /home/enomix/apps/solr\n'
                        './run.sh > /dev/null\n'
                        'cd /home/enomix/apps/bin\n'
                        './dummy_chatbot_run.sh > /dev/null\n'
        },
        {
            'name': SHELL_FILE_FORMAT.format('16G_run'),
            'contents': '#!/bin/bash\n'
                        'cd /home/enomix/bin\n'
                        'cp ecc_16G.sh ecc.sh\n'
                        './all_run.sh\n'
                        'cd /home/enomix/apps/solr\n'
                        './run.sh > /dev/null\n'
                        'cd /home/enomix/apps/bin\n'
                        './dummy_chatbot_run.sh > /dev/null\n'
        },
        {
            'name': SHELL_FILE_FORMAT.format('scouter'),
            'contents': '#!/bin/bash\n'
                        'cd /home/enomix/scouter/agent.host\n'
                        './host.sh\n'
        },
    ]

    def __init__(self):
        tempDir = ['/bin']
        # create temp directory
        for dir in tempDir:
            path = FlarePath.FLARE_TEMP + dir
            if not os.path.exists(path):
                os.makedirs(path)

    def create(self):
        for shell in self.SHELL_INFO:
            fileName = shell['name']
            fileContents = shell['contents']

            target = os.path.join(self.SHELL_PATH[0], fileName)
            temp = os.path.join(self.SHELL_PATH[1], fileName)

            self.makeFile(target, temp, fileContents)

    def makeFile(self, target, temp, fileContents):
        tempFile = open(temp, 'w', encoding='UTF8')
        tempFile.write(fileContents)
        tempFile.close()

        os.chmod(temp, 0o755)
        shutil.copy(temp, target)
