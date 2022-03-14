import random
import sqlite3

def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_connection()
c = conn.cursor()

result = c.execute('SELECT * FROM "reasoning"')
questions = result.fetchall()

class Reasoning():
    def __init__(self, id, statement, query, answer1, answer2):
        self.id = id
        self.statement = statement
        self.query = query
        self.answer1 = answer1
        self.answer2 = answer2

    def __str__(self):
        return "Twierdzenie: {}, Pytanie: {}, Poprawna odp. to:{}, błędna to: {}".format(self.statement, self.query, self.answer1, self.answer2)

    @staticmethod
    def select_random():
        return random.choice(questions)


