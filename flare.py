import sys
from service.build.execute import Build

def main():
    args = sys.argv[1:]

    if args[0] == 'build':
        build = Build()
        build.execute()
        del args[0]

if __name__ == '__main__':
    main()