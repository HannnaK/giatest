import sqlite3

conn = sqlite3.connect('base.db')
c = conn.cursor()


def run_script_sql(script):
    with open(script) as f:
        query = f.read()
    c.executescript(query)


run_script_sql('migrations\\1_reasoning.sql')
run_script_sql('migrations\\2_compare_items.sql')
run_script_sql('migrations\\users.sql')
run_script_sql('migrations\\answers_reasoning.sql')
run_script_sql('migrations\\answers_compare_items.sql')

conn.commit()

conn.close()
