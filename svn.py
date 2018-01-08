import subprocess
from config import Config
import message

class Svn():
    def __init__(self):
        config = Config()
        self.svn = [
            config.get('SVN', 'ID'),
            config.get('SVN', 'PASSWORD'),
            config.get('SVN', 'URL'),
            config.get('SVN', 'DIR')
        ]

    def checkout(self):
        command = 'svn checkout --username {0} --password {1} {2} {3}'.format(self.svn[0], self.svn[1], self.svn[2], self.svn[3])
        subprocess.call(command, shell=True)

        message.msg_print('svn checkout complete !!!')


if __name__ == '__main__':
    svn = Svn()
    svn.checkout()
