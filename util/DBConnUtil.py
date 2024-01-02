from util import DBPropertyUtil as DB
import mysql.connector as sql
class DBConnUtil:
    def open(self):
        connstring=DB.DBPropertyUtil.getConnString()
        self.conn=sql.connect(user=connstring[1],host=connstring[0],password=connstring[2],database=connstring[3])
        if self.conn.is_connected():
            self.stmt=self.conn.cursor()
            print("Datebase Connected")
    def close(self):
        self.conn.close()




