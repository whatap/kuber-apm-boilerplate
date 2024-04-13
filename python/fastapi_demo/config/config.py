# -*- coding: utf-8 -*-
from src.utils import get_project_dir
from configparser import ConfigParser

project_dir = get_project_dir()
config = ConfigParser()
config.read(filenames=f'{project_dir}/config/config.ini')

class MysqlConfig():
    def __init__(self):
        section = 'Mysql'
        self.host = config.get(section=section, option='host')
        self.port = config.getint(section=section, option='port')
        self.user = config.get(section=section, option='user')
        #self.user_wrong = config.get(section=section, option='user_wrong')
        self.password = config.get(section=section, option='password')
        self.charset = config.get(section=section, option='charset')
        self.database = config.get(section=section, option='database')

if __name__ == "__main__":
    mysql = MysqlConfig()
    print(f"project_dir={project_dir}")
    print(f"mysql.host={mysql.host}")
