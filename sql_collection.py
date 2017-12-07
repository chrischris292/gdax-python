import mysql.connector


class SqlCollection:
    def __init__(self):
    self.cnx = mysql.connector.connect(user='chris', password='tiger',
                                       host='127.0.0.1',
                                       database='employees')

    def insert_one(self, msg):

    def close(self):
        cnx.close()
