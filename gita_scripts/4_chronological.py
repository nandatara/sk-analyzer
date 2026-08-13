#!/usr/bin/env python3
"""
Phase 1.4: Chronological word index — order words by first appearance in the Gita.
Outputs: gita_chronological.json
"""

import json
import re
from collections import defaultdict

DEV_PUNCT = "।॥,;:!?()[]{}'\" \n\t\r॰"

def verse_sort_key(verse_id):
    """Sort key for verse IDs like '1:1', '1:10', '2:3'."""
    parts = verse_id.split(":")
    return (int(parts[0]), int(parts[1]))

def extract_words(text_lines):
    words = []
    for line in text_lines:
        for token in line.split():
            cleaned = token.strip(DEV_PUNCT)
            if cleaned:
                words.append(cleaned)
    return words

def main():
    print("Loading data...")

    with open("gita_assets/gita_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    verses = data.get("verses", {})

    # Sort verse IDs chronologically
    sorted_verse_ids = sorted(verses.keys(), key=verse_sort_key)

    # Track first appearance and all appearances
    word_first_appearance = {}  # word → (chapter, verse, position_in_verse)
    word_all_appearances = defaultdict(list)  # word → [(verse_id, position), ...]

    for verse_id in sorted_verse_ids:
        vdata = verses[verse_id]
        sa_lines = vdata.get("text", {}).get("sa", [])
        words = extract_words(sa_lines)

        for position, word in enumerate(words):
            word_all_appearances[word].append((verse_id, position))

            if word not in word_first_appearance:
                word_first_appearance[word] = (verse_id, position)

    # Build chronological list
    chronological = []
    for word in sorted(word_first_appearance.keys(),
                        key=lambda w: (verse_sort_key(word_first_appearance[w][0]),
                                       word_first_appearance[w][1])):
        first_verse, first_pos = word_first_appearance[word]
        appearances = word_all_appearances[word]

        chronological.append({
            "word": word,
            "first_verse": first_verse,
            "first_position": first_pos,
            "total_occurrences": len(appearances),
            "verses": [a[0] for a in appearances]
        })

    output = {
        "total_unique_words": len(chronological),
        "chronological_index": chronological
    }

    with open("gita_assets/gita_chronological.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Console summary
    print("\n=== Chronological Index Summary ===")
    print(f"Total unique words: {len(chronological)}")

    print("\nFirst 20 words in chronological order:")
    for i, entry in enumerate(chronological[:20], 1):
        print(f"  {i}. {entry['word']} — first at {entry['first_verse']}:{entry['first_position']}, {entry['total_occurrences']}x total")

    print("\nLast 10 words (appear latest):")
    for entry in chronological[-10:]:
        print(f"  {entry['word']} — first at {entry['first_verse']}:{entry['first_position']}, {entry['total_occurrences']}x total")

    print(f"\n✓ gita_chronological.json created")

if __name__ == "__main__":
    main()