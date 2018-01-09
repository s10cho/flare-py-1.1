import sys
import shutil
from props import Config

class DB():
    def __init__(self):
        config = Config().getConfig()
        self.db = [
            config['DIR']['TEMP']
        ]

        self.oracle = [
            config['ORACLE_DB']['DRIVER'],
            config['ORACLE_DB']['URL'],
            config['ORACLE_DB']['T']['USERNAME'],
            config['ORACLE_DB']['T']['PASSWORD'],
            config['ORACLE_DB']['T']['OWNERNAME'],
            config['ORACLE_DB']['VALIDATION']
        ]

        self.jdbc_file = [
            "./temp/engine.properties",
            "./workspace/home/conf/engine.properties.oracle"
        ]

    def database_init(self):
        self.jdbc_convert()
        self.jdbc_copy()

    def jdbc_convert(self):
        jdbc = [
            "db.driverClassName={0}\n",
            "db.url={0}\n",
            "db.username={0}\n",
            "db.password={0}\n",
            "db.ownername={0}\n",
            "db.validationQuery={0}\n",
        ]

        f = open(self.jdbc_file[0], 'w')
        for i in range(len(jdbc)):
            f.write(jdbc[i].format(self.oracle[i]))

        f.close()
        self.jdbc_copy()

    def jdbc_copy(self):
        shutil.copy(self.jdbc_file[0], self.jdbc_file[1])




def main():
    args = sys.argv[1:]

    db = DB()
    db.database_init()
    #
    # if args[0] == 'init':
    #     del args[0]


if __name__ == '__main__':
    main()