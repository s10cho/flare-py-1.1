import os
import sys
from flare_module.build.service import build

FLARE_HOME = os.path.dirname(os.path.abspath(__file__))

def main():
    args = sys.argv[1:]

    if args[0] == 'build':
        build()
        del args[0]

if __name__ == '__main__':
    main()