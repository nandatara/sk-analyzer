import json
import re
from indic_transliteration import sanscript

def build_full_tsv(input_file, output_file):
    print(f"📂 Reading {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # 1. Clean the input to ensure valid JSON parsing
    # If data2.txt starts with '"data" : [', wrap it in brackets to make it a valid dictionary
    if raw_text.strip().startswith('"data"'):
        raw_text = "{" + raw_text + "}"
        
    try:
        json_data = json.loads(raw_text)
        entries = json_data.get("data", [])
    except json.JSONDecodeError:
        print("⚠️ Failed to parse JSON. Attempting regex extraction fallback...")
        # Fallback if the file has syntax errors
        entries = []
        words = re.findall(r'"word":\s*"([^"]+)"', raw_text)
        lingas = re.findall(r'"linga":\s*"([^"]+)"', raw_text)
        for w, l in zip(words, lingas):
            entries.append({"word": w, "linga": l})

    # 2. Map Linga abbreviations to Vidyut's required strict enums
    linga_map = {
        "P": "Pum",
        "M": "Pum",  # Just in case Masculine is marked as M
        "S": "Stri",
        "F": "Stri",
        "N": "Napumsaka"
    }

    processed_stems = 0
    skipped_stems = 0

    print("⚙️ Processing stems and transliterating to SLP1...")
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for entry in entries:
            word_dev = entry.get("word", "").strip()
            raw_linga = entry.get("linga", "").strip().upper()
            
            if not word_dev or not raw_linga:
                skipped_stems += 1
                continue
                
            # Transliterate carefully to SLP1
            word_slp1 = sanscript.transliterate(word_dev, sanscript.DEVANAGARI, sanscript.SLP1)
            
            # Resolve gender
            mapped_linga = linga_map.get(raw_linga)
            if not mapped_linga:
                skipped_stems += 1
                continue

            # Write perfectly formatted TSV line
            out_f.write(f"{word_slp1}\t{mapped_linga}\n")
            processed_stems += 1

    print(f"✅ Successfully exported {processed_stems:,} stems to {output_file}")
    if skipped_stems > 0:
        print(f"⚠️ Skipped {skipped_stems:,} invalid or incomplete entries.")

if __name__ == '__main__':
    # Point this at your data source and output the TSV for Rust
    build_full_tsv('data2.txt', 'full_stems.tsv')