from flare_module.build.command.svn import Svn
from flare_module.build.command.maven import Maven
from flare_module.build.command.setup import Setup
from flare_module.build.command.docker import Docker
from flare_module.build.command.logback import Logback
from flare_module.build.command.shell import Shell
from flare_module.build.command.scouter import Scouter
from config import FlarePath, FlareProcess
import decorator

class BuildService():

    @decorator.chown_path(FlarePath.ORACLE_HOME)
    def __init__(self):
        self.svn = Svn()
        self.maven = Maven()
        self.setup = Setup()
        self.docker = Docker()
        self.logback = Logback()
        self.shell = Shell()
        self.scouter = Scouter()

    def run(self, param):

        if FlareProcess.BUILD == 'Y':
            if len(param) == 0:
                self.docker.rm()
                self.svn.checkout()
                self.maven.clean_install()
                self.setup.settings()
                self.logback.change_log_level()
                self.shell.create()
                self.scouter.agent_set()
                self.maven.database_clean()
                self.docker.all_run()
            else:
                # command run
                command = param[0]
                print(command)
                if command == 'svn':
                    self.docker.rm()
                    self.svn.checkout()
                elif command == 'maven':
                    self.maven.clean_install()
                elif command == 'setup':
                    self.setup.settings()
                    self.logback.change_log_level()
                    self.shell.create()
                    self.scouter.agent_set()
                elif command == 'clean':
                    self.maven.database_clean()
                elif command == 'run':
                    self.docker.all_run()





