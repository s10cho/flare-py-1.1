import os
import sys
import subprocess
from props import Config
from props import Command
import message

class Maven():
    def __init__(self):
        config = Config().getConfig()
        self.maven = [
            config['DIR']['WORKSPACE']
        ]

    def move_maven_root(self):
        os.chdir(self.maven[0])

    def clean_install(self):
        self.move_maven_root()

        subprocess.call(Command.MVN_CLEAN_INSTALL, shell=True)
        message.msg_print('mvn clean install complete !!!')

    def db_clean(self):
        self.move_maven_root()

        subprocess.call(Command.MVN_TEST_DB_CLEAN, shell=True)
        message.msg_print('mvn test db clean complete !!!')


def main():
    args = sys.argv[1:]

    maven = Maven()
    if args[0] == 'install':
        maven.clean_install()
        del args[0]

    if args[0] == 'dbclean':
        maven.db_clean()
        del args[0]

if __name__ == '__main__':
    main()