import os
import hashlib
from flask import Flask, render_template, request, redirect, url_for, session, send_file
import mysql.connector
from api.iqconnect import connect_iq
from config import DB_CONFIG

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'frontend'),
    static_folder=os.path.join(BASE_DIR, 'css'),
)
app.secret_key = 'secret_key'


def get_db():
    return mysql.connector.connect(**DB_CONFIG)


@app.route('/')
def index():
    return send_file(os.path.join(BASE_DIR, 'index.html'))


@app.route('/register', methods=['GET', 'POST'])
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()
        iq_email = request.form['iq_email']
        iq_password = request.form['iq_password']
        db = get_db()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO users (email, password, iq_email, iq_password) VALUES (%s, %s, %s, %s)',
            (email, password, iq_email, iq_password),
        )
        db.commit()
        cur.close()
        db.close()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        raw_password = request.form['password']
        password = hashlib.md5(raw_password.encode()).hexdigest()
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT password, iq_email, iq_password FROM users WHERE email=%s', (email,))
        result = cur.fetchone()
        cur.close()
        db.close()
        if result and result[0] == password:
            session['user'] = email
            iq_email = result[1]
            iq_password = result[2]
            iq = connect_iq(iq_email, iq_password)
            if iq:
                return redirect(url_for('panel'))
            return 'Falha na conexão com IQ Option', 401
        return 'Credenciais inválidas', 401
    return render_template('login.html')


@app.route('/panel')
@app.route('/panel.html')
def panel():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('panel.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
