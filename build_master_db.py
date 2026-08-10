import json
import os
import glob

def compile_nouns(generated_dir):
    """Parses the generated noun tables using a memory cache."""
    master_db = {}
    index_file = os.path.join(generated_dir, "shabd-index.json")
    
    print("Loading Noun Index...")
    with open(index_file, 'r', encoding='utf-8') as f:
        shabd_index = json.load(f)
        
    case_map = {"1": "Nominative", "2": "Accusative", "3": "Instrumental", "4": "Dative", 
                "5": "Ablative", "6": "Genitive", "7": "Locative", "8": "Vocative"}
    number_map = {"sg": "Singular", "du": "Dual", "pl": "Plural"}
    
    table_cache = {}
    total_entries = len(shabd_index)
    print(f"Index loaded. Processing {total_entries} noun entries...")
    
    for count, entry in enumerate(shabd_index, 1):
        if count % 2000 == 0:
            print(f"  ...processed {count}/{total_entries} nouns...")
            
        base_word = entry.get("deva", "Unknown")
        gender = entry.get("gender", "Unknown").capitalize()
        meaning = entry.get("meaning") or entry.get("artha") or "Unknown"
        
        table_path = os.path.join(generated_dir, entry.get("tableFile", ""))
        
        if table_path not in table_cache:
            if os.path.exists(table_path):
                with open(table_path, 'r', encoding='utf-8') as tf:
                    table_cache[table_path] = json.load(tf)
            else:
                table_cache[table_path] = {}
                
        table_data = table_cache[table_path]
        word_data = table_data.get(entry.get("id"), {})
        forms = word_data.get("forms", {})
        
        for case_num, num_dict in forms.items():
            case_name = case_map.get(str(case_num), f"Case {case_num}")
            
            for num_key, num_name in number_map.items():
                for form_obj in num_dict.get(num_key, []):
                    deva_form = form_obj.get("deva", "").strip()
                    if deva_form:
                        master_db[deva_form] = {
                            "pos": f"Noun, {gender} ({case_name}, {num_name}) [Base: {base_word}]",
                            "meaning": meaning,
                            "split": [deva_form]
                        }
                        
    print(f"Extracted {len(master_db)} noun forms.")
    return master_db

