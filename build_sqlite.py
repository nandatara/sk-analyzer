import json
import sqlite3
import os

def build_database():
    db_file = "sanskrit_engine.db"
    
    if os.path.exists(db_file):
        os.remove(db_file)
        
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    print("1. Creating SQLite tables...")
    
    # 1. Primary Engine
    cursor.execute('CREATE TABLE IF NOT EXISTS dictionary (word TEXT, pos TEXT, meaning TEXT)')
    
    # 2. Amarakośa
    cursor.execute('CREATE TABLE IF NOT EXISTS amarakosha (word TEXT PRIMARY KEY, artha TEXT, synonyms TEXT, linga TEXT)')
    
    # 3. Mini Aṣṭādhyāyī Glossary (Expanded Schema)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ashtadhyayi (
            word TEXT PRIMARY KEY,
            id TEXT,
            iast TEXT,
            slp1 TEXT,
            aliases TEXT,
            meaning TEXT,
            members TEXT
        )
    ''')
    
    # 4. Mini Aṣṭādhyāyī Sūtras (Expanded Schema)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sutras (
            id TEXT PRIMARY KEY, 
            slp1 TEXT, 
            slp1Display TEXT,
            type TEXT,
            typeDisplay TEXT,
            uddeshya TEXT, 
            vidheya TEXT, 
            meaning TEXT,
            explanation TEXT,
            anuvritti TEXT,
            adhikara TEXT,
            examples TEXT,
            related TEXT,
            glossary TEXT,
            notes TEXT,
            searchAliases TEXT
        )
    ''')
    
    print("2. Importing Primary Engine (analyzer_db.json)...")
    if os.path.exists("analyzer_db.json"):
        with open("analyzer_db.json", "r", encoding="utf-8") as f:
            primary_db = json.load(f)
        primary_rows = [(w, e.get("pos", ""), e.get("meaning", "")) for w, entries in primary_db.items() for e in entries]
        cursor.executemany('INSERT INTO dictionary VALUES (?, ?, ?)', primary_rows)
        print(f"   -> Inserted {len(primary_rows):,} morphological tags.")
        
    print("3. Importing Amarakośa (amara.json)...")
    if os.path.exists("amara.json"):
        with open("amara.json", "r", encoding="utf-8") as f:
            amara_data = json.load(f)
        amara_rows = [(w.get("word", "").strip(), w.get("artha", ""), ", ".join(w.get("synonyms", [])), w.get("linga", "")) 
                      for v in amara_data.get("data", []) for w in v.get("words", []) if w.get("word", "").strip()]
        cursor.executemany('INSERT OR IGNORE INTO amarakosha VALUES (?, ?, ?, ?)', amara_rows)
        print(f"   -> Inserted {len(amara_rows):,} synonym entries.")

    print("4. Importing Mini Aṣṭādhyāyī Terminology (JSON)...")
    ash_rows = []
    for file in ["glossary.json", "pratyahara.json"]:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    # --- NEW SAFEGUARD ---
                    if not isinstance(item, dict):
                        continue
                        
                    word = item.get("devanagari", "").strip()
                    if not word:
                        continue
                    
                    item_id = item.get("id", "")
                    iast = item.get("iast", "")
                    slp1 = item.get("slp1", "")
                    meaning = item.get("meaning", "")
                    
                    aliases = json.dumps(item.get("aliases", []), ensure_ascii=False)
                    members = json.dumps(item.get("members", []), ensure_ascii=False)
                    
                    ash_rows.append((word, item_id, iast, slp1, aliases, meaning, members))
    
    if ash_rows:
        cursor.executemany('''
            INSERT OR IGNORE INTO ashtadhyayi 
            (word, id, iast, slp1, aliases, meaning, members) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ash_rows)
        print(f"   -> Inserted {len(ash_rows):,} technical terms & pratyāhāras.")

    print("5. Importing Mini Aṣṭādhyāyī Sūtras (JSON)...")
    sutra_rows = []
    for file in ["sutras-1-1.json", "sutras-1-2.json"]:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    # --- NEW SAFEGUARD ---
                    if not isinstance(item, dict):
                        continue
                        
                    s_id = item.get("id", "")
                    if not s_id:
                        continue
                        
                    slp1 = item.get("slp1", "")
                    slp1Disp = item.get("slp1Display", "")
                    sType = item.get("type", "")
                    typeDisp = item.get("typeDisplay", "")
                    udd = item.get("uddeshya", "")
                    vid = item.get("vidheya", "")
                    
                    meaning = item.get("meaning", "")
                    expl = item.get("explanation", item.get("purpose", ""))
                    anuv = item.get("anuvritti", "")
                    adhi = item.get("adhikara", "")
                    notes = item.get("notes", "")
                    
                    examples = json.dumps(item.get("examples", []), ensure_ascii=False)
                    related = json.dumps(item.get("related", []), ensure_ascii=False)
                    glossary = json.dumps(item.get("glossary", []), ensure_ascii=False)
                    searchAl = json.dumps(item.get("searchAliases", []), ensure_ascii=False)
                    
                    sutra_rows.append((
                        s_id, slp1, slp1Disp, sType, typeDisp, 
                        udd, vid, meaning, expl, anuv, adhi, 
                        examples, related, glossary, notes, searchAl
                    ))

    if sutra_rows:
        cursor.executemany('''
            INSERT OR IGNORE INTO sutras 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sutra_rows)
        print(f"   -> Inserted {len(sutra_rows):,} Pāṇinian Sūtras.")

    print("6. Creating Indexes...")
    cursor.execute('CREATE INDEX idx_dictionary_word ON dictionary(word)')
    cursor.execute('CREATE INDEX idx_ashtadhyayi_word ON ashtadhyayi(word)')
    
    conn.commit()
    conn.close()
    print("\nSuccess! 'sanskrit_engine.db' has been built and is ready.")

if __name__ == "__main__":
    build_database()