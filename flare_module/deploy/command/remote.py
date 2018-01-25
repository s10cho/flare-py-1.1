from fabric.api import *
from config import FlareEnv


def SetServer(hostname):
    def wrapper(func):
        def decorator(*args, **kwargs):
            remoteInfo = FlareEnv.SERVER[hostname]
            env.hosts = remoteInfo["HOSTS"]
            env.user = remoteInfo["USER"]
            env.password = remoteInfo["PASSWORD"]
            for host in env.hosts:
                with settings(host_string=host):
                    func(*args, **kwargs)
        return decorator
    return wrapper


class EERServer():
    def __init__(self):
        pass

    @SetServer("EER")
    def execute(self, command):
        run(command)


class GatlingServer():
    def __init__(self):
        pass

    @SetServer("GATLING")
    def execute(self, command):
        run(command)
