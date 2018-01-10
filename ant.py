import os
import sys
import subprocess
import shutil
from props import Config, Command, Template
import message

class Ant():
    def __init__(self):
        config = Config().getConfig()

        self.setup_file = [
            config['DIR']['SETUP']['TEMP_PATH'],
            config['DIR']['SETUP']['COPY_PATH']
        ]

    def ant_init(self):
        self.before_copy()
        self.setup_convert()
        self.setup_copy()

    def before_copy(self):
        shutil.copy(self.setup_file[1], './template')

    def setup_convert(self):
        setup = Template().get_template(Template.SETUP)
        setup = setup.replace('install.mode=part1', 'install.mode=part2')

        with open(self.setup_file[0], 'w') as f:
            f.write(setup)

    def setup_copy(self):
        shutil.copy(self.setup_file[0], self.setup_file[1])

    def ant_build(self):
        os.chdir(self.maven[0])


def main():
    args = sys.argv[1:]

    ant = Ant()
    ant.ant_init()

    # if args[0] == 'build':
    #     del args[0]


if __name__ == '__main__':
    main()