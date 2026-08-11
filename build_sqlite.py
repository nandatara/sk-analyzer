import sqlite3
import json
import os

DB_FILE = 'sanskrit_engine.db'
JSON_FILE = 'gita_data.json'

def build_database():
    if not os.path.exists(JSON_FILE):
        print(f"⚠️ Error: {JSON_FILE} not found.")
        return

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # --- 1. Update Verses Table ---
    cursor.execute('DROP TABLE IF EXISTS gita_verses')
    cursor.execute('''
        CREATE TABLE gita_verses (
            id TEXT PRIMARY KEY,
            chapter INTEGER,
            verse INTEGER,
            text_sa TEXT,
            text_iast TEXT,
            pada_sa TEXT,
            pada_iast TEXT,
            anvaya_sa TEXT,
            anvaya_iast TEXT,
            analysis TEXT
        )
    ''')

    verse_rows = []
    for v_id, v_data in data.get("verses", {}).items():
        parts = v_id.split(':')
        if len(parts) == 2:
            ch, vs = int(parts[0]), int(parts[1])
            
            # 🛡️ Bulletproof check: Look for direct keys first, fallback to nested "text" object
            text_sa_array = v_data.get("text_sa")
            if not text_sa_array:
                text_sa_array = v_data.get("text", {}).get("sa", [])
                
            text_iast_array = v_data.get("text_iast")
            if not text_iast_array:
                text_iast_array = v_data.get("text", {}).get("iast", [])
            
            verse_rows.append((
                v_id, ch, vs,
                json.dumps(text_sa_array, ensure_ascii=False),
                json.dumps(text_iast_array, ensure_ascii=False),
                v_data.get("pada_sa", ""),
                v_data.get("pada_iast", ""),
                v_data.get("anvaya_sa", ""),
                v_data.get("anvaya_iast", ""),
                json.dumps(v_data.get("analysis", {}), ensure_ascii=False)
            ))

    if verse_rows:
        cursor.executemany('INSERT INTO gita_verses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', verse_rows)
        print(f"✅ Inserted {len(verse_rows):,} verses.")

    # --- 2. Rebuild Dictionaries ---
    dicts = data.get("dictionaries", {})
    
    # English Glossary
    cursor.execute('DROP TABLE IF EXISTS glossary_en')
    cursor.execute('CREATE TABLE glossary_en (word TEXT PRIMARY KEY, meaning TEXT)')
    en_rows = [(k, v) for k, v in dicts.get("en", {}).items()]
    if en_rows: cursor.executemany('INSERT INTO glossary_en VALUES (?, ?)', en_rows)

    # Hindi Glossary
    cursor.execute('DROP TABLE IF EXISTS glossary_hi')
    cursor.execute('CREATE TABLE glossary_hi (word TEXT PRIMARY KEY, meaning TEXT)')
    hi_rows = [(k, v) for k, v in dicts.get("hi", {}).items()]
    if hi_rows: cursor.executemany('INSERT INTO glossary_hi VALUES (?, ?)', hi_rows)

    # Philosophical Glossary
    cursor.execute('DROP TABLE IF EXISTS glossary_philo')
    cursor.execute('CREATE TABLE glossary_philo (word TEXT PRIMARY KEY, meaning TEXT)')
    philo_rows = [(k, v) for k, v in dicts.get("philosophical", {}).items()]
    if philo_rows: cursor.executemany('INSERT INTO glossary_philo VALUES (?, ?)', philo_rows)

    print(f"✅ Inserted {len(en_rows):,} English, {len(hi_rows):,} Hindi, and {len(philo_rows):,} Philosophical terms.")

    conn.commit()
    conn.close()
    print("🎉 Database successfully updated!")

if __name__ == '__main__':
    build_database()