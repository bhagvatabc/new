import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "2017",
                           db = "test")
    c = conn.cursor()

    return c, conn