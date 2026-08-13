import sqlite3
import json
import os

DB_FILE = 'sanskrit_engine.db'

def build_subanta_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("🚀 Initializing Vidyut subanta table...")
    cursor.execute('DROP TABLE IF EXISTS vidyut_subanta')
    cursor.execute('''
        CREATE TABLE vidyut_subanta (
            word_slp1 TEXT,
            stem TEXT,
            linga TEXT,
            vibhakti TEXT,
            vacana TEXT
        )
    ''')
    
    if os.path.exists('subanta_test.json'):
        with open('subanta_test.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        rows_to_insert = []
        for record in data:
            stem = record.get("stem")
            linga = record.get("linga")
            
            for form in record.get("forms", []):
                rows_to_insert.append((
                    form.get("final_string"),
                    stem,
                    linga,
                    form.get("vibhakti"),
                    form.get("vacana")
                ))
        
        cursor.executemany('INSERT INTO vidyut_subanta VALUES (?, ?, ?, ?, ?)', rows_to_insert)
        cursor.execute('CREATE INDEX idx_subanta_word ON vidyut_subanta(word_slp1)')
        
        conn.commit()
        print(f"✅ Successfully injected {len(rows_to_insert)} nominal forms into SQLite!")
    else:
        print("⚠️ subanta_test.json not found!")

    conn.close()

if __name__ == '__main__':
    build_subanta_table()