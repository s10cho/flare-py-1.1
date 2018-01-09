import sys
import subprocess
from props import Config, Command
import message

class Svn():
    def __init__(self):
        config = Config().getConfig()
        self.svn = [
            config['SVN']['ID'],
            config['SVN']['PASSWORD'],
            config['SVN']['URL'],
            config['DIR']['WORKSPACE']
        ]

    def checkout(self):
        command = Command.SVN_CHECKOUT.format(self.svn[0], self.svn[1], self.svn[2], self.svn[3])
        subprocess.call(command, shell=True)
        message.msg_print('svn checkout complete !!!')


def main():
    args = sys.argv[1:]

    svn = Svn()
    if args[0] == 'checkout':
        svn.checkout()
        del args[0]

if __name__ == '__main__':
    main()
