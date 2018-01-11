import sys
from flare_module.build.service import BuildService

def main():
    args = sys.argv[1:]

    if args[0] == 'build':
        buildService = BuildService()
        buildService.run()
        del args[0]

if __name__ == '__main__':
    main()