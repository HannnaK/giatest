import random
import sqlite3


def get_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_connection()
c = conn.cursor()

reasoning = c.execute('SELECT * FROM "reasoning"')
questions = reasoning.fetchall()
# questions_jason = [dict(q) for q in questions]


class Reasoning():
    def __init__(self, id, statement, query, answer1, answer2):
        self.id = id
        self.statement = statement
        self.query = query
        self.answer1 = answer1
        self.answer2 = answer2

    def __str__(self):
        return "Twierdzenie: {}, Pytanie: {}, Poprawna odp. to:{}, błędna to: {}".format(self.statement, self.query,
                                                                                         self.answer1, self.answer2)

    def check_answer(self, given_answer):
        if given_answer == self.answer1:
            answer = 1
        else:
            answer = 0
        return answer

    @staticmethod
    def select_random():
        return random.choice(questions)

compare_items = c.execute('SELECT * FROM "compare_items"')
items = reasoning.fetchall()

class Compare_items():
    def __init__(self, id, letter1, letter2, letter3, letter4, letter5, letter6, letter7, letter8, correct_answer):
        self.id = id
        self.letter1 = letter1
        self.letter2 = letter2
        self.letter3 = letter3
        self.letter4 = letter4
        self.letter5 = letter5
        self.letter6 = letter6
        self.letter7 = letter7
        self.letter8 = letter8
        self.correct_answer = correct_answer

    def __str__(self):
        return "Litery {}, {}, {}, {}, {}, {}, {}, {}, poprawna odpowiedź: {}".format(self.letter1, self.letter2, self.letter3, self.letter4, self.letter5, self.letter6, self.letter7, self.letter8, self.correct_answer)

    @staticmethod
    def select_random():
        return random.choice(items)