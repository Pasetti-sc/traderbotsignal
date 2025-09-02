import os
import hashlib

import bcrypt
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

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

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, password FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        stored = user["password"]
        password_bytes = password.encode("utf-8")

        if stored.startswith("$2b$"):
            if bcrypt.checkpw(password_bytes, stored.encode("utf-8")):
                cursor.close()
                conn.close()
                return jsonify({"message": "login successful"})
        else:
            legacy_hash = hashlib.md5(password_bytes).hexdigest()
            if legacy_hash == stored:
                new_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")
                cursor.execute(
                    "UPDATE users SET password=%s WHERE id=%s",
                    (new_hash, user["id"]),
                )
                conn.commit()
                cursor.close()
                conn.close()
                return jsonify({"message": "login successful"})

    cursor.close()
    conn.close()
    return jsonify({"error": "invalid credentials"}), 401


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'missing data'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hashed),
        )
        conn.commit()
    except Error as exc:
        conn.rollback()
        cursor.close()
        conn.close()
        return jsonify({"error": str(exc)}), 400

    cursor.close()
    conn.close()
    return jsonify({'message': 'user created'}), 201


if __name__ == '__main__':
    app.run(debug=True)
