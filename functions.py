import sqlite3
from flask import session, redirect


def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn


def results_compare_items():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    quiry = """
        SELECT ci.id, ci.letter1, ci.letter2,  ci.letter3, ci.letter4, ci.letter5, ci.letter6,  ci.letter7, ci.letter8, ci.correct_answer, aci.my_answer, aci.tests_number FROM "compare_items" AS ci
        LEFT JOIN "answers_compare_items" AS aci 
        ON ci.id=aci.id_compare_items
        LEFT JOIN "users" AS u
        ON aci.id_user=u.id
        WHERE aci.id_user=?
        """
    id_user = int(session['user_id'])
    c.execute(quiry, (id_user,))

    answers_compare_items = []
    for item in c:
        answers_compare_items.append(item)
    conn.close()
    return answers_compare_items


def results_reasoning():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    quiry = """
    SELECT r.statement, r.query,  r.correct_answer, ar.my_answer, ar.tests_number FROM "reasoning" AS r
    LEFT JOIN "answers_reasoning" AS ar
    ON r.id=ar.id_reasoning
    LEFT JOIN "users" AS u
    ON ar.id_user=u.id
    WHERE ar.id_user=?
    """
    id_user = int(session['user_id'])
    c.execute(quiry, (id_user,))

    answers_reasoning = []
    for questions in c:
        answers_reasoning.append(questions)
    conn.close()
    return answers_reasoning


def results_reasoning_pdf():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    quiry = """
    SELECT ar.tests_number, r.statement, r.query,  r.correct_answer, ar.my_answer FROM "reasoning" AS r
    LEFT JOIN "answers_reasoning" AS ar
    ON r.id=ar.id_reasoning
    LEFT JOIN "users" AS u
    ON ar.id_user=u.id
    WHERE ar.id_user=?
    """
    id_user = int(session['user_id'])
    c.execute(quiry, (id_user,))

    answers_reasoning = []
    for questions in c:
        answers_reasoning.append(questions)
    conn.close()

    return answers_reasoning


def results_compare_items_pdf():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    quiry = """
                SELECT aci.tests_number, ci.letter1, ci.letter2, ci.letter3, ci.letter4, ci.letter5, ci.letter6,  ci.letter7, ci.letter8, ci.correct_answer, aci.my_answer FROM "compare_items" AS ci
                LEFT JOIN "answers_compare_items" AS aci 
                ON ci.id=aci.id_compare_items
                LEFT JOIN "users" AS u
                ON aci.id_user=u.id
                WHERE aci.id_user=?
                """
    id_user = int(session['user_id'])
    c.execute(quiry, (id_user,))

    answers_compare_items = []
    for item in c:
        answers_compare_item = []
        row = ''.join(str(el) for el in item)
        answers_compare_item.append(row[0])
        answers_compare_item.append(row[1:5])
        answers_compare_item.append(row[5:9])
        answers_compare_item.append(row[9])
        answers_compare_item.append(row[10])
        answers_compare_items.append(answers_compare_item)
    conn.close()

    return answers_compare_items


def login_required(view):
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect('/login')

    return wrapped_view
