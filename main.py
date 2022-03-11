import sqlite3
import random
from flask import Flask, render_template, request, redirect, abort
from datetime import datetime, timedelta
from giaTestClass import Reasoning

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def welcome():
    return render_template('welcome.html')

questions_selected_list = []
wrong_answers_list = []
time_end = datetime.now() + timedelta(0, 10)

@app.route('/reasoning/', methods=['GET', 'POST'])
def reasoning():

    if datetime.now()<time_end:
        if request.method == 'GET':
            question_selected = Reasoning.select_random()
            question = Reasoning(question_selected[0], question_selected[1], question_selected[2], question_selected[3],
                                 question_selected[4])
            questions_selected_list.append(question)
            answer1, answer2= random.sample([question.answer1, question.answer2], 2)
            print('questionGET', question)
            return render_template('reasoning.html', question=question, answer1=answer1, answer2=answer2)

        if request.method == 'POST':
            answer = request.form.get("answer")
            if answer == questions_selected_list[-1].answer2:
                wrong_answers_list.append(questions_selected_list[-1])
            for g in wrong_answers_list:
                print('g', g, 'złą odp', g.answer2)
            return redirect('/reasoning/')

    return redirect('/')

@app.route('/compare_items')
def compare_items():
    return render_template('compare_items.html')

if __name__ == '__main__':
    app.run(debug=True)
