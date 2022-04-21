from flask import Blueprint, request, get_flashed_messages, render_template, \
    session, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash

from functions import get_connection

auth_bp = Blueprint('auth_endpoints', __name__)


@auth_bp.route('/registration', methods=['GET', 'POST'], endpoint='registration')
def registration():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('registration.html', messages=messages)
    if request.method == 'POST':
        username = request.form['username']
        email_address = request.form['email_address']
        password = generate_password_hash(request.form['password'])

        conn = get_connection()
        c1 = conn.cursor()
        result = c1.execute('SELECT * FROM users WHERE email_address = ?', (email_address,))
        user_data = result.fetchone()

        if user_data == None:
            c = conn.cursor()
            quiry = """
                            INSERT INTO "users" ("email_address", "username", "password") VALUES (?, ?, ?)
                            """
            parameters = (email_address, username, password)
            c.execute(quiry, parameters)
            conn.commit()
            conn.close()
            return redirect('/')

        flash('Podany użytkownik już istnieje, zaloguj się.')
        return redirect('/registration')


@auth_bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']

        conn = get_connection()
        c = conn.cursor()

        result = c.execute('SELECT * FROM users WHERE email_address = ?', (email_address,))
        user_data = result.fetchone()
        conn.close()
        if user_data:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data['id']
                session['email_address'] = user_data['email_address']
                session['username'] = user_data['username']

                return render_template('welcome.html', session=session) and redirect('/')

        flash('błędna nazwa użytkownika lub hasło')
        return redirect('/login')


@auth_bp.route('/logout', endpoint='logout')
def logout():
    session.clear()
    flash('Zostałeś wylogowany')
    return redirect('/login')
