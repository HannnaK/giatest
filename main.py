import sqlite3
import random
from flask import Flask, get_flashed_messages, flash, session, render_template, request, redirect, json, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'secret-key-1103'


def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/registration', methods=['GET', 'POST'])
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

@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/logout')
def logout():
    session.clear()
    flash('Zostałeś wylogowany')
    return redirect('/login')


def login_required(view):
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect('/login')

    return wrapped_view


@app.route('/')
def welcome():
    if session:

        user = session['username']
    else:
        user = None
    return render_template('welcome.html', user=user)


@app.route('/reasoning/', methods=['GET', 'POST'], endpoint='reasoning')
@login_required
def reasoning():
    return render_template('reasoning.html')


conn = get_connection()
c = conn.cursor()
query1 = c.execute('SELECT * FROM "reasoning"')
data1 = query1.fetchall()


@app.route('/reasoning/questions', methods=['GET', 'POST'])
def reasoning_questions():
    # data_sufle = random.shuffle(data1)
    data_dict = [dict(q) for q in data1]

    questions = dict({"reasoning": data_dict})
    return questions


@app.route('/reasoning/answers', methods=['POST'])
def reasoning_answers():
    output = request.get_json()
    result = json.loads(output)
    conn = sqlite3.connect('base.db')
    c = conn.cursor()

    query1 = '''
    SELECT MAX(tests_number) FROM "answers_reasoning" WHERE id_user=?;
    '''

    id_user = int(session['user_id'])
    c.execute(query1, (id_user,))

    number = c.fetchone()

    if number[0] == None:
        tests_number = 0
    else:
        tests_number = number[0]

    for i in result['qa']:
        quiry2 = """
                INSERT INTO "answers_reasoning" ("id_user", "tests_number", "id_reasoning", "my_answer") VALUES (?, ?, ?, ?)
                """
        parameters = (id_user, (tests_number + 1), i['id'], i['my_answer'])
        c.execute(quiry2, parameters)

    conn.commit()
    conn.close()

    return result


conn = get_connection()
c = conn.cursor()
query2 = c.execute('SELECT * FROM "compare_items"')
data2 = query2.fetchall()


@app.route('/compare_items', methods=['GET', 'POST'], endpoint='compare_items')
@login_required
def compare_items():
    return render_template('compare_items.html')


@app.route('/compare_items/questions', methods=['GET', 'POST'])
def compare_items_questions():
    # data_sufle = random.shuffle(data)
    data_dict = [dict(q) for q in data2]

    questions = dict({"compare_items": data_dict})
    return questions


@app.route('/compare_items/answers', methods=['POST'])
def compare_items_answers():
    output = request.get_json()
    result = json.loads(output)
    conn = sqlite3.connect('base.db')
    c = conn.cursor()

    query1 = '''
    SELECT MAX(tests_number) FROM "answers_compare_items" WHERE id_user=?;
    '''

    id_user = int(session['user_id'])
    c.execute(query1, (id_user,))

    number = c.fetchone()

    if number[0] == None:
        tests_number = 0
    else:
        tests_number = number[0]

    for i in result['qa']:
        quiry2 = """
                INSERT INTO "answers_compare_items" ("id_user", "tests_number", "id_compare_items", "my_answer") VALUES (?, ?, ?, ?)
                """
        parameters = (id_user, (tests_number + 1), i['id'], i['my_answer'])
        c.execute(quiry2, parameters)

    conn.commit()
    conn.close()

    return result


@app.route('/results', endpoint='results')
@login_required
def results():
    conn = sqlite3.connect('base.db')
    c1 = conn.cursor()
    quiry1 = """
    SELECT r.id, r.statement, r.query,  r.correct_answer, ar.my_answer, ar.tests_number FROM "reasoning" AS r
    LEFT JOIN "answers_reasoning" AS ar
    ON r.id=ar.id_reasoning
    LEFT JOIN "users" AS u
    ON ar.id_user=u.id
    WHERE ar.id_user=?
    """
    id_user = int(session['user_id'])
    c1.execute(quiry1, (id_user,))

    answers_reasoning = []
    for questions in c1:
        answers_reasoning.append(questions)

    c2 = conn.cursor()
    quiry2 = """
    SELECT ci.id, ci.letter1, ci.letter2,  ci.letter3, ci.letter4, ci.letter5, ci.letter6,  ci.letter7, ci.letter8, ci.correct_answer, aci.my_answer, aci.tests_number FROM "compare_items" AS ci
    LEFT JOIN "answers_compare_items" AS aci 
    ON ci.id=aci.id_compare_items
    LEFT JOIN "users" AS u
    ON aci.id_user=u.id
    WHERE aci.id_user=?
    """
    c2.execute(quiry2, (id_user,))

    answers_compare_items = []
    for item in c2:
        answers_compare_items.append(item)
    conn.close()

    return render_template('results.html', answers_reasoning=answers_reasoning,
                           answers_compare_items=answers_compare_items)


if __name__ == '__main__':
    app.run(debug=True)
