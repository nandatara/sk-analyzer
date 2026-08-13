import sqlite3
import json
import os

DB_FILE = 'sanskrit_engine.db'
FULL_JSON = 'derivations.json' 

def build_full_vidyut_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("🚀 Initializing full Vidyut database build...")
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
    
    if os.path.exists(FULL_JSON):
        print(f"📂 Loading {FULL_JSON} into memory (this may take a moment)...")
        with open(FULL_JSON, 'r', encoding='utf-8') as f:
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
        
        print(f"⏳ Injecting {len(rows_to_insert):,} verbal forms into SQLite...")
        cursor.executemany('INSERT INTO vidyut_verbs VALUES (?, ?, ?, ?, ?, ?, ?)', rows_to_insert)
        
        print("🗂️ Building high-speed index for instantaneous UI lookups...")
        cursor.execute('CREATE INDEX idx_word_slp1 ON vidyut_verbs(word_slp1)')
        
        conn.commit()
        print("✅ Full Vidyut database successfully integrated!")
    else:
        print(f"⚠️ {FULL_JSON} not found! Please ensure it is in the active directory.")

    conn.close()

if __name__ == '__main__':
    build_full_vidyut_table()