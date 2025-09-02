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
      password VARCHAR(32),
      iq_email VARCHAR(255),
      iq_password VARCHAR(255)
    )
    """
)
cur.close()
db.close()
