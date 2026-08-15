#!/usr/bin/env python3
"""
Phase 2: Import all Gita JSON data into SQLite.
Creates: gita_analytics.db (separate from sanskrit_engine.db)
"""

import json
import sqlite3
import os

DB_PATH = "gita_analytics.db"

def main():
    # Remove old DB if exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ════════════════════════════════════════════════════════
    # Table 1: gita_words — master word index
    # ════════════════════════════════════════════════════════
    print("Importing word index...")
    with open("gita_assets/gita_word_index.json", "r", encoding="utf-8") as f:
        word_index = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devanagari TEXT UNIQUE,
            iast TEXT,
            verses TEXT,
            occurrence_count INTEGER
        )
    ''')

    for entry in word_index:
        cursor.execute(
            'INSERT INTO gita_words (devanagari, iast, verses, occurrence_count) VALUES (?, ?, ?, ?)',
            (entry["devanagari"], entry["iast"],
             json.dumps(entry["verses"], ensure_ascii=False),
             entry.get("count", len(entry["verses"])))
        )

    # ════════════════════════════════════════════════════════
    # Table 2: gita_frequency — top words + longest words + distribution
    # ════════════════════════════════════════════════════════
    print("Importing frequency data...")
    with open("gita_assets/gita_frequency.json", "r", encoding="utf-8") as f:
        freq = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_frequency (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devanagari TEXT,
            iast TEXT,
            frequency INTEGER,
            rank INTEGER
        )
    ''')

    for rank, entry in enumerate(freq["top_100_by_frequency"], 1):
        cursor.execute(
            'INSERT INTO gita_frequency (devanagari, iast, frequency, rank) VALUES (?, ?, ?, ?)',
            (entry["devanagari"], entry["iast"], entry["frequency"], rank)
        )

    # Longest words table
    cursor.execute('''
        CREATE TABLE gita_longest_words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devanagari TEXT,
            iast TEXT,
            length INTEGER,
            frequency INTEGER
        )
    ''')

    for entry in freq["top_100_longest"]:
        cursor.execute(
            'INSERT INTO gita_longest_words (devanagari, iast, length, frequency) VALUES (?, ?, ?, ?)',
            (entry["devanagari"], entry["iast"], entry["length"], entry["frequency"])
        )

    # Word length distribution
    cursor.execute('''
        CREATE TABLE gita_word_length_dist (
            length INTEGER PRIMARY KEY,
            occurrences INTEGER
        )
    ''')

    for entry in freq["word_length_distribution"]:
        cursor.execute(
            'INSERT INTO gita_word_length_dist (length, occurrences) VALUES (?, ?)',
            (entry["length"], entry["occurrences"])
        )

    # ════════════════════════════════════════════════════════
    # Table 3: gita_speakers — speaker analysis
    # ════════════════════════════════════════════════════════
    print("Importing speaker data...")
    with open("gita_assets/gita_epithets.json", "r", encoding="utf-8") as f:
        epithets = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_speakers (
            speaker TEXT PRIMARY KEY,
            verse_ids TEXT
        )
    ''')

    for detail in epithets["speaker_details"]:
        cursor.execute(
            'INSERT INTO gita_speakers (speaker, verse_ids) VALUES (?, ?)',
            (detail["speaker"],
             json.dumps(detail["verse_ids"], ensure_ascii=False))
        )

    # ════════════════════════════════════════════════════════
    # Table 4: gita_epithets — epithet attribution
    # ════════════════════════════════════════════════════════
    print("Importing epithet data...")
    with open("gita_assets/gita_epithets_attr.json", "r", encoding="utf-8") as f:
        epithet_attr = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_epithets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english TEXT,
            devanagari TEXT,
            belongs_to TEXT,
            count INTEGER,
            explanation TEXT
        )
    ''')

    for entry in epithet_attr["krishna_epithets"]:
        cursor.execute(
            'INSERT INTO gita_epithets (english, devanagari, belongs_to, count, explanation) VALUES (?, ?, ?, ?, ?)',
            (entry["english"], entry["devanagari"], "Krishna", entry["count"], entry.get("explanation", ""))
        )

    for entry in epithet_attr["arjuna_epithets"]:
        cursor.execute(
            'INSERT INTO gita_epithets (english, devanagari, belongs_to, count, explanation) VALUES (?, ?, ?, ?, ?)',
            (entry["english"], entry["devanagari"], "Arjuna", entry["count"], entry.get("explanation", ""))
        )

    # ════════════════════════════════════════════════════════
    # Table 5: gita_chapters — chapter-wise index
    # ════════════════════════════════════════════════════════
    print("Importing chapter index...")
    with open("gita_assets/gita_chapter_index.json", "r", encoding="utf-8") as f:
        chapter_data = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_chapters (
            chapter_number INTEGER PRIMARY KEY,
            total_words INTEGER,
            unique_words INTEGER,
            verses_in_chapter INTEGER,
            top_words TEXT
        )
    ''')

    for ch_num, ch in chapter_data["chapters"].items():
        cursor.execute(
            'INSERT INTO gita_chapters (chapter_number, total_words, unique_words, verses_in_chapter, top_words) VALUES (?, ?, ?, ?, ?)',
            (int(ch_num), ch["total_words"], ch["unique_words"],
             ch["verses_in_chapter"],
             json.dumps(ch["top_20_words"], ensure_ascii=False))
        )

    # Chapter words detail table (full word index per chapter)
    cursor.execute('''
        CREATE TABLE gita_chapter_words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_number INTEGER,
            word TEXT,
            count INTEGER,
            verses TEXT
        )
    ''')

    for ch_num, ch in chapter_data["chapters"].items():
        for wi in ch["word_index"]:
            cursor.execute(
                'INSERT INTO gita_chapter_words (chapter_number, word, count, verses) VALUES (?, ?, ?, ?)',
                (int(ch_num), wi["word"], wi["count"],
                 json.dumps(wi["verses"], ensure_ascii=False))
            )

    # ════════════════════════════════════════════════════════
    # Table 6: gita_chronological — word order by first appearance
    # ════════════════════════════════════════════════════════
    print("Importing chronological index...")
    with open("gita_assets/gita_chronological.json", "r", encoding="utf-8") as f:
        chrono = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_chronological (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            first_verse TEXT,
            first_position INTEGER,
            total_occurrences INTEGER,
            verses TEXT
        )
    ''')

    for entry in chrono["chronological_index"]:
        cursor.execute(
            'INSERT INTO gita_chronological (word, first_verse, first_position, total_occurrences, verses) VALUES (?, ?, ?, ?, ?)',
            (entry["word"], entry["first_verse"], entry["first_position"],
             entry["total_occurrences"],
             json.dumps(entry["verses"], ensure_ascii=False))
        )

    # ════════════════════════════════════════════════════════
    # Table 7: gita_crossref — words with glossary meanings
    # ════════════════════════════════════════════════════════
    print("Importing cross-reference data...")
    with open("gita_assets/gita_crossref.json", "r", encoding="utf-8") as f:
        crossref = json.load(f)

    cursor.execute('''
        CREATE TABLE gita_crossref (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devanagari TEXT,
            iast TEXT,
            verses TEXT,
            occurrence_count INTEGER,
            meanings TEXT,
            has_meaning INTEGER
        )
    ''')

    for entry in crossref:
        cursor.execute(
            'INSERT INTO gita_crossref (devanagari, iast, verses, occurrence_count, meanings, has_meaning) VALUES (?, ?, ?, ?, ?, ?)',
            (entry["devanagari"], entry["iast"],
             json.dumps(entry.get("verses", []), ensure_ascii=False),
             entry.get("occurrences", 0),
             json.dumps(entry["meanings"], ensure_ascii=False),
             1 if entry["has_meaning"] else 0)
        )

    conn.commit()
    conn.close()

    # Summary
    print("\n=== Database Creation Complete ===")
    print(f"Database: {DB_PATH}")
    print(f"Size: {os.path.getsize(DB_PATH) / 1024:.1f} KB")
    print(f"\nTables created:")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    for table in cursor.fetchall():
        cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
        count = cursor.fetchone()[0]
        print(f"  {table[0]}: {count} rows")
    conn.close()

    print(f"\n✓ {DB_PATH} created successfully")

if __name__ == "__main__":
    main()