import json
import os
import root

config_path = os.path.join(root.ROOT_PATH, 'conf/config.json')
print(root.ROOT_PATH)
with open(config_path, 'r') as f:
    Config = json.load(f)

class FlarePath:

    FLARE_ROOT = root.ROOT_PATH

    WORKSPACE = os.path.join(FLARE_ROOT, Config['DIR']['WORKSPACE'])


class FlareEnv(FlarePath):
    svn = [
        Config['SVN']['ID'],
        Config['SVN']['PASSWORD'],
        Config['SVN']['URL'],
        FlarePath.WORKSPACE
    ]