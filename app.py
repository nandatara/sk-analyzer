import subprocess
import os
import sqlite3
import streamlit as st
import pandas as pd
import re
import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

st.set_page_config(page_title="Sanskrit Morphological Analyzer", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #F8F0E3; font-size: 18px !important; }
    header[data-testid="stHeader"] { background-color: #2B3A55 !important; }
    
    .streamlit-expanderHeader { background-color: #F0E6D2 !important; color: #2B3A55 !important; border-radius: 8px; font-family: 'Georgia', serif; }
    div[data-testid="stExpander"] { background-color: #FAF4EB !important; border: 1px solid #E8DCC4 !important; border-radius: 8px; }
    .badge-sutra { background-color: #E6B97A; color: #4A3515; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
    .badge-term { background-color: #B5C6D8; color: #1D2A40; padding: 4px 10px; border-radius: 12px; font-size: 20px; font-weight: bold; }
    .badge-gita { background-color: #F2C94C; color: #4A3515; padding: 4px 10px; border-radius: 12px; font-size: 20px; font-weight: bold; }
    .badge-philo { background-color: #C1E1C1; color: #1D2A40; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
    
    .devanagari { font-family: 'Sanskrit 2003', 'Noto Sans Devanagari', serif; font-size: 24px !important; }

    .stApp h1 { font-size: 40px !important; }
    .stApp h2 { font-size: 30px !important; }
    .stApp h3 { font-size: 24px !important; }
    .stMarkdown p, .stMarkdown li { font-size: 18px !important; }
    .stApp label, .stApp .stRadio label { font-size: 17px !important; }
    .stApp textarea, .stApp input { font-size: 16px !important; }
    .stApp button { font-size: 16px !important; }
    .stApp .stTabs [data-baseweb="tab"] { font-size: 18px !important; }
    .stApp .stSelectbox label { font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

DB_FILE = "sanskrit_engine.db"

def tokenize_text(text):
    # Now explicitly strips English and Devanagari numbers to keep the table clean
    punctuation_to_strip = "।॥,;:!?()[]{}'\" \n\t\r0123456789०१२३४५६७८९" 
    raw_words = text.split()
    return [word.strip(punctuation_to_strip) for word in raw_words if word.strip(punctuation_to_strip)]

def chop_sandhi_with_rust(word_devanagari):
    """Passes fused text to the Rust segmenter and returns isolated padas."""
    try:
        # 1. Convert to SLP1 for the Rust engine
        word_slp1 = sanscript.transliterate(word_devanagari, sanscript.DEVANAGARI, sanscript.SLP1)
        
        # 2. Call the compiled Rust binary
        # Get the absolute path to the 'tulya' directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Step UP one level into the 'Projects' directory
        projects_dir = os.path.dirname(base_dir)
        
        # Build the absolute path to the Rust executable
        rust_binary_path = os.path.join(projects_dir, "vidyut_exporter", "target", "release", "segmenter.exe")
        
        print(f"🔍 DEBUG [Path]: Looking for Rust binary at: {rust_binary_path}")
        
        result = subprocess.run(
            [rust_binary_path, word_slp1],
            capture_output=True,
            text=True,
            check=True
        )
        
        # 3. Parse the JSON array returned by Rust
        slp1_splits = json.loads(result.stdout.strip())
        
        # 4. Convert back to Devanagari for the UI and DB lookups
        devanagari_splits = [
            sanscript.transliterate(split, sanscript.SLP1, sanscript.DEVANAGARI) 
            for split in slp1_splits
        ]
        
        return devanagari_splits
        
    except Exception as e:
        print(f"Rust Segmentation Error: {e}")
        return [word_devanagari] # Fallback to the original word if the bridge fails

def get_vidyut_analysis(word_devanagari):
    """Translates Devanagari to SLP1 and returns ALL Vidyut matches (verbs and nouns)."""
    try:
        word_slp1 = sanscript.transliterate(word_devanagari, sanscript.DEVANAGARI, sanscript.SLP1)
        
        conn = sqlite3.connect('sanskrit_engine.db')
        cursor = conn.cursor()
        
        results = []
        
        # 1. Fetch ALL Verbal Matches
        cursor.execute("SELECT root, gana, meaning, lakara, purusha, vacana FROM vidyut_verbs WHERE word_slp1 = ?", (word_slp1,))
        v_matches = cursor.fetchall()
        for v in v_matches:
            results.append({
                "type": "verb",
                "Root": v[0],
                "Meaning": v[2],
                "details": f"**Lakāra:** {v[3]} | **Purusha:** {v[4]} | **Vacana:** {v[5]}"
            })
            
        # 2. Fetch ALL Nominal Matches
        cursor.execute("SELECT stem, linga, vibhakti, vacana FROM vidyut_subanta WHERE word_slp1 = ?", (word_slp1,))
        n_matches = cursor.fetchall()
        for n in n_matches:
            results.append({
                "type": "noun",
                "Stem": n[0],
                "details": f"**Liṅga:** {n[1]} | **Vibhakti:** {n[2]} | **Vacana:** {n[3]}"
            })
            
        conn.close()
        
        # Return the list of all matches, or None if the list is empty
        return results if results else None
        
    except Exception as e:
        return None

def query_database(lookup_token):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # ↓↓↓ ADD THIS BLOCK suggested by LUMO ↓↓↓
    is_sutra_id = bool(re.match(r'^\d+\.\d+\.\d+$', lookup_token))
    if is_sutra_id:
        try:
            cursor.execute(
                'SELECT slp1, typeDisplay, uddeshya, vidheya, meaning, '
                'explanation, anuvritti, adhikara, examples, notes '
                'FROM sutras WHERE id = ?',
                (lookup_token,)
            )
            sutra_result = cursor.fetchone()
            if sutra_result:
                conn.close()
                return {"source": "sutra", "data": sutra_result}
        except sqlite3.Error as e:
            print(f"SQLite error in sutra lookup: {e}")
        conn.close()
        return {"source": "none", "data": None}
    # ↑↑↑ END ADDED BLOCK ↑↑↑

    # ... rest of function unchanged ...
    
    # Auto-convert Devanagari to IAST so we can check both scripts against the JS objects
    lookup_iast = transliterate(lookup_token, sanscript.DEVANAGARI, sanscript.IAST)
    
    # 1. Check Philosophical Glossary
    cursor.execute('SELECT meaning FROM glossary_philo WHERE word = ? OR word = ?', (lookup_token, lookup_iast))
    philo_result = cursor.fetchone()
    if philo_result:
        conn.close()
        return {"source": "philo", "data": philo_result}

    # 2. Check English and Hindi Glossaries (Combined Output)
    cursor.execute('SELECT meaning FROM glossary_en WHERE word = ? OR word = ?', (lookup_token, lookup_iast))
    en_res = cursor.fetchone()
    
    cursor.execute('SELECT meaning FROM glossary_hi WHERE word = ? OR word = ?', (lookup_token, lookup_iast))
    hi_res = cursor.fetchone()
    
    if en_res or hi_res:
        meaning_str = ""
        if en_res: meaning_str += f"**EN:** {en_res[0]}  "
        if hi_res: meaning_str += f"**HI:** {hi_res[0]}"
        conn.close()
        return {"source": "gita", "data": [meaning_str.strip()]}
    
    # 3. Check Base Grammatical Engines
    try:
        cursor.execute('SELECT slp1, typeDisplay, uddeshya, vidheya, meaning, explanation, anuvritti, adhikara, examples, notes FROM sutras WHERE id = ?', (lookup_token,))
        sutra_result = cursor.fetchone()
        if sutra_result:
            conn.close()
            return {"source": "sutra", "data": sutra_result}
            
        cursor.execute('SELECT meaning, members, aliases, iast, slp1 FROM ashtadhyayi WHERE word = ?', (lookup_token,))
        ash_result = cursor.fetchone()
        if ash_result:
            conn.close()
            return {"source": "ashtadhyayi", "data": ash_result}
        
        cursor.execute('SELECT pos, meaning FROM dictionary WHERE word = ?', (lookup_token,))
        primary_results = cursor.fetchall()
        if primary_results:
            conn.close()
            return {"source": "primary", "data": primary_results}
            
        cursor.execute('SELECT artha, synonyms, linga FROM amarakosha WHERE word = ?', (lookup_token,))
        amara_result = cursor.fetchone()
        if amara_result:
            conn.close()
            return {"source": "amarakosha", "data": amara_result}
    except:
        pass # Silently pass if base tables haven't been generated yet
        
    conn.close()
    return {"source": "none", "data": None}

def colorize_tags(tag_string):
    tag_string = re.sub(r'(\[Base: .*?\])', r':red[\1]', tag_string)
    tag_string = re.sub(r'(\[Root: .*?\])', r':red[\1]', tag_string)
    tag_string = re.sub(r"(Root '.*?')", r":red[\1]", tag_string)
    tag_string = re.sub(r'(\(.*?\))', r':blue[\1]', tag_string)
    tag_string = tag_string.replace("Noun", ":green[Noun]")
    tag_string = tag_string.replace("Verb", ":green[Verb]")
    tag_string = tag_string.replace("Avyaya (Indeclinable)", ":orange[Avyaya]")
    return tag_string

def process_tokens(tokens):
    analysis_results = []
    detailed_views = [] 
    
    for token in tokens:
        raw_token = token.strip("॥।.,;: ")
        if not raw_token:
            continue

        # 🚀 INTERCEPT SŪTRA IDs FIRST (e.g., 1.1.1) before any sandhi or translation
        import re
        if re.match(r'^\d+\.\d+\.\d+$', raw_token):
            db_response = query_database(raw_token) # Assuming query_database handles the sūtra table lookup
            if db_response and db_response.get("source") == "sutra":
                slp1, typeDisp, udd, vid, meaning, expl, anuv, adhi, examples_str, notes = db_response["data"]
                devanagari_sutra = transliterate(slp1, sanscript.SLP1, sanscript.DEVANAGARI)
                examples_list = json.loads(examples_str) if examples_str else []
                
                analysis_results.append({"Word": raw_token, "Meaning(s)": "Pāṇinian Sūtra", "Status": "📜 Sūtra"})
                detailed_views.append({
                    "word": raw_token, "status": "sutra", "slp1": slp1, "deva": devanagari_sutra,
                    "type": typeDisp, "udd": udd, "vid": vid, "meaning": meaning, 
                    "expl": expl, "anuv": anuv, "adhi": adhi, "examples": examples_list, "notes": notes
                })
                continue # Skip sandhi segmentation and dictionary checks for sūtra IDs!
            
        # 1. Pass the raw token through the Rust Sandhi segmenter
        chopped_padas = chop_sandhi_with_rust(raw_token)
        
        # 2. INNER LOOP: Process each chopped piece individually
        for lookup_token in chopped_padas:
            # Normalization
            if lookup_token.endswith("ं"):
                lookup_token = lookup_token[:-1] + "म्"
                
            # Check Vidyut Engine First
            # ---------------------------------------------------------
            # 2. Check Vidyut Engine First (Now handles multiple matches)
            # ---------------------------------------------------------

            vidyut_results = get_vidyut_analysis(lookup_token)
            
            if vidyut_results:
                for vidyut_data in vidyut_results:
                    if vidyut_data["type"] == "verb":
                        analysis_results.append({
                            "Word": lookup_token, 
                            "Meaning(s)": f"Root: {vidyut_data['Root']} ({vidyut_data.get('Meaning', '')})", 
                            "Status": "⚙️ Vidyut Verb"
                        })
                    else:
                        analysis_results.append({
                            "Word": lookup_token, 
                            "Meaning(s)": f"Stem: {vidyut_data['Stem']}", 
                            "Status": "⚙️ Vidyut Noun"
                        })
                        
                    detailed_views.append({
                        "word": lookup_token, 
                        "status": "vidyut", 
                        "type": vidyut_data["type"],
                        "details": vidyut_data["details"]
                    })
                    
                continue # Skip the rest of the dictionary lookups for this word!
            # ---------------------------------------------------------
            
            # 3. Existing Dictionary Logic
            db_response = query_database(lookup_token)
            
            # Safety check in case the database returns None
            if not db_response:
                analysis_results.append({"Word": lookup_token, "Meaning(s)": "-", "Status": "❌ Unknown"})
                detailed_views.append({"word": lookup_token, "status": "unknown"})
                continue
            
            if db_response["source"] == "philo":
                meaning = db_response["data"][0]
                analysis_results.append({"Word": lookup_token, "Meaning(s)": "Philosophical Concept", "Status": "🌟 Tattva"})
                detailed_views.append({"word": lookup_token, "status": "philo", "meaning": meaning})
                
            elif db_response["source"] == "gita":
                meaning = db_response["data"][0]
                analysis_results.append({"Word": lookup_token, "Meaning(s)": meaning, "Status": "✨ Verse Context"})
                detailed_views.append({"word": lookup_token, "status": "gita", "meaning": meaning})

            elif db_response["source"] == "sutra":
                slp1, typeDisp, udd, vid, meaning, expl, anuv, adhi, examples_str, notes = db_response["data"]
                devanagari_sutra = transliterate(slp1, sanscript.SLP1, sanscript.DEVANAGARI)
                examples_list = json.loads(examples_str) if examples_str else []
                analysis_results.append({"Word": lookup_token, "Meaning(s)": "Pāṇinian Sūtra", "Status": "📜 Sūtra"})
                detailed_views.append({
                    "word": lookup_token, "status": "sutra", "slp1": slp1, "deva": devanagari_sutra,
                    "type": typeDisp, "udd": udd, "vid": vid, "meaning": meaning, 
                    "expl": expl, "anuv": anuv, "adhi": adhi, "examples": examples_list, "notes": notes
                })

            elif db_response["source"] == "ashtadhyayi":
                meaning, members_str, aliases_str, iast, slp1 = db_response["data"]
                aliases_list = json.loads(aliases_str) if aliases_str else []
                members_list = json.loads(members_str) if members_str else []
                analysis_results.append({"Word": lookup_token, "Meaning(s)": meaning, "Status": "📘 Technical Term"})
                detailed_views.append({
                    "word": lookup_token, "status": "ashtadhyayi", "meaning": meaning, 
                    "members": members_list, "aliases": aliases_list, "iast": iast, "slp1": slp1
                })
                
            elif db_response["source"] == "primary":
                pos_list = [row[0] for row in db_response["data"]]
                unique_meanings = " | ".join(set([row[1] for row in db_response["data"]]))
                analysis_results.append({"Word": lookup_token, "Meaning(s)": unique_meanings, "Status": "✅ Recognized"})
                detailed_views.append({"word": lookup_token, "status": "primary", "meanings": unique_meanings, "tags": pos_list})
                
            elif db_response["source"] == "amarakosha":
                artha, synonyms, linga = db_response["data"]
                analysis_results.append({"Word": lookup_token, "Meaning(s)": artha, "Status": "⚠️ Synonym Match"})
                detailed_views.append({"word": lookup_token, "status": "amara", "meanings": artha, "synonyms": synonyms, "linga": linga})
                
            else:
                analysis_results.append({"Word": lookup_token, "Meaning(s)": "-", "Status": "❌ Unknown"})
                detailed_views.append({"word": lookup_token, "status": "unknown"})
                
    return analysis_results, detailed_views

def render_detailed_views(detailed_views):
    for item in detailed_views:
        if item["status"] == "philo":
            with st.expander(f"🌟 **{item['word']}** (Philosophical Term)"):
                st.markdown(f"<span class='badge-philo'>Tattva</span>", unsafe_allow_html=True)
                st.markdown(f"**Explanation:** {item['meaning']}")
                
        elif item["status"] == "gita":
            with st.expander(f"✨ **{item['word']}** (Verse Context)"):
                st.markdown(f"<span class='badge-gita'>Glossary Definition</span>", unsafe_allow_html=True)
                st.markdown(item['meaning'])
                
        elif item["status"] == "sutra":
            with st.expander(f"📜 **Sūtra {item['word']}** - {item['deva']}"):
                st.markdown(f"<span class='badge-sutra'>{item['type']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Devanāgarī:** `{item['deva']}` | **SLP1:** `{item['slp1']}`")
                
                col1, col2 = st.columns(2)
                with col1:
                    if item['udd']: st.markdown(f"**Uddeśya:** {item['udd']}")
                with col2:
                    if item['vid']: st.markdown(f"**Vidheya:** {item['vid']}")
                    
                if item['adhi']: st.markdown(f"**Adhikāra:** {item['adhi']}")
                if item['anuv']: st.markdown(f"**Anuvṛtti:** {item['anuv']}")
                
                st.markdown(f"**Explanation:** {item['expl'] or item['meaning']}")
                
                if item['examples']:
                    st.markdown("**Examples:**")
                    for ex in item['examples']:
                        dev_ex = transliterate(ex.get('slp1', ''), sanscript.SLP1, sanscript.DEVANAGARI)
                        st.markdown(f"- `{dev_ex}` ({ex.get('slp1', '')}): {ex.get('note', '')}")
                        
                if item['notes']:
                    st.info(f"**Notes:** {item['notes']}")
                
        elif item["status"] == "ashtadhyayi":
            with st.expander(f"📘 **{item['word']}** (Technical Term)"):
                st.markdown(f"<span class='badge-term'>Glossary Term</span>", unsafe_allow_html=True)
                st.markdown(f"**Definition:** {item['meaning']}")
                st.caption(f"IAST: {item['iast']} | SLP1: {item['slp1']}")
                
                if item["members"]:
                    st.markdown(f"**Phonemes (Members):** `{'`, `'.join(item['members'])}`")
                if item["aliases"]:
                    st.markdown(f"**Aliases:** `{'`, `'.join(item['aliases'])}`")

        elif item["status"] == "primary":
            with st.expander(f"✅ **{item['word']}** - {item['meanings']}"):
                for tag in item["tags"]:
                    st.markdown(f"- {colorize_tags(tag)}")
                    
        elif item["status"] == "amara":
            with st.expander(f"⚠️ **{item['word']}** (Amarakośa Match)"):
                st.markdown(f"**Meaning:** {item['meanings']} | **Gender:** {item['linga'] or 'N/A'}")
                syn_list = item["synonyms"].split(", ")
                st.markdown(" ".join([f"`{s}`" for s in syn_list]))

        elif item["status"] == "vidyut":
            title = "Vidyut Verb" if item.get("type") == "verb" else "Vidyut Noun"
            with st.expander(f"⚙️ {item['word']} ({title})"):
                st.markdown(f"**Vidyut Morphological Analysis:**")
                st.markdown(item["details"])        
                
        else:
            with st.expander(f"❌ **{item['word']}** - Unknown"):
                st.markdown("Word not found in databases.")

def color_rows(val):
    if val == '❌ Unknown': return 'background-color: #ffe6e6; color: black;'
    elif val == '⚠️ Synonym Match': return 'background-color: #fff3cd; color: black;'
    elif val == '📘 Technical Term': return 'background-color: #B5C6D8; color: black;'
    elif val == '📜 Sūtra': return 'background-color: #E6B97A; color: black;'
    elif val == '✨ Verse Context': return 'background-color: #d1ecf1; color: black;' 
    elif val == '🌟 Tattva': return 'background-color: #e2f0cb; color: black;' 
    return 'background-color: #e6ffe6; color: black;' if val == '✅ Recognized' else ''

st.markdown("<h1 style='color: #2B3A55; font-family: Georgia, serif;'>Sanskrit Morphological Analyzer</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Morphological Analyzer",
    "Gītā Explorer",
    "Aṣṭādhyāyī",
    "Gītā Dictionary",
    "Gītā Statistics",
    "Speaker Analysis",
    "Chapter Browser",
    "Chronological Index"
])

with tab1:
    input_scheme = st.radio("Select Input Script:", ["Devanagari", "IAST", "SLP1"], horizontal=True)
    user_input = st.text_area("Input Text (Enter a word, sentence, or Sūtra ID like 1.1.1):", height=100)

    if st.button("Analyze Text", type="primary"):
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            is_sutra_id = bool(re.match(r'^\d+\.\d+\.\d+$', user_input.strip()))

        if is_sutra_id:
            # ── Sūtra ID path: bypass tokenize/process entirely ──
            sutra_id = user_input.strip()
            result = query_database(sutra_id)
            if result["source"] == "sutra" and result["data"]:
                row = result["data"]
                slp1, typeDisp, udd, vid, meaning, expl, anuv, adhi, examples_str, notes = row
                devanagari_sutra = transliterate(slp1, sanscript.SLP1, sanscript.DEVANAGARI)
                examples_list = json.loads(examples_str) if examples_str else []

                st.markdown(f"### Sūtra {sutra_id}")
                st.markdown(f"**Devanagari:** <span class='devanagari'>{devanagari_sutra}</span>", unsafe_allow_html=True)
                st.markdown(f"**Type:** <span class='devanagari'>{typeDisp}</span>", unsafe_allow_html=True)
                st.markdown(f"**Uddeśya:** <span class='devanagari'>{udd}</span>", unsafe_allow_html=True)
                st.markdown(f"**Vidheya:** <span class='devanagari'>{vid}</span>", unsafe_allow_html=True)
                st.markdown(f"**Meaning:** <span class='devanagari'>{meaning}</span>", unsafe_allow_html=True)
                st.markdown(f"**Explanation:** <span class='devanagari'>{expl}</span>", unsafe_allow_html=True)
                st.markdown(f"**Anuvṛtti:** <span class='devanagari'>{anuv}</span>", unsafe_allow_html=True)
                st.markdown(f"**Adhikāra:** <span class='devanagari'>{adhi}</span>", unsafe_allow_html=True)
                st.markdown(f"**Examples:** <span class='devanagari'>{', '.join(ex.get('word', str(ex)) for ex in examples_list)}</span>", unsafe_allow_html=True)
                st.markdown(f"**Notes:** <span class='devanagari'>{notes}</span>", unsafe_allow_html=True)
            else:
                st.info(f"No sūtra found for ID: {sutra_id}")

        else:
            # ── Normal Sanskrit text path: original logic ──
            if input_scheme == "IAST":
                devanagari_text = transliterate(user_input, sanscript.IAST, sanscript.DEVANAGARI)
            elif input_scheme == "SLP1":
                devanagari_text = transliterate(user_input, sanscript.SLP1, sanscript.DEVANAGARI)
            else:
                devanagari_text = user_input

            tokens = tokenize_text(devanagari_text)
            analysis_results, detailed_views = process_tokens(tokens)

            if analysis_results:
                df = pd.DataFrame(analysis_results)
                st.dataframe(df.style.map(color_rows, subset=['Status']), use_container_width=True, hide_index=True)
                st.markdown("<h3 style='color: #2B3A55;'>Detailed Breakdown</h3>", unsafe_allow_html=True)
                render_detailed_views(detailed_views)

with tab2:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Safely get chapters if gita_verses table exists
    try:
        cursor.execute("SELECT DISTINCT chapter FROM gita_verses ORDER BY chapter")
        chapters = [row[0] for row in cursor.fetchall() if row[0] != 0]
    except sqlite3.OperationalError:
        chapters = []
    
    if chapters:
        col1, col2 = st.columns(2)
        with col1:
            selected_chapter = st.selectbox("Select Chapter", chapters)
        
        cursor.execute("SELECT verse FROM gita_verses WHERE chapter = ? ORDER BY verse", (selected_chapter,))
        verses = [row[0] for row in cursor.fetchall()]
        
        with col2:
            selected_verse = st.selectbox("Select Verse", verses)
            
        verse_id = f"{selected_chapter}:{selected_verse}"
        
       # Pulling the 8 columns, including translations at index 7
        cursor.execute("SELECT text_sa, text_iast, pada_sa, pada_iast, anvaya_sa, anvaya_iast, analysis, translations FROM gita_verses WHERE id = ?", (verse_id,))
        verse_data = cursor.fetchone()
        
        if verse_data:
            raw_sa = verse_data[0]
            raw_iast = verse_data[1]
            pada_sa = verse_data[2]
            pada_iast = verse_data[3]
            anvaya_sa = verse_data[4]
            anvaya_iast = verse_data[5]
            raw_translations = verse_data[7]

            try:
                text_sa_list = json.loads(raw_sa) if raw_sa else []
                if not isinstance(text_sa_list, list): text_sa_list = []
            except: text_sa_list = []

            try:
                text_iast_list = json.loads(raw_iast) if raw_iast else []
                if not isinstance(text_iast_list, list): text_iast_list = []
            except: text_iast_list = []
                
            try:
                translations_list = json.loads(raw_translations) if raw_translations else []
                if not isinstance(translations_list, list): translations_list = []
            except: translations_list = []

            formatted_sa = "<br>".join(text_sa_list) if text_sa_list else pada_sa
            formatted_iast = "<br>".join(text_iast_list) if text_iast_list else pada_iast
            
            # --- SPLIT LAYOUT: Main Content (Left) | Translations (Right) ---
            left_col, right_col = st.columns([1.3, 1]) # Left column slightly wider
            
            with left_col:
                html_card = f"""
                <div style="max-width: 100%; margin: 0 auto 20px auto; background-color: #FDFBF7; border: 1px solid #EAE3D1; box-shadow: 2px 4px 10px rgba(0,0,0,0.05); border-radius: 8px;">
                    <div style="background-color: #002B5B; color: white; padding: 12px 25px; border-radius: 8px 8px 0 0; font-family: 'Segoe UI', sans-serif; font-size: 24px; font-weight: bold;">
                        Bhagavad Gita Chapter {selected_chapter}.
                    </div>
                    <div style="padding: 25px 35px;">
                        <div style="color: #4A235A; font-family: 'Segoe UI', sans-serif; font-size: 18px; font-weight: 600; margin-bottom: 15px;">
                            Verse {selected_verse}.
                        </div>
                        <div style="font-family: 'Sanskrit 2003', 'Mangal', sans-serif; font-size: 26px; line-height: 1.6; color: #111; margin-left: 20px; margin-bottom: 25px;">
                            {formatted_sa}
                        </div>
                        <div style="color: #4A235A; font-family: 'Segoe UI', sans-serif; font-size: 18px; font-weight: 600; margin-bottom: 15px;">
                            Transliteration
                        </div>
                        <div style="font-family: 'Arial Unicode MS', 'Segoe UI', sans-serif; font-size: 20px; line-height: 1.6; color: #111; margin-left: 20px;">
                            {formatted_iast}
                        </div>
                    </div>
                </div>
                """
                st.markdown(html_card, unsafe_allow_html=True)
                
                # Tabs nested inside the left column
                v_tab1, v_tab2 = st.tabs(["Padapāṭha & Anvaya", "Morphology Analyzer"])
                with v_tab1:
                    if anvaya_sa:
                        st.markdown(f"**Anvaya (Prose Order):** {anvaya_sa}")
                        st.markdown(f"*{anvaya_iast}*")
                        st.markdown("<br>", unsafe_allow_html=True)
                    if pada_sa:
                        st.markdown(f"**Padapāṭha (Split Words):** {pada_sa}")
                        st.markdown(f"*{pada_iast}*")
                
                with v_tab2:
                    final_tokens = tokenize_text(pada_sa) if pada_sa else []
                    analysis_results, detailed_views = process_tokens(final_tokens)
                    if analysis_results:
                        df = pd.DataFrame(analysis_results)
                        st.dataframe(df.style.map(color_rows, subset=['Status']), use_container_width=True, hide_index=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                        render_detailed_views(detailed_views)

            with right_col:
                # Build Scrollable HTML Container for Translations
                trans_html = "<div style='height: 700px; overflow-y: auto; padding: 25px; background-color: #FDFBF7; border: 1px solid #EAE3D1; box-shadow: 2px 4px 10px rgba(0,0,0,0.05); border-radius: 8px;'>"
                trans_html += "<h3 style='color: #002B5B; margin-top: 0; font-family: Georgia, serif; border-bottom: 2px solid #EAE3D1; padding-bottom: 15px; margin-bottom: 20px;'>Verse Translations</h3>"
                
                if translations_list:
                    for tr in translations_list:
                        author = tr.get("author", "Unknown Author")
                        lang = tr.get("lang", "").capitalize()
                        text = str(tr.get("text", "")).replace("\n", "<br>")
                        
                        trans_html += "<div style='margin-bottom: 20px;'>"
                        trans_html += f"<div style='font-size: 20px; font-weight: bold; color: #6C3483; text-transform: uppercase; letter-spacing: 0.8px;'>{author} <span style='color:#888;'>• {lang}</span></div>"
                        
                        # 🎨 UPGRADED FONT AND SIZE FOR TRANSLATION TEXT
                        trans_html += f"<div style='font-family: \"Sanskrit 2003\", \"Arial Unicode MS\", sans-serif; font-size: 24px; line-height: 1.6; color: #111; margin-top: 8px;'>{text}</div>"
                        
                        trans_html += "</div>"
                        trans_html += "<hr style='border: none; border-top: 1px dashed #D5CABD; margin: 20px 0;'>"
                else:
                    trans_html += "<div style='color: #666; font-style: italic;'>Translations currently unavailable for this verse.</div>"
                
                trans_html += "</div>"
                st.markdown(trans_html, unsafe_allow_html=True)

    else:
        st.info("No Gītā verses found in the database. Ensure the SQLite database has been built correctly using the new schema.")
    conn.close()

with tab3:
    st.markdown("## Aṣṭādhyāyī Browser")

    adhyaya = st.selectbox("Adhyāya", list(range(1, 9)), key="adhyaya")
    paada = st.selectbox("Pāda", list(range(1, 5)), key="paada")

    if st.button("Load Sūtras", key="load_sutras"):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, slp1, typeDisplay, uddeshya, vidheya, meaning, '
            'explanation, anuvritti, adhikara, examples, notes '
            'FROM sutras WHERE id LIKE ? ORDER BY id',
            (f"{adhyaya}.{paada}.%",)
        )
        rows = cursor.fetchall()
        conn.close()

        # Natural sort by sutra ID
        import re
        rows.sort(key=lambda r: [int(x) for x in r[0].split('.')])

        if rows:
            for row in rows:
                sutra_id, slp1, typeDisp, udd, vid, meaning, expl, anuv, adhi, examples_str, notes = row
                devanagari_sutra = transliterate(slp1, sanscript.SLP1, sanscript.DEVANAGARI)
                examples_list = json.loads(examples_str) if examples_str else []

                with st.expander(f"{sutra_id} — {devanagari_sutra}"):
                    st.markdown(f"### Sūtra {sutra_id}")
                    st.markdown(f"**Devanagari:** <span class='devanagari'>{devanagari_sutra}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Type:** <span class='devanagari'>{typeDisp}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Uddeśya:** <span class='devanagari'>{udd}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Vidheya:** <span class='devanagari'>{vid}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Meaning:** <span class='devanagari'>{meaning}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Explanation:** <span class='devanagari'>{expl}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Anuvṛtti:** <span class='devanagari'>{anuv}</span>", unsafe_allow_html=True)
                    st.markdown(f"**Adhikāra:** <span class='devanagari'>{adhi}</span>", unsafe_allow_html=True)
                    st.markdown("**Examples:**", unsafe_allow_html=True)
                    if examples_list:
                        for ex in examples_list:
                            ex_deva = transliterate(ex["slp1"], sanscript.SLP1, sanscript.DEVANAGARI)
                            st.markdown(f"- <span class='devanagari'><b>{ex_deva}</b></span> ({ex['slp1']}): {ex['note']}", unsafe_allow_html=True)
                    else:
                        st.markdown("None")
                    st.markdown(f"**Notes:** <span class='devanagari'>{notes}</span>", unsafe_allow_html=True)
        else:
            st.info(f"No sūtras found for {adhyaya}.{paada}")

# ═══════════════════════════════════════════════════════════════
# TAB 4: Gītā Dictionary
# ═══════════════════════════════════════════════════════════════
with tab4:
    st.markdown("## Gītā Dictionary")
    st.markdown("Search Sanskrit words from the Bhagavad Gītā with verse references and meanings.")

    conn_gita = sqlite3.connect("gita_analytics.db")
    cursor_gita = conn_gita.cursor()

    search_query = st.text_input("Search word (Devanagari or IAST):", key="gita_dict_search")

    col1, col2 = st.columns(2)
    with col1:
        search_type = st.radio("Search by:", ["Contains", "Exact match"], horizontal=True, key="gita_dict_type")
    with col2:
        only_with_meanings = st.checkbox("Only show words with meanings", key="gita_dict_meanings_only")

    if st.button("Search", key="gita_dict_btn"):
        if search_query.strip():
            q = search_query.strip()
            if search_type == "Exact match":
                cursor_gita.execute(
                    '''SELECT devanagari, iast, verses, occurrence_count, meanings, has_meaning
                       FROM gita_crossref
                       WHERE devanagari = ? OR iast = ?
                       ORDER BY occurrence_count DESC''',
                    (q, q)
                )
            else:
                cursor_gita.execute(
                    '''SELECT devanagari, iast, verses, occurrence_count, meanings, has_meaning
                       FROM gita_crossref
                       WHERE devanagari LIKE ? OR iast LIKE ?
                       ORDER BY occurrence_count DESC
                       LIMIT 100''',
                    (f"%{q}%", f"%{q}%")
                )
        else:
            # Show all, optionally filtered
            if only_with_meanings:
                cursor_gita.execute(
                    '''SELECT devanagari, iast, verses, occurrence_count, meanings, has_meaning
                       FROM gita_crossref WHERE has_meaning = 1
                       ORDER BY devanagari LIMIT 100'''
                )
            else:
                cursor_gita.execute(
                    '''SELECT devanagari, iast, verses, occurrence_count, meanings, has_meaning
                       FROM gita_crossref ORDER BY devanagari LIMIT 100'''
                )

        results = cursor_gita.fetchall()

        if results:
            st.success(f"Found {len(results)} words")
            for row in results:
                deva, iast, verses_json, occ_count, meanings_json, has_meaning = row
                verses = json.loads(verses_json)
                meanings = json.loads(meanings_json) if meanings_json else []

                with st.expander(f"{deva} ({iast}) — {occ_count}x in {len(verses)} verses"):
                    st.markdown(f"<span class='devanagari'><b>{deva}</b></span> ({iast})", unsafe_allow_html=True)
                    st.markdown(f"**Occurrences:** {occ_count}")
                    st.markdown(f"**Verses:** {', '.join(verses[:20])}" + ("..." if len(verses) > 20 else ""))

                    if meanings:
                        for m in meanings:
                            st.markdown(f"**{m['source'].upper()}:** <span class='devanagari'>{m['value']}</span>", unsafe_allow_html=True)
                    else:
                        st.markdown("*No glossary meaning found*")
        else:
            st.info("No matching words found.")

    conn_gita.close()


# ═══════════════════════════════════════════════════════════════
# TAB 5: Gītā Statistics
# ═══════════════════════════════════════════════════════════════
with tab5:
    st.markdown("## Gītā Statistics")

    conn_gita = sqlite3.connect("gita_analytics.db")
    cursor_gita = conn_gita.cursor()

    # Overall stats
    cursor_gita.execute("SELECT COUNT(*) FROM gita_words")
    total_unique = cursor_gita.fetchone()[0]
    cursor_gita.execute("SELECT SUM(occurrence_count) FROM gita_words")
    total_occ = cursor_gita.fetchone()[0]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Unique Words", f"{total_unique:,}")
    with col2:
        st.metric("Total Occurrences", f"{total_occ:,}")
    with col3:
        cursor_gita.execute("SELECT COUNT(*) FROM gita_crossref WHERE has_meaning = 1")
        matched = cursor_gita.fetchone()[0]
        st.metric("Words with Meanings", f"{matched:,} ({100*matched/total_unique:.0f}%)")

    st.markdown("---")

    # Top 10 by frequency
    st.markdown("### Top 10 Most Frequent Words")
    cursor_gita.execute("SELECT devanagari, iast, frequency, rank FROM gita_frequency ORDER BY rank LIMIT 10")
    freq_rows = cursor_gita.fetchall()
    freq_data = [{"rank": r[3], "word": r[0], "iast": r[1], "frequency": r[2]} for r in freq_rows]
    if freq_data:
        import pandas as pd
        df_freq = pd.DataFrame(freq_data)
        df_freq["display"] = df_freq.apply(lambda r: f"{r['word']} ({r['iast']})", axis=1)
        st.bar_chart(df_freq.set_index("display")["frequency"], use_container_width=True)

    st.markdown("---")

    # Top 10 longest words
    st.markdown("### Top 10 Longest Words")
    cursor_gita.execute("SELECT devanagari, iast, length, frequency FROM gita_longest_words ORDER BY length DESC LIMIT 10")
    longest_rows = cursor_gita.fetchall()
    for i, row in enumerate(longest_rows, 1):
        st.markdown(f"{i}. <span class='devanagari'>{row[0]}</span> ({row[1]}) — {row[2]} chars, {row[3]}x", unsafe_allow_html=True)

    conn_gita.close()


# ═══════════════════════════════════════════════════════════════
# TAB 6: Speaker Analysis
# ═══════════════════════════════════════════════════════════════
with tab6:
    st.markdown("## Speaker Analysis")

    conn_gita = sqlite3.connect("gita_analytics.db")
    cursor_gita = conn_gita.cursor()

    # Speaker summary
    st.markdown("### Speakers in the Bhagavad Gītā")
    cursor_gita.execute("SELECT speaker, verse_ids FROM gita_speakers")
    speaker_rows = cursor_gita.fetchall()

    import pandas as pd
    speaker_data = []
    for sp, vids_json in speaker_rows:
        vids = json.loads(vids_json)
        speaker_data.append({"Speaker": sp, "Verses Spoken": len(vids)})
    df_sp = pd.DataFrame(speaker_data)
    st.dataframe(df_sp, use_container_width=True, hide_index=True)
    st.bar_chart(df_sp.set_index("Speaker")["Verses Spoken"], use_container_width=True)

    st.markdown("---")

    # Epithets
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔄 Krishna's Epithets")
        cursor_gita.execute("SELECT devanagari, english, count, explanation FROM gita_epithets WHERE belongs_to = 'Krishna' AND count > 0 ORDER BY count DESC")
        krishna_eps = cursor_gita.fetchall()
        for ep in krishna_eps:
            with st.expander(f"{ep[0]} ({ep[1]}) — {ep[2]}x"):
                st.markdown(f"<span class='devanagari'>{ep[3]}</span>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 🏹 Arjuna's Epithets")
        cursor_gita.execute("SELECT devanagari, english, count, explanation FROM gita_epithets WHERE belongs_to = 'Arjuna' AND count > 0 ORDER BY count DESC")
        arjuna_eps = cursor_gita.fetchall()
        for ep in arjuna_eps:
            with st.expander(f"{ep[0]} ({ep[1]}) — {ep[2]}x"):
                st.markdown(f"<span class='devanagari'>{ep[3]}</span>", unsafe_allow_html=True)

    conn_gita.close()


# ═══════════════════════════════════════════════════════════════
# TAB 7: Chapter Browser
# ═══════════════════════════════════════════════════════════════
with tab7:
    st.markdown("## Chapter Browser")

    conn_gita = sqlite3.connect("gita_analytics.db")
    cursor_gita = conn_gita.cursor()

    # Chapter overview
    cursor_gita.execute("SELECT chapter_number, total_words, unique_words, verses_in_chapter FROM gita_chapters ORDER BY chapter_number")
    ch_rows = cursor_gita.fetchall()
    import pandas as pd
    ch_data = [{"Chapter": r[0], "Verses": r[3], "Total Words": r[1], "Unique Words": r[2]} for r in ch_rows]
    df_ch = pd.DataFrame(ch_data)
    st.dataframe(df_ch, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Select chapter to drill down
    ch_selected = st.selectbox("Select chapter for detailed word list:", list(range(1, 19)), key="ch_browser_select")

    cursor_gita.execute(
        "SELECT word, count, verses FROM gita_chapter_words WHERE chapter_number = ? ORDER BY count DESC LIMIT 50",
        (ch_selected,)
    )
    ch_words = cursor_gita.fetchall()

    if ch_words:
        st.markdown(f"### Chapter {ch_selected} — Top 50 Words")
        word_data = [{"Word": r[0], "Count": r[1], "Verses": ', '.join(json.loads(r[2])[:5])} for r in ch_words]
        df_cw = pd.DataFrame(word_data)
        st.dataframe(df_cw, use_container_width=True, hide_index=True)

    conn_gita.close()


# ═══════════════════════════════════════════════════════════════
# TAB 8: Chronological Index
# ═══════════════════════════════════════════════════════════════
with tab8:
    st.markdown("## Chronological Word Index")
    st.markdown("Words ordered by their first appearance in the Gītā.")

    conn_gita = sqlite3.connect("gita_analytics.db")
    cursor_gita = conn_gita.cursor()

    col1, col2 = st.columns(2)
    with col1:
        start_verse = st.text_input("From verse (e.g., 1:1):", value="1:1", key="chrono_start")
    with col2:
        end_verse = st.text_input("To verse (e.g., 2:10):", value="2:10", key="chrono_end")

    limit = st.slider("Max words to show:", 10, 500, 100, key="chrono_limit")

    if st.button("Browse", key="chrono_btn"):
        def verse_sort_key(v):
            parts = v.split(":")
            return (int(parts[0]), int(parts[1]))

        cursor_gita.execute(
            "SELECT word, first_verse, first_position, total_occurrences, verses FROM gita_chronological"
        )
        all_rows = cursor_gita.fetchall()

        # Filter by verse range
        filtered = []
        for row in all_rows:
            fv = row[1]
            if verse_sort_key(fv) >= verse_sort_key(start_verse) and verse_sort_key(fv) <= verse_sort_key(end_verse):
                filtered.append(row)

        filtered.sort(key=lambda r: (verse_sort_key(r[1]), r[2]))
        filtered = filtered[:limit]

        if filtered:
            st.success(f"Showing {len(filtered)} words from {start_verse} to {end_verse}")
            import pandas as pd
            chrono_data = [{
                "Word": r[0],
                "First Verse": r[1],
                "Position": r[2],
                "Total Occurrences": r[3],
                "All Verses": ', '.join(json.loads(r[4])[:10])
            } for r in filtered]
            df_chrono = pd.DataFrame(chrono_data)
            st.dataframe(df_chrono, use_container_width=True, hide_index=True)
        else:
            st.info("No words found in this range.")

    conn_gita.close()