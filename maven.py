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
        command = 'mvn clean install'
        subprocess.call(command, shell=True)

        message.msg_print('mvn clean install complete !!!')


if __name__ == '__main__':
    maven = Maven()
    maven.clean_install()
