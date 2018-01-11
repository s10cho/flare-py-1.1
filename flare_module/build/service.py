from flare_module.build.command.svn import Svn
from flare_module.build.command.maven import Maven


def build():
    buildService = BuildService()
    buildService.run()


class BuildService(object):
    def __init__(self):
        self.svn = Svn()
        self.maven = Maven()

    def run(self):
        self.svn.checkout()
        self.maven.clean_install()



