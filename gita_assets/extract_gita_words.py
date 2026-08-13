#!/usr/bin/env python3
"""
Build a Sanskrit word index from gita_data.json.
For each unique Devanagari word, records which verses it appears in.
Includes IAST transliteration via indic_transliteration.
"""

import json
import re
from collections import defaultdict
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Punctuation to strip from word boundaries
DEV_PUNCT = "।॥,;:!?()[]{}'\" \n\t\r॰॥॰"

def extract_words(text_lines):
    """Split Sanskrit text into words by whitespace, strip punctuation."""
    words = []
    for line in text_lines:
        for token in line.split():
            cleaned = token.strip(DEV_PUNCT)
            if cleaned:
                words.append(cleaned)
    return words

def build_index(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    verses = data.get("verses", {})

    # word → set of verse IDs
    word_verses = defaultdict(set)

    for verse_id, vdata in verses.items():
        sa_lines = vdata.get("text", {}).get("sa", [])
        words = extract_words(sa_lines)
        for word in words:
            word_verses[word].add(verse_id)

    # Sort: Devanagari alphabetical
    sorted_words = sorted(word_verses.keys())

    # Build output with transliteration
    index = []
    for word in sorted_words:
        try:
            iast = transliterate(word, sanscript.DEVANAGARI, sanscript.IAST)
        except Exception:
            iast = ""

        index.append({
            "devanagari": word,
            "iast": iast,
            "verses": sorted(word_verses[word], key=lambda v: [int(x) for x in v.split(":")]),
            "count": len(word_verses[word])
        })

    return index

def main():
    json_path = "gita_data.json"

    print("Building Sanskrit word index...")
    index = build_index(json_path)

    # ── Output 1: Human-readable text file ──
    with open("gita_word_index.txt", "w", encoding="utf-8") as f:
        f.write("# Bhagavad Gita — Sanskrit Word Index\n")
        f.write(f"# Total unique words: {len(index)}\n\n")
        for entry in index:
            verses_str = ", ".join(entry["verses"])
            f.write(f"{entry['devanagari']} ({entry['iast']})\n")
            f.write(f"  Verses: [{verses_str}]\n")
            f.write(f"  Occurrences: {entry['count']}\n\n")
    print(f"✓ gita_word_index.txt ({len(index)} words)")

    # ── Output 2: JSON for database import ──
    with open("gita_word_index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"✓ gita_word_index.json")

    # ── Summary ──
    total_occurrences = sum(e["count"] for e in index)
    print(f"\n=== Summary ===")
    print(f"Unique words: {len(index)}")
    print(f"Total occurrences: {total_occurrences}")

if __name__ == "__main__":
    main()