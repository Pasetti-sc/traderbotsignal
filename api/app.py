import os
import hashlib
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

try:
    from iqoptionapi.stable_api import IQ_Option
except Exception:  # pragma: no cover - library may not be installed
    IQ_Option = None

app = Flask(__name__, template_folder='templates', static_folder='static')


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'traderbot'),
    )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return render_template('register.html', error='Missing data')
        hashed = hashlib.md5(password.encode()).hexdigest()
        conn = get_db_connection()
        cursor = conn.cursor()
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
            return render_template('register.html', error=str(exc))
        cursor.close()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return render_template('login.html', error='Missing credentials')
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, password FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user and user['password'] == hashlib.md5(password.encode()).hexdigest():
            if IQ_Option is not None:
                iq = IQ_Option(email, password)
                try:
                    iq.connect()
                    if iq.check_connect():
                        return render_template('panel.html', message='Connected to IQ Option')
                    return render_template('panel.html', message='Failed to connect to IQ Option')
                except Exception as exc:  # pragma: no cover - runtime error
                    return render_template('panel.html', message=f'Error: {exc}')
            return render_template('panel.html', message='IQ Option library not available')
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
