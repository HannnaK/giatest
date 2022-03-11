import random
import sqlite3
from datetime import datetime, timedelta

def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_connection()
c = conn.cursor()

result = c.execute('SELECT * FROM "reasoning"')
questions = result.fetchall()

class GiaTest:
    def __init__(self):
        self.time_start = datetime.now()
        self.time_end = self.time_start + timedelta(0, 15)
        self.counter = 0


class Reasoning(GiaTest):
    def __init__(self, id, statement, query, answer1, answer2):
        super().__init__()
        self.id = id
        self.statement = statement
        self.query = query
        self.answer1 = answer1
        self.answer2 = answer2

    def __str__(self):
        return "Twierdzenie: {}, Pytanie: {}, Poprawna odp. to:{}".format(self.statement, self.query, self.answer1)

    def wrong_answer(self, answer):
        pass

    @staticmethod
    def select_random():
        return random.choice(questions)


# gia_test_reasoning = GiaTest()
#
# while datetime.now() <= gia_test_reasoning.time_end:
#     gia_test_reasoning.counter += 1
#     question_selected = Reasoning.select_random()
#     question = Reasoning(question_selected[0], question_selected[1], question_selected[2], question_selected[3], question_selected[4])
#     question.select_answer()
#
# for f in gia_test_reasoning.wrong_answer:
#     print(f)
# print('liczba odp: ', gia_test_reasoning.counter)
#
# print('liczba prawidłowych odp: ', gia_test_reasoning.counter-len(gia_test_reasoning.wrong_answer))
