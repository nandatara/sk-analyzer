#!/usr/bin/env python3
"""
Phase 1.3: Epithet Attribution using explicit split rule
Outputs: gita_epithets_attr.json
"""

import json
import re
from collections import defaultdict

DEV_PUNCT = "।॥,;:!?()[]{}'\" \n\t\r॰"

def load_epithet_db(filepath="gita_assets/epithets.js"):
    """Parse EPITHET_DB from JS file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = re.search(r'const\s+EPITHET_DB\s*=\s*', content)
    if not marker:
        print("ERROR: Could not find EPITHET_DB in file")
        return {}

    start = marker.end()

    brace_count = 0
    in_string = False
    escape_next = False
    string_char = None
    obj_end = None

    for i, char in enumerate(content[start:], start=start):
        if escape_next:
            escape_next = False
            continue
        if char == '\\':
            escape_next = True
            continue
        if char in '"\'`':
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
            continue
        if in_string:
            continue
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                obj_end = i + 1
                break

    if obj_end is None:
        print("ERROR: Could not find end of EPITHET_DB object")
        return {}

    js_str = content[start:obj_end]
    js_str = re.sub(r'//.*?$', '', js_str, flags=re.MULTILINE)
    js_str = re.sub(r'/\*.*?\*/', '', js_str, flags=re.DOTALL)
    js_str = re.sub(r',(\s*[}\]])', r'\1', js_str)

    try:
        return json.loads(js_str)
    except json.JSONDecodeError as e:
        print(f"JSON parse error at line {e.lineno}")
        return {}

def extract_words_from_text(full_text):
    """Extract Devanagari words from text."""
    words = re.findall(r'[\u0900-\u097F]+', full_text)
    return [w.strip(DEV_PUNCT) for w in words if w.strip(DEV_PUNCT)]

def main():
    print("Loading data...")

    with open("gita_assets/gita_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    epithet_db = load_epithet_db("gita_assets/epithets.js")
    print(f"Loaded {len(epithet_db)} epithets from database")

    verses = data.get("verses", {})

    # ── KEY CHANGE: Split epithets at "Arjuna" key ──
    krishna_epithets = []
    arjuna_epithets = []
    found_arjuna = False

    for epithet_en, epit_data in epithet_db.items():
        if epithet_en == "Arjuna":
            found_arjuna = True
        if not found_arjuna:
            krishna_epithets.append((epithet_en, epit_data))
        else:
            arjuna_epithets.append((epithet_en, epit_data))

    print(f"Krishna epithets: {len(krishna_epithets)}")
    print(f"Arjuna epithets: {len(arjuna_epithets)}")

    # Count occurrences
    krishna_counts = []
    arjuna_counts = []

    for epithet_en, epit_data in krishna_epithets:
        title = epit_data.get("title", "")
        deva_match = re.search(r'[\u0900-\u097F]+', title)
        epithet_deva = deva_match.group(0) if deva_match else ""

        count = 0
        for verse_id, vdata in verses.items():
            sa_lines = vdata.get("text", {}).get("sa", [])
            full_text = " ".join(sa_lines)
            if epithet_deva and epithet_deva in full_text:
                count += 1

        krishna_counts.append({
            "english": epithet_en,
            "devanagari": epithet_deva,
            "explanation": epit_data.get("explanation", ""),
            "count": count
        })

    for epithet_en, epit_data in arjuna_epithets:
        title = epit_data.get("title", "")
        deva_match = re.search(r'[\u0900-\u097F]+', title)
        epithet_deva = deva_match.group(0) if deva_match else ""

        count = 0
        for verse_id, vdata in verses.items():
            sa_lines = vdata.get("text", {}).get("sa", [])
            full_text = " ".join(sa_lines)
            if epithet_deva and epithet_deva in full_text:
                count += 1

        arjuna_counts.append({
            "english": epithet_en,
            "devanagari": epithet_deva,
            "explanation": epit_data.get("explanation", ""),
            "count": count
        })

    # Sort by frequency
    krishna_counts.sort(key=lambda e: -e["count"])
    arjuna_counts.sort(key=lambda e: -e["count"])

    output = {
        "krishna_epithets": krishna_counts,
        "arjuna_epithets": arjuna_counts,
        "summary": {
            "krishna_total": sum(e["count"] for e in krishna_counts),
            "arjuna_total": sum(e["count"] for e in arjuna_counts)
        }
    }

    with open("gita_assets/gita_epithets_attr.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("\n=== Krishna Epithets ===")
    for ep in krishna_counts[:15]:
        print(f"  {ep['devanagari']} ({ep['english']}): {ep['count']}x")
    print(f"  Total: {output['summary']['krishna_total']}")

    print("\n=== Arjuna Epithets ===")
    for ep in arjuna_counts[:15]:
        print(f"  {ep['devanagari']} ({ep['english']}): {ep['count']}x")
    print(f"  Total: {output['summary']['arjuna_total']}")

    print(f"\n✓ gita_epithets_attr.json created")

if __name__ == "__main__":
    main()