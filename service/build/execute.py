import sys
from service.build.command.svn import Svn

class Build():
    def __init__(self):
        self.svn = Svn()

    def execute(self):
        self.svn.checkout()