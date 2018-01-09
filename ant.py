import os
import sys
import subprocess
from props import Config, Command
import message

class Ant():
    def __init__(self):
        config = Config().getConfig()



def main():
    args = sys.argv[1:]

    ant = Ant()
    if args[0] == 'build':
        del args[0]


if __name__ == '__main__':
    main()