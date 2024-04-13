# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from config import config
import uuid

# Connect to the database
class WhatapMySql():
    def __init__(self, sql_config=None):

        self.sql_config = sql_config if sql_config is not None else config.MysqlConfig()
        self.conn = None
        self.curs = None
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.sql_config.host,
                                    port=self.sql_config.port,
                                    user=self.sql_config.user,
                                    password=self.sql_config.password,
                                    database=self.sql_config.database,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.conn.close()

    def create_table(self):
        sql = ''' CREATE TABLE user 
        (
        id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        email varchar(255),
        nickname varchar(255)
        )'''

        self.curs.execute(sql)
        self.conn.commit()

    def insert(self, email, nickname):
        # Create a new record
        # sql = "INSERT INTO `users` (`email`, `name`) VALUES (%s, %s)"
        sql = f"insert into user (email, nickname) values ('{email}','{nickname}')"
        self.curs.execute(sql)
        # curs.fetchall()
        # curs.execute(sql, ('jykim@whatap.io', 'jykim'))
        self.conn.commit()

    def select_wrong_all(self):
        sql = f"SELECT * FROM users"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        print("select all success")

    def select_all(self):
        sql = f"SELECT * FROM user"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        print("select all success")

    def select_one(self, email):
        sql = f"SELECT * FROM user WHERE email='{email}'"
        self.curs.execute(sql)
        result = self.curs.fetchone()
        print("select one success")

    def call_error_query(self):
        # try:
            sql = f"SELECT * FROM users"
            self.curs.execute(sql)
            result = self.curs.fetchone()
        # except Exception as e:
        #     print(f"error:{e}")

if __name__ == "__main__":
    sql = WhatapMySql()
    # sql.create_table()
    email = "ikorea@whatap.io"
    nickname = "fkorea"
    # s = uuid.uuid4()
    # print(s)
    # sql.insert(email=email,nickname=nickname)
    sql.select_one(email)
    # sql.select_all()
    # sql.close()