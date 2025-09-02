import os
import hashlib
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from iqoptionapi.stable_api import IQ_Option

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'traderbot')
    )


@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    if not email or not password:
        return jsonify({'error': 'missing credentials'}), 400

    hashed_password = hashlib.md5(password.encode()).hexdigest()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id FROM users WHERE email=%s AND password=%s",
        (email, hashed_password)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        iq_client = IQ_Option(email, password)
        try:
            iq_client.connect()
            if iq_client.check_connect():
                return jsonify({'message': 'login successful'})
            return jsonify({'error': 'iq option connection failed'}), 502
        except Exception as exc:
            return jsonify({'error': str(exc)}), 502

    return jsonify({'error': 'invalid credentials'}), 401


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'missing data'}), 400

    hashed_password = hashlib.md5(password.encode()).hexdigest()

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hashed_password)
        )
        conn.commit()
    except Error as exc:
        conn.rollback()
        cursor.close()
        conn.close()
        return jsonify({'error': str(exc)}), 400

    cursor.close()
    conn.close()
    return jsonify({'message': 'user created'}), 201


if __name__ == '__main__':
    app.run(debug=True)
