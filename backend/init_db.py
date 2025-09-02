import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='')
cur = db.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS traderbot')
cur.execute('USE traderbot')
cur.execute(
    'CREATE TABLE IF NOT EXISTS users ('
    'email VARCHAR(255) PRIMARY KEY,'
    'password VARCHAR(32),'
    'iq_email VARCHAR(255),'
    'iq_password VARCHAR(255)'
    ')'
)
cur.close()
db.close()
