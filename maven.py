import os
import sys
import subprocess
from config import Config
import message

class Maven():
    def __init__(self):
        config = Config()
        self.maven = [
            config.get('SVN', 'DIR')
        ]

    def clean_install(self):
        os.chdir(self.maven[0])

        command = 'mvn clean install'
        subprocess.call(command, shell=True)

        message.msg_print('mvn clean install complete !!!')


def main():
    args = sys.argv[1:]

    maven = Maven()
    if args[0] == 'bulid':
        maven.clean_install()
        del args[0]

if __name__ == '__main__':
    main()