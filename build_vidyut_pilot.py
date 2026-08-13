import sqlite3
import json
import os

DB_FILE = 'sanskrit_engine.db'

def build_vidyut_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # 1. Create the Reverse-Lookup Table
    cursor.execute('DROP TABLE IF EXISTS vidyut_verbs')
    cursor.execute('''
        CREATE TABLE vidyut_verbs (
            word_slp1 TEXT,
            root TEXT,
            gana INTEGER,
            meaning TEXT,
            lakara TEXT,
            purusha TEXT,
            vacana TEXT
        )
    ''')
    
    # Create an index for lightning-fast word lookups
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_word_slp1 ON vidyut_verbs(word_slp1)')

    # 2. Parse and Flatten the JSON
    if os.path.exists('derivations_pilot.json'):
        with open('derivations_pilot.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        rows_to_insert = []
        for dhatu in data:
            root = dhatu.get("upadesha")
            gana = dhatu.get("gana")
            meaning = dhatu.get("meaning")
            
            for form in dhatu.get("forms", []):
                rows_to_insert.append((
                    form.get("final_string"),
                    root,
                    gana,
                    meaning,
                    form.get("lakara"),
                    form.get("purusha"),
                    form.get("vacana")
                ))
        
        # 3. Inject into SQLite
        cursor.executemany('INSERT INTO vidyut_verbs VALUES (?, ?, ?, ?, ?, ?, ?)', rows_to_insert)
        conn.commit()
        print(f"✅ Inserted {len(rows_to_insert)} verbal forms into the Vidyut lookup table.")
    else:
        print("⚠️ derivations_pilot.json not found!")

    conn.close()

if __name__ == '__main__':
    build_vidyut_table()