def compile_verbs(raw_dir):
    """Parses raw dhatu metadata and all conjugation/krut text files."""
    master_db = {}
    data_file = os.path.join(raw_dir, "data.txt")
    
    print("\nLoading Verb Metadata...")
    with open(data_file, 'r', encoding='utf-8') as f:
        dhatu_metadata = json.load(f)
        
    root_lookup = {}
    for entry in dhatu_metadata.get("data", []):
        root_lookup[entry["baseindex"]] = {
            "root": entry["dhatu"],
            "meaning": entry.get("artha_english") or entry.get("artha_hindi") or "Unknown",
            "pada": "Parasmaipada" if entry.get("pada") == "P" else "Atmanepada"
        }
        
    persons = ["3rd Person", "2nd Person", "1st Person"]
    numbers = ["Singular", "Dual", "Plural"]
    lakara_names = {"lat": "Lat", "lit": "Lit", "lut": "Lut", "lrut": "Lrt", "lot": "Lot", 
                    "lang": "Lang", "vidhiling": "Vidhiling", "ashirling": "Ashirling", 
                    "lung": "Lung", "lrung": "Lrng"}
    avyaya_suffixes = ["क्त्वा", "ल्यप्", "तुमुन्", "णमुल्"]
    
    verb_files = glob.glob(os.path.join(raw_dir, "dhatuforms_vidyut_*.txt"))
    
    print(f"Processing {len(verb_files)} verb files...")
    for v_file in verb_files:
        is_krut = "krut" in v_file.lower()
        with open(v_file, 'r', encoding='utf-8') as f:
            try:
                forms_data = json.load(f)
            except json.JSONDecodeError:
                continue
                
        for base_index, forms_dict in forms_data.items():
            if base_index not in root_lookup:
                continue
            root_info = root_lookup[base_index]
            
            if is_krut:
                for suffix, forms_string in forms_dict.items():
                    for group in forms_string.split(";"):
                        parts = group.split(",")
                        if len(parts) >= 4:
                            stem = parts[0].strip()
                            masc, fem, neut = parts[1].strip(), parts[2].strip(), parts[3].strip()
                            if suffix in avyaya_suffixes:
                                if stem:
                                    master_db[stem] = {
                                        "pos": f"Indeclinable Participle ({suffix}) [Root: {root_info['root']}]",
                                        "meaning": root_info['meaning'],
                                        "split": [stem]
                                    }
                            else:
                                for form, gender in [(masc, "Masculine"), (fem, "Feminine"), (neut, "Neuter")]:
                                    if form:
                                        for sub_form in form.split("/"):
                                            master_db[sub_form] = {
                                                "pos": f"Noun/Adj, {gender} (Nom, Sg) - Krut: {suffix} [Root: {root_info['root']}]",
                                                "meaning": root_info['meaning'],
                                                "split": [sub_form]
                                            }
            else:
                for lakara_code, forms_string in forms_dict.items():
                    pure_lakara = lakara_code[1:] if lakara_code[0] in ['p', 'a'] else lakara_code
                    lakara_display = lakara_names.get(pure_lakara, pure_lakara.capitalize())
                    forms_list = forms_string.split(";")
                    if len(forms_list) == 9:
                        idx = 0
                        for person in persons:
                            for number in numbers:
                                raw_slot = forms_list[idx].strip()
                                for variant in raw_slot.split(","):
                                    clean_form = variant.strip()
                                    if clean_form:
                                        master_db[clean_form] = {
                                            "pos": f"Verb, Root '{root_info['root']}' {root_info['pada']} ({lakara_display}, {person}, {number})",
                                            "meaning": root_info['meaning'],
                                            "split": [clean_form]
                                        }
                                idx += 1
                                
    print(f"Extracted {len(master_db)} verb and krut forms.")
    return master_db

def compile_avyayas(raw_dir):
    """Parses avyayas.txt to include indeclinables."""
    avyaya_db = {}
    filepath = os.path.join(raw_dir, "avyayas.txt")
    if not os.path.exists(filepath):
        print("No avyayas.txt found. Skipping.")
        return avyaya_db
        
    print("\nLoading Avyayas...")
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.strip()
            if not line_str or ("-" not in line_str):
                continue
            parts = line_str.split("-", 1)
            sanskrit_word = parts[0].replace(";", "").strip()
            meaning = parts[1].strip()
            if sanskrit_word:
                avyaya_db[sanskrit_word] = {
                    "pos": "Avyaya (Indeclinable)",
                    "meaning": meaning,
                    "split": [sanskrit_word]
                }
    print(f"Extracted {len(avyaya_db)} avyayas.")
    return avyaya_db

def merge_databases(*databases):
    """
    Safely merges databases. If a word exists in multiple categories 
    (e.g., both noun and verb), it stores all tags in a list instead of overwriting.
    """
    merged_db = {}
    for db in databases:
        for word, properties in db.items():
            if word not in merged_db:
                merged_db[word] = []
            if properties not in merged_db[word]:
                merged_db[word].append(properties)
    return merged_db

if __name__ == "__main__":
    generated_dir = os.path.join("data", "generated")
    raw_dir = os.path.join("data", "raw")
    output_file = "analyzer_db.json"
    
    print("--- Starting Database Compilation ---")
    nouns_db = compile_nouns(generated_dir)
    verbs_db = compile_verbs(raw_dir)
    avyaya_db = compile_avyayas(raw_dir)
    
    print("\n--- Safely Merging Databases ---")
    master_analyzer_db = merge_databases(nouns_db, verbs_db, avyaya_db)
    
    print(f"Final unique keys: {len(master_analyzer_db)}")
    print(f"Saving to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as out_file:
         json.dump(master_analyzer_db, out_file, ensure_ascii=False, indent=2)
    print("Success!")