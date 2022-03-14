import sqlite3
import random
from flask import Flask, get_flashed_messages, flash, session, render_template, request, redirect
from datetime import datetime, timedelta
from giaTestClass import Reasoning
from werkzeug.security import check_password_hash



app = Flask(__name__)
app.secret_key = 'secret-key-1103'

def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        c = conn.cursor()

        result = c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = result.fetchone()

        if user_data:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data['id']
                session['username'] = user_data['username']

                return render_template('welcome.html', session=session) and redirect('/')

        flash('błędna nazwa użytkownika lub hasło')
        return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
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
    return render_template('welcome.html')

questions_selected_list = []
wrong_answers_list = []
good_answers_list = []



@app.route('/reasoning/', methods=['GET', 'POST'], endpoint='reasoning')
@login_required
def reasoning():

        if request.method == 'GET':
            question_selected = Reasoning.select_random()
            question = Reasoning(question_selected[0], question_selected[1], question_selected[2], question_selected[3],
                                 question_selected[4])
            questions_selected_list.append(question)
            answer1, answer2= random.sample([question.answer1, question.answer2], 2)
            return render_template('reasoning.html', question=question, answer1=answer1, answer2=answer2)

        if request.method == 'POST':
            answer = request.form.get("answer")
            if answer == questions_selected_list[-1].answer2:
                wrong_answers_list.append(questions_selected_list[-1])
            else:
                good_answers_list.append(questions_selected_list[-1])
            for g in wrong_answers_list:
                print('g', g, 'złą odp', g.answer2)
            return redirect('/reasoning/')



@app.route('/compare_items', endpoint='compare_items')
@login_required
def compare_items():
    return render_template('compare_items.html')

@app.route('/results', endpoint='results')
@login_required
def results():
    number_of_questions = len(questions_selected_list)
    number_of_answers = len(wrong_answers_list)+len(good_answers_list)
    wrong_answers = wrong_answers_list

    return render_template('results.html', number_of_questions=number_of_questions, wrong_answers=wrong_answers, number_of_answers=number_of_answers)


if __name__ == '__main__':
    app.run(debug=True)
