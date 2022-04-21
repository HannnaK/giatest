import sqlite3
import random
from flask import Blueprint, session, request, json
from functions import get_connection

api_gia_bp = Blueprint('api_gia', __name__)

conn = get_connection()
c = conn.cursor()
query1 = c.execute('SELECT * FROM "reasoning"')
data1 = query1.fetchall()


@api_gia_bp.route('/reasoning/questions', methods=['GET', 'POST'])
def reasoning_questions():
    data_sufle = random.shuffle(data1)
    data_dict = [dict(q) for q in data1]

    questions = dict({"reasoning": data_dict})
    return questions


@api_gia_bp.route('/reasoning/answers', methods=['POST'])
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


@api_gia_bp.route('/compare_items/questions', methods=['GET', 'POST'])
def compare_items_questions():
    data_sufle = random.shuffle(data2)
    data_dict = [dict(q) for q in data2]

    questions = dict({"compare_items": data_dict})
    return questions


@api_gia_bp.route('/compare_items/answers', methods=['POST'])
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
