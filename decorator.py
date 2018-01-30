import getpass
import subprocess
from fabric.api import env, settings

def before(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

def remote(server):
    def wrapper(func):
        def decorator(*args, **kwargs):
            env.hosts = server["HOSTS"]
            env.user = server["USER"]
            env.password = server["PASSWORD"]
            for host in env.hosts:
                with settings(host_string=host):
                    func(*args, **kwargs)
        return decorator
    return wrapper

def chown_path(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            whoami = getpass.getuser()
            command = 'sudo chown -R {0}:{0} {1}'.format(whoami, path)
            subprocess.call(command, shell=True)
            func(*args, **kwargs)
        return wrapper
    return decorator
