from flare_module.deploy.command.remote import EERServer, GatlingServer

class DeployService():
    def __init__(self):
        self.eer = EERServer()
        self.gatling = GatlingServer()

    def run(self, param):
        if len(param) == 0:
            self.eer.execute('uname -a')
            self.gatling.execute('uname -a')
        else:
            # command run
            command = param[0]
            print(command)



