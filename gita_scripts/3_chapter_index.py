#!/usr/bin/env python3
"""
Phase 1.3: Chapter-wise word index
Outputs: gita_chapter_index.json
"""

import json
import re
from collections import defaultdict, Counter

DEV_PUNCT = "।॥,;:!?()[]{}'\" \n\t\r॰"

def extract_words(text_lines):
    """Split Sanskrit text into words."""
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

    # ── Build chapter-level structures ──
    chapter_word_counts = {}  # chapter_num → {word: count}
    chapter_word_verses = {}  # chapter_num → {word: [verse_ids]}
    chapter_total_words = {}  # chapter_num → total word occurrences
    chapter_unique_words = {}  # chapter_num → unique word count

    for verse_id, vdata in verses.items():
        # Parse chapter from verse_id (format: "X:Y")
        parts = verse_id.split(":")
        chapter_num = int(parts[0])

        sa_lines = vdata.get("text", {}).get("sa", [])
        words = extract_words(sa_lines)

        # Initialize chapter if new
        if chapter_num not in chapter_word_counts:
            chapter_word_counts[chapter_num] = Counter()
            chapter_word_verses[chapter_num] = defaultdict(list)
            chapter_total_words[chapter_num] = 0

        # Accumulate
        for word in words:
            chapter_word_counts[chapter_num][word] += 1
            chapter_word_verses[chapter_num][word].append(verse_id)
            chapter_total_words[chapter_num] += 1

    # Finalize unique counts
    for ch in chapter_word_counts:
        chapter_unique_words[ch] = len(chapter_word_counts[ch])

    # ── Convert to JSON-friendly format ──
    output = {}

    for ch in sorted(chapter_word_counts.keys()):
        # Get top 20 words for this chapter
        top_words = [
            {"word": w, "count": c}
            for w, c in chapter_word_counts[ch].most_common(20)
        ]

        output[str(ch)] = {
            "chapter_number": ch,
            "total_words": chapter_total_words[ch],
            "unique_words": chapter_unique_words[ch],
            "verses_in_chapter": len([v for v in verses.keys() if v.startswith(f"{ch}:")]),
            "top_20_words": top_words,
            # Full word index (comment out for smaller file if needed)
            "word_index": [
                {"word": w, "count": c, "verses": chapter_word_verses[ch][w]}
                for w, c in sorted(chapter_word_counts[ch].items())
            ]
        }

    # Global summary
    all_words = Counter()
    for ch_counter in chapter_word_counts.values():
        all_words.update(ch_counter)

    global_stats = {
        "total_chapters": len(chapter_word_counts),
        "total_unique_words_across_chapters": len(all_words),
        "chapter_with_most_unique_words": max(chapter_unique_words, key=chapter_unique_words.get),
        "chapter_with_fewest_unique_words": min(chapter_unique_words, key=chapter_unique_words.get),
    }

    full_output = {
        "statistics": global_stats,
        "chapters": output
    }

    with open("gita_assets/gita_chapter_index.json", "w", encoding="utf-8") as f:
        json.dump(full_output, f, ensure_ascii=False, indent=2)

    # Console summary
    print("\n=== Chapter Summary ===")
    print(f"{'Chap':<5} {'Verses':<7} {'Total':<8} {'Unique':<8} {'Top Word'}")
    print("-" * 50)

    for ch in sorted(output.keys()):
        data = output[ch]
        top_word = data['top_20_words'][0]['word'] if data['top_20_words'] else "-"
        verse_count = data['verses_in_chapter']
        print(f"{ch:<5} {verse_count:<7} {data['total_words']:<8} {data['unique_words']:<8} {top_word}")

    print("\n=== Global Stats ===")
    print(f"Total unique words across all chapters: {global_stats['total_unique_words_across_chapters']}")
    print(f"Chapter with most unique words: {global_stats['chapter_with_most_unique_words']}")
    print(f"Chapter with fewest unique words: {global_stats['chapter_with_fewest_unique_words']}")

    print(f"\n✓ gita_chapter_index.json created")

if __name__ == "__main__":
    main()