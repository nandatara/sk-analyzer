import sqlite3
conn = sqlite3.connect('sanskrit_engine.db')
print(conn.cursor().execute("SELECT * FROM vidyut_verbs WHERE word_slp1='Bavati'").fetchone())