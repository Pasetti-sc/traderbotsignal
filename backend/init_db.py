import mysql.connector
from config import DB_CONFIG
db = mysql.connector.connect(
    host=DB_CONFIG["host"], user=DB_CONFIG["user"], password=DB_CONFIG["password"]
)
cur = db.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
cur.execute(f"USE {DB_CONFIG['database']}")
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
      email VARCHAR(255) PRIMARY KEY,
      password CHAR(32) NOT NULL,
      iq_email VARCHAR(255) NOT NULL,
      iq_password VARCHAR(255) NOT NULL
    )
    """
      password VARCHAR(32),
      iq_email VARCHAR(255),
      iq_password VARCHAR(255)
    )
    """
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
    'password VARCHAR(32)'
    ')'
)
cur.close()
db.close()