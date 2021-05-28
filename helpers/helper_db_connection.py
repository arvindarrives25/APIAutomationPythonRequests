import mysql.connector
from mysql.connector import Error
from utilities.configurations import get_config

"""This Helper class contains all the DB related methods"""


class DBConnectionHelper:

    """This generic method contains all the parameters for database connection for example,
    host, database name, user name and password"""
    @staticmethod
    def db_connection_string():

        db_connection = {'host': get_config()['DB']['host'],
                         'database': get_config()['DB']['database'],
                         'user': get_config()['DB']['user'],
                         'password': get_config()['DB']['password'],
                         }
        return db_connection

    """This generic method actually calls connection string and connects to database"""
    @staticmethod
    def helper_get_db_connection():
        try:
            conn = mysql.connector.connect(**DBConnectionHelper.db_connection_string())
            if conn.is_connected():
                print("Connection Successful")
                return conn
        except Error as e:
            print(e)

    """This generic method calls db connection method executes the given db query
     and returns rows of a specific table"""
    @staticmethod
    def helper_get_db_query(query):
        conn = DBConnectionHelper.helper_get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        conn.close()
        return row

    """This generic method takes a tupple from user as key, takes db table output as second table 
    and finally creates a dictionary which can be used as payload in further API uses"""
    @staticmethod
    def get_dynamic_payload(query, tups, index):
        tup2 = DBConnectionHelper.helper_get_db_query(query)[index]
        dict1 = dict(zip(tups, tup2))
        return dict1

#For debug purpose only
# x = DBConnectionHelper.get_dynamic_payload('select * from program', tup1, 0)
# print(x)
