#!/usr/bin/env python3
"""
Phase 1.5: Cross-reference Gita words with glossaries
Matches gita_word_index.json against glossary-en.js, glossary-hi.js, glossary-db.js
Outputs: gita_crossref.json
"""

import json
import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def parse_js_dict(filepath, var_name):
    """Parse a simple const VAR = { "key": "value", ... } JS file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = re.search(rf'const\s+{var_name}\s*=\s*', content)
    if not marker:
        print(f"  Could not find {var_name} in {filepath}")
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
        print(f"  Could not find end of {var_name}")
        return {}

    js_str = content[start:obj_end]
    js_str = re.sub(r'//.*?$', '', js_str, flags=re.MULTILINE)
    js_str = re.sub(r'/\*.*?\*/', '', js_str, flags=re.DOTALL)
    js_str = re.sub(r',(\s*[}\]])', r'\1', js_str)

    try:
        return json.loads(js_str)
    except json.JSONDecodeError as e:
        print(f"  JSON parse error in {var_name} at line {e.lineno}")
        return {}

def normalize_iast(text):
    """Normalize IAST variants for matching."""
    # Common variants in Gita translations
    replacements = {
        'ṛ': 'r̥', 'ṝ': 'r̥̄', 'ṅ': 'ṅ', 'ñ': 'ñ',
        'ṭ': 'ṭ', 'ḍ': 'ḍ', 'ṇ': 'ṇ', 'ś': 'ś', 'ṣ': 'ṣ',
        'ḥ': 'ḥ', 'ṃ': 'ṃ', 'ā': 'ā', 'ī': 'ī', 'ū': 'ū', 'ē': 'e', 'ō': 'o',
        # Handle non-standard "h" after t/th/d/dh (e.g., "kṣhetre" vs "kṣetre")
        'kh': 'k', 'gh': 'g', 'ch': 'c', 'jh': 'j',
        'ṭh': 'ṭ', 'ḍh': 'ḍ', 'th': 't', 'dh': 'd', 'ph': 'p', 'bh': 'b',
    }
    result = text
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result.lower()

def main():
    print("Loading word index...")
    with open("gita_assets/gita_word_index.json", "r", encoding="utf-8") as f:
        word_index = json.load(f)
    print(f"  {len(word_index)} words in index")

    print("\nLoading glossaries...")
    glossary_en = parse_js_dict("gita_assets/raw_data/glossary-en.js", "GLOSSARY_EN")
    print(f"  glossary-en: {len(glossary_en)} entries")

    glossary_hi = parse_js_dict("gita_assets/raw_data/glossary-hi.js", "GLOSSARY_HI")
    print(f"  glossary-hi: {len(glossary_hi)} entries")

    glossary_db = parse_js_dict("gita_assets/raw_data/glossary-db.js", "GLOSSARY_DB")
    print(f"  glossary-db: {len(glossary_db)} entries")

    # Build lookup sets with multiple keys per entry
    print("\nBuilding lookup indexes...")

    # glossary_hi: Devanagari keys → meaning
    hi_lookup = {}  # Devanagari word → meaning
    for key, value in glossary_hi.items():
        # Keys are Devanagari
        hi_lookup[key.strip()] = value
        # Also store without final visarga/anusvara
        stripped = key.strip().rstrip('ःंँ')
        if stripped != key.strip():
            hi_lookup[stripped] = value

    # glossary_en: IAST keys → meaning
    en_lookup = {}  # IAST word → meaning
    en_normalized = {}  # normalized IAST → meaning
    for key, value in glossary_en.items():
        en_lookup[key.strip()] = value
        norm = normalize_iast(key.strip())
        en_normalized[norm] = value
        stripped = key.strip().rstrip('ḥṃ')
        if stripped != key.strip():
            en_lookup[stripped] = value
            en_normalized[normalize_iast(stripped)] = value

    # glossary_db: IAST/SLP1 keys → meaning
    db_lookup = {}
    db_normalized = {}
    for key, value in glossary_db.items():
        db_lookup[key.strip()] = value
        db_normalized[normalize_iast(key.strip())] = value

    print(f"  hi_lookup: {len(hi_lookup)} keys")
    print(f"  en_lookup: {len(en_lookup)} keys (+ {len(en_normalized)} normalized)")
    print(f"  db_lookup: {len(db_lookup)} keys (+ {len(db_normalized)} normalized)")

    # ── Cross-reference ──
    print("\nCross-referencing...")
    matched = 0
    unmatched = 0
    crossref = []

    for entry in word_index:
        deva = entry["devanagari"]
        iast = entry["iast"]
        verses = entry.get("verses", [])

        meanings = []

        # Strategy 1: Exact Devanagari match in glossary-hi
        for key in [deva, deva.rstrip('ःंँ')]:
            if key in hi_lookup:
                meanings.append({"source": "hi", "value": hi_lookup[key]})
                break

        # Strategy 2: Exact IAST match in glossary-en
        for key in [iast, iast.rstrip('ḥṃ')]:
            if key in en_lookup:
                meanings.append({"source": "en", "value": en_lookup[key]})
                break

        # Strategy 3: Normalized IAST match in glossary-en
        if not any(m["source"] == "en" for m in meanings):
            norm = normalize_iast(iast)
            if norm in en_normalized:
                meanings.append({"source": "en", "value": en_normalized[norm]})

        # Strategy 4: Exact IAST match in glossary-db
        if iast in db_lookup:
            meanings.append({"source": "db", "value": db_lookup[iast]})
        elif iast.rstrip('ḥṃ') in db_lookup:
            meanings.append({"source": "db", "value": db_lookup[iast.rstrip('ḥṃ')]})
        else:
            norm = normalize_iast(iast)
            if norm in db_normalized:
                meanings.append({"source": "db", "value": db_normalized[norm]})

        # Strategy 5: Try SLP1 lookup in glossary-db
        try:
            slp1 = transliterate(deva, sanscript.DEVANAGARI, sanscript.SLP1)
            if slp1 in db_lookup:
                meanings.append({"source": "db", "value": db_lookup[slp1]})
        except:
            pass

        if meanings:
            matched += 1
        else:
            unmatched += 1

        crossref.append({
            "devanagari": deva,
            "iast": iast,
            "verses": verses,
            "occurrences": entry.get("count", len(verses)),
            "meanings": meanings,
            "has_meaning": len(meanings) > 0
        })

    # Write output
    with open("gita_assets/gita_crossref.json", "w", encoding="utf-8") as f:
        json.dump(crossref, f, ensure_ascii=False, indent=2)

    # Console summary
    print(f"\n=== Cross-reference Summary ===")
    print(f"Total words: {len(crossref)}")
    print(f"Matched: {matched} ({100*matched/len(crossref):.1f}%)")
    print(f"Unmatched: {unmatched} ({100*unmatched/len(crossref):.1f}%)")

    # Show sample matched
    print(f"\nSample matched entries:")
    for entry in crossref[:5]:
        if entry["has_meaning"]:
            sources = [m["source"] for m in entry["meanings"]]
            print(f"  {entry['devanagari']} ({entry['iast']}) — sources: {sources}")

    # Show sample unmatched
    print(f"\nSample unmatched entries:")
    shown = 0
    for entry in crossref:
        if not entry["has_meaning"] and shown < 10:
            print(f"  {entry['devanagari']} ({entry['iast']})")
            shown += 1

    print(f"\n✓ gita_crossref.json created")

if __name__ == "__main__":
    main()