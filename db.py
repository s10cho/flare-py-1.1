import sys
import shutil
from config import Config

class DB():
    def __init__(self):
        config = Config()
        self.db = [
            config.get('DIR', 'TEMP')
        ]

        self.oracle = [
            config.get('T_ORACLE_DB', 'DRIVER'),
            config.get('T_ORACLE_DB', 'URL'),
            config.get('T_ORACLE_DB', 'USERNAME'),
            config.get('T_ORACLE_DB', 'PASSWORD'),
            config.get('T_ORACLE_DB', 'OWNERNAME'),
            config.get('T_ORACLE_DB', 'VALIDATION'),
        ]

        self.jdbc_file = [
            "./temp/engine.properties",
            "./workspace/home/conf/engine.properties",
            "./workspace/home/conf/engine.properties.oracle"
        ]

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
        shutil.copy(self.jdbc_file[0], self.jdbc_file[2])




def main():
    args = sys.argv[1:]

    db = DB()
    db.jdbc_convert()
    #
    # if args[0] == 'init':
    #     del args[0]


if __name__ == '__main__':
    main()