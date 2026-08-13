#!/usr/bin/env python3
"""
Phase 1.1: Generate frequency stats from gita_data.json
Outputs: gita_frequency.json
"""

import json
import re
from collections import Counter
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

DEV_PUNCT = "।॥,;:!?()[]{}'\" \n\t\r॰"

def extract_words(text_lines):
    words = []
    for line in text_lines:
        for token in line.split():
            cleaned = token.strip(DEV_PUNCT)
            if cleaned:
                words.append(cleaned)
    return words

def main():
    with open("gita_assets/gita_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    verses = data.get("verses", {})
    
    word_freq = Counter()
    word_lengths = {}
    
    for verse_id, vdata in verses.items():
        sa_lines = vdata.get("text", {}).get("sa", [])
        words = extract_words(sa_lines)
        for word in words:
            word_freq[word] += 1
            if word not in word_lengths:
                word_lengths[word] = len(word)
    
    # Top 100 by frequency
    top_words = []
    for word, count in word_freq.most_common(100):
        try:
            iast = transliterate(word, sanscript.DEVANAGARI, sanscript.IAST)
        except:
            iast = ""
        top_words.append({
            "devanagari": word,
            "iast": iast,
            "frequency": count
        })
    
    # Top 100 longest (tie-break by frequency desc)
    longest_words = sorted(
        word_freq.keys(),
        key=lambda w: (-len(w), -word_freq[w])
    )[:100]
    
    longest = []
    for word in longest_words:
        try:
            iast = transliterate(word, sanscript.DEVANAGARI, sanscript.IAST)
        except:
            iast = ""
        longest.append({
            "devanagari": word,
            "iast": iast,
            "length": len(word),
            "frequency": word_freq[word]
        })
    
    # Word length distribution
    length_dist = Counter()
    for word, freq in word_freq.items():
        length_dist[len(word)] += freq
    
    length_distribution = [
        {"length": k, "occurrences": v}
        for k, v in sorted(length_dist.items())
    ]
    
    output = {
        "total_unique_words": len(word_freq),
        "total_word_occurrences": sum(word_freq.values()),
        "top_100_by_frequency": top_words,
        "top_100_longest": longest,
        "word_length_distribution": length_distribution
    }
    
    with open("gita_assets/gita_frequency.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    # Console summary
    print("=== Frequency Analysis ===")
    print(f"Total unique words: {output['total_unique_words']}")
    print(f"Total occurrences: {output['total_word_occurrences']}")
    print(f"\nTop 100 by frequency:")
    for i, w in enumerate(top_words, 1):
        print(f"  {i}. {w['devanagari']} ({w['iast']}) — {w['frequency']}x")
    print(f"\nTop 100 longest:")
    for i, w in enumerate(longest, 1):
        print(f"  {i}. {w['devanagari']} ({w['iast']}) — {w['length']} chars, {w['frequency']}x")
    print(f"\n✓ gita_frequency.json created")

if __name__ == "__main__":
    main()