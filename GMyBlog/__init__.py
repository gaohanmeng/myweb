import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect('localhost', 'root', '1338.332', 'MYBLOG_DB')
cursor = db.cursor()
cursor.execute('SELECT DATABASE();')
data = cursor.fetchall()
db.close()
