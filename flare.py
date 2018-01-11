import os
import sys
from flare_module.build.service import BuildService

FLARE_HOME = os.path.dirname(os.path.abspath(__file__))

def getFlareRootPath():
    return FLARE_HOME

def main():
    args = sys.argv[1:]

    if args[0] == 'build':
        buildService = BuildService()
        buildService.run()
        del args[0]

if __name__ == '__main__':
    main()