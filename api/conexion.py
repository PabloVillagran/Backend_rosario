import mysql.connector as con
import os

HOST = os.getenv('MYSQL_HOST')
USER = os.getenv('MYSQL_USER')
PASS = os.getenv('MYSQL_PASS')
PORT = os.getenv('MYSQL_PORT')
if not HOST:
    HOST = "localhost"
    USER = "proyecto"
    PASS = "proyecto1234"
    PORT = "3306"
    print("configuraciones de SO no encontradas conectando a ", USER,":",PASS,"@",HOST,":",str(PORT),"/Proyecto")

con_string = USER+":"+PASS+"@"+HOST+":"+str(PORT)+"/Proyecto"

def db_test():
    with con.connect(host=HOST, user=USER, passwd=PASS, port=PORT) as db:
        with db.cursor() as cursor :
            cursor.execute('SELECT version()')
            s_r = ""
            for x in cursor:
                s_r = x[0]
            print(s_r)
            return s_r

def get_connection():
    return con.connect(host=HOST, user=USER, passwd=PASS, port=PORT)