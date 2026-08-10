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
    
    cursor.execute('CREATE TABLE IF NOT EXISTS dictionary (word TEXT, pos TEXT, meaning TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS amarakosha (word TEXT PRIMARY KEY, artha TEXT, synonyms TEXT, linga TEXT)')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ashtadhyayi (
            word TEXT PRIMARY KEY, id TEXT, iast TEXT, slp1 TEXT, 
            aliases TEXT, meaning TEXT, members TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sutras (
            id TEXT PRIMARY KEY, slp1 TEXT, slp1Display TEXT, type TEXT, typeDisplay TEXT,
            uddeshya TEXT, vidheya TEXT, meaning TEXT, explanation TEXT, anuvritti TEXT,
            adhikara TEXT, examples TEXT, related TEXT, glossary TEXT, notes TEXT, searchAliases TEXT
        )
    ''')
    
    # NEW: Expanded Gītā Verses Table to hold Pada and Anvaya
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gita_verses (
            id TEXT PRIMARY KEY,
            chapter INTEGER,
            verse INTEGER,
            text_sa TEXT,
            text_iast TEXT,
            overrides TEXT,
            pada_sa TEXT,
            pada_iast TEXT,
            anvaya_sa TEXT,
            anvaya_iast TEXT,
            translation TEXT,
            explanation TEXT,
            word_meanings TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gita_glossary (
            word TEXT PRIMARY KEY,
            meaning TEXT
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

    print("4. Importing Mini Aṣṭādhyāyī Terminology...")
    ash_rows = []
    for file in ["glossary.json", "pratyahara.json"]:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if not isinstance(item, dict): continue
                    word = item.get("devanagari", "").strip()
                    if not word: continue
                    ash_rows.append((
                        word, item.get("id", ""), item.get("iast", ""), item.get("slp1", ""),
                        json.dumps(item.get("aliases", []), ensure_ascii=False),
                        item.get("meaning", ""),
                        json.dumps(item.get("members", []), ensure_ascii=False)
                    ))
    if ash_rows:
        cursor.executemany('INSERT OR IGNORE INTO ashtadhyayi VALUES (?, ?, ?, ?, ?, ?, ?)', ash_rows)
        print(f"   -> Inserted {len(ash_rows):,} technical terms & pratyāhāras.")

    print("5. Importing Mini Aṣṭādhyāyī Sūtras...")
    sutra_rows = []
    for file in ["sutras-1-1.json", "sutras-1-2.json"]:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if not isinstance(item, dict): continue
                    s_id = item.get("id", "")
                    if not s_id: continue
                    sutra_rows.append((
                        s_id, item.get("slp1", ""), item.get("slp1Display", ""), item.get("type", ""), item.get("typeDisplay", ""),
                        item.get("uddeshya", ""), item.get("vidheya", ""), item.get("meaning", ""), 
                        item.get("explanation", item.get("purpose", "")), item.get("anuvritti", ""), item.get("adhikara", ""),
                        json.dumps(item.get("examples", []), ensure_ascii=False), json.dumps(item.get("related", []), ensure_ascii=False),
                        json.dumps(item.get("glossary", []), ensure_ascii=False), item.get("notes", ""), 
                        json.dumps(item.get("searchAliases", []), ensure_ascii=False)
                    ))
    if sutra_rows:
        cursor.executemany('INSERT OR IGNORE INTO sutras VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', sutra_rows)
        print(f"   -> Inserted {len(sutra_rows):,} Pāṇinian Sūtras.")

    print("6. Importing Bhagavad Gītā Data...")
    gita_file = os.path.join("gita_assets", "gita_data.json")
    if os.path.exists(gita_file):
        with open(gita_file, "r", encoding="utf-8") as f:
            gita_data = json.load(f)
            
        verses = gita_data.get("verses", {})
        verse_rows = []
        for v_id, v_data in verses.items():
            parts = v_id.split(":")
            ch = int(parts[0]) if len(parts) == 2 else 0
            vs = int(parts[1]) if len(parts) == 2 else 0
            
            text_sa = json.dumps(v_data.get("text", {}).get("sa", []), ensure_ascii=False)
            text_iast = json.dumps(v_data.get("text", {}).get("iast", []), ensure_ascii=False)
            overrides = json.dumps(v_data.get("overrides", {}), ensure_ascii=False)
            
            # Extract new Pada and Anvaya data
            pada_iast = v_data.get("pada_iast", "")
            pada_sa = v_data.get("pada_sa", "")
            anvaya_sa = v_data.get("anvaya_sa", "")
            anvaya_iast = v_data.get("anvaya_iast", "")
            
            # NEW: Extract English Data
            translation = v_data.get("translation", "")
            explanation = v_data.get("explanation", "")
            word_meanings = v_data.get("word_meanings", "")
            
            verse_rows.append((v_id, ch, vs, text_sa, text_iast, overrides, pada_sa, pada_iast, anvaya_sa, anvaya_iast, translation, explanation, word_meanings))
            
        if verse_rows:
            cursor.executemany('INSERT OR IGNORE INTO gita_verses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', verse_rows)
            print(f"   -> Inserted {len(verse_rows):,} Gītā verses.")
            
        glossary = gita_data.get("glossary", {})
        glossary_rows = [(word, meaning) for word, meaning in glossary.items()]
        if glossary_rows:
            cursor.executemany('INSERT OR IGNORE INTO gita_glossary VALUES (?, ?)', glossary_rows)
            print(f"   -> Inserted {len(glossary_rows):,} Gītā glossary entries.")

    print("7. Creating Indexes...")
    cursor.execute('CREATE INDEX idx_dictionary_word ON dictionary(word)')
    cursor.execute('CREATE INDEX idx_ashtadhyayi_word ON ashtadhyayi(word)')
    cursor.execute('CREATE INDEX idx_gita_chapter ON gita_verses(chapter)')
    
    conn.commit()
    conn.close()
    print("\nSuccess! 'sanskrit_engine.db' has been built and is ready.")

if __name__ == "__main__":
    build_database()