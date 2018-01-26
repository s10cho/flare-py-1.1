from fabric.api import *
from config import FlareEnv
from decorator import before, remote

@before(remote(FlareEnv.SERVER["GATLING"]))
class GatlingServer():
    def __init__(self): pass

    def execute(self, command):
        run(command)
