import pymysql
import json

class BaseDao:
    '''
    数据库访问基本类
    '''
    def __init__(self,config = "mysql.json"):
        self.__config = json.load(open(config, mode='r', encoding='utf-8'))
        self.__conn = None
        self.__cursor =  None
        ...

    def getConnection(self):
        if self.__conn != None:
            return self.__conn
        self.__conn =pymysql.connect(**self.__config)
        return self.__conn

    def execute(self, sql, params=[],  ret="dict"):
        result = None
        try:
            self.__conn = self.getConnection()
            if ret == "dict":
                self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)
                ...
            else:
                self.__cursor = self.__conn.cursor()
                ...
            result = self.__cursor.execute(sql,params)
        except pymysql.DatabaseError as e:
            print(e)
            ...
        return result

    def fetchOne(self):
        if self.__cursor:
            return self.__cursor.fetchone()
        ...

    def fetchAll(self):
        if self.__cursor:
            return self.__cursor.fetchall()
        ...

    def close(self):
        if self.__cursor:
            self.__cursor.close()
            ...
        if self.__conn:
            self.__conn.close()
            ...
        ...

    def commit(self):
        if self.__conn:
            self.__conn.commit()
            ...
        ...

    def rollback(self):
        if self.__conn:
            self.__conn.rollback()
            ...
        ...

    ...
