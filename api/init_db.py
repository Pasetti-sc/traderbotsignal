import os
import mysql.connector


def create_database():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '')
    )
    cursor = connection.cursor()
    db_name = os.getenv('DB_NAME', 'traderbot')
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.close()
    connection.close()


def create_users_table():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'traderbot')
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


def force_password_reset_for_legacy_hashes():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'traderbot')
    )
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET password='' WHERE password NOT LIKE '$2b$%'"
    )
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    create_database()
    create_users_table()
    force_password_reset_for_legacy_hashes()
    print('Database and users table created')
