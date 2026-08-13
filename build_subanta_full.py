import sqlite3
import json
import os

DB_FILE = 'sanskrit_engine.db'
FULL_JSON = 'subanta_full.json'

def build_full_subanta_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("🚀 Initializing full Vidyut subanta database build...")
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
    
    if os.path.exists(FULL_JSON):
        print(f"📂 Loading {FULL_JSON} into memory...")
        with open(FULL_JSON, 'r', encoding='utf-8') as f:
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
        
        print(f"⏳ Injecting {len(rows_to_insert):,} nominal forms into SQLite...")
        cursor.executemany('INSERT INTO vidyut_subanta VALUES (?, ?, ?, ?, ?)', rows_to_insert)
        
        print("🗂️ Building high-speed index for instantaneous UI lookups...")
        cursor.execute('CREATE INDEX idx_subanta_word ON vidyut_subanta(word_slp1)')
        
        conn.commit()
        print("✅ Full Vidyut nominal database successfully integrated!")
    else:
        print(f"⚠️ {FULL_JSON} not found! Please move it to this directory.")

    conn.close()

if __name__ == '__main__':
    build_full_subanta_table()