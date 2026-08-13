#!/usr/bin/env python3
"""
Phase 1.2: Analyze speakers and epithets in Gita
Outputs: gita_epithets.json
"""

import json
import re
from collections import Counter, defaultdict

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
        lines = js_str.split('\n')
        print(f"JSON parse error at line {e.lineno}, col {e.colno}")
        for ln in range(max(0, e.lineno - 3), min(len(lines), e.lineno + 2)):
            marker = ">>>" if ln == e.lineno - 1 else "   "
            print(f"  {marker} {ln+1}: {lines[ln][:120]}")
        return {}

def find_speakers(verses):
    """Find all speaker instances using strict whitelist."""
    speakers = Counter()
    speaker_verses = defaultdict(list)

    speaker_patterns = {
        "अर्जुन उवाच": "Arjuna",
        "सञ्जय उवाच": "Sanjaya",
        "धृतराष्ट्र उवाच": "Dhritarashtra",
        "श्रीभगवानुवाच": "Krishna",
        "श्रीभगवानुवाच": "Krishna",
    }

    for verse_id, vdata in verses.items():
        sa_lines = vdata.get("text", {}).get("sa", [])
        full_text = " ".join(sa_lines)

        for pattern, canonical in speaker_patterns.items():
            if pattern in full_text:
                speakers[canonical] += 1
                speaker_verses[canonical].append(verse_id)

    return dict(speakers), dict(speaker_verses)

def main():
    print("Loading data...")

    with open("gita_assets/gita_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    epithet_db = load_epithet_db("gita_assets/epithets.js")
    print(f"Loaded {len(epithet_db)} epithets from database")

    verses = data.get("verses", {})

    print("Analyzing speakers...")
    speaker_counts, speaker_verses = find_speakers(verses)

    # Initialize epithet_usage at the START, before any loops
    epithet_usage = []
    
    for epithet_en, epit_data in epithet_db.items():
        title = epit_data.get("title", "")
        deva_match = re.search(r'[\u0900-\u097F]+', title)
        epithet_deva = deva_match.group(0) if deva_match else ""

        usage_verses = []
        for verse_id, vdata in verses.items():
            sa_lines = vdata.get("text", {}).get("sa", [])
            full_text = " ".join(sa_lines)
            if epithet_deva and epithet_deva in full_text:
                usage_verses.append(verse_id)

        epithet_usage.append({
            "english": epithet_en,
            "devanagari": epithet_deva,
            "explanation": epit_data.get("explanation", ""),
            "verses": usage_verses,
            "count": len(usage_verses)
        })

    epithet_usage.sort(key=lambda e: -e["count"])

    output = {
        "speaker_summary": {
            "total_uvacas": sum(speaker_counts.values()),
            "by_speaker": [
                {"speaker": s, "count": c}
                for s, c in sorted(speaker_counts.items(), key=lambda x: -x[1])
            ],
        },
        "speaker_details": [
            {
                "speaker": speaker,
                "verse_ids": sorted(verses_list, key=lambda x: [int(n) for n in x.split(":")])
            }
            for speaker, verses_list in speaker_verses.items()
        ],
        "epithet_analysis": epithet_usage,
        "epithet_db_loaded": len(epithet_db)
    }

    with open("gita_assets/gita_epithets.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("\n=== Speaker Analysis ===")
    print(f"Total 'उवāच' occurrences: {output['speaker_summary']['total_uvacas']}")
    print("\nBy canonical speaker:")
    for entry in output['speaker_summary']['by_speaker']:
        print(f"  {entry['speaker']}: {entry['count']}x")

    print(f"\n=== Epithet Analysis ===")
    print(f"Epithets in database: {len(epithet_db)}")
    found = [e for e in epithet_usage if e["count"] > 0]
    print(f"Epithets found in text: {len(found)}")
    for epit in found[:25]:
        print(f"  {epit['devanagari']} ({epit['english']}): {epit['count']}x")

    print(f"\n✓ gita_epithets.json created")

if __name__ == "__main__":
    main()