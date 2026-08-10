import streamlit as st
import sqlite3
import os
import pandas as pd
import re
import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

st.set_page_config(page_title="Sanskrit Morphological Analyzer", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #F8F0E3; }
    header[data-testid="stHeader"] { background-color: #2B3A55 !important; }
    .streamlit-expanderHeader { background-color: #F0E6D2 !important; color: #2B3A55 !important; border-radius: 8px; font-family: 'Georgia', serif; }
    div[data-testid="stExpander"] { background-color: #FAF4EB !important; border: 1px solid #E8DCC4 !important; border-radius: 8px; }
    .badge-sutra { background-color: #E6B97A; color: #4A3515; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
    .badge-term { background-color: #B5C6D8; color: #1D2A40; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
    .badge-gita { background-color: #F2C94C; color: #4A3515; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

DB_FILE = "sanskrit_engine.db"

def tokenize_text(text):
    punctuation_to_strip = "।॥,;:!?()[]{}'\" \n\t\r" 
    raw_words = text.split()
    return [word.strip(punctuation_to_strip) for word in raw_words if word.strip(punctuation_to_strip)]

def query_database(lookup_token):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT slp1, typeDisplay, uddeshya, vidheya, meaning, explanation, anuvritti, adhikara, examples, notes FROM sutras WHERE id = ?', (lookup_token,))
    sutra_result = cursor.fetchone()
    if sutra_result:
        conn.close()
        return {"source": "sutra", "data": sutra_result}
        
    cursor.execute('SELECT meaning FROM gita_glossary WHERE word = ?', (lookup_token,))
    gita_result = cursor.fetchone()
    if gita_result:
        conn.close()
        return {"source": "gita", "data": gita_result}
    
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
    conn.close()
    
    if amara_result:
        return {"source": "amarakosha", "data": amara_result}
        
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

def parse_contextual_meanings(meaning_str):
    if not meaning_str: return {}
    mapping = {}
    pairs = meaning_str.split(';')
    for pair in pairs:
        if '—' in pair:
            parts = pair.split('—', 1)
        elif ' - ' in pair:
            parts = pair.split(' - ', 1)
        else:
            continue
            
        if len(parts) >= 2:
            raw_iast = parts[0].strip()
            meaning = parts[1].strip()
            
            clean_iast = raw_iast.replace('kṣh', 'kṣ')
            clean_iast = clean_iast.replace('śht', 'ṣṭ') 
            clean_iast = clean_iast.replace('śh', 'ś')
            clean_iast = clean_iast.replace('sh', 'ṣ')
            clean_iast = clean_iast.replace('ch', 'c')
            clean_iast = clean_iast.replace('ṛi', 'ṛ')
            
            try:
                # 1. Convert to Devanagari keeping hyphens 
                deva_key_hyphenated = transliterate(clean_iast, sanscript.IAST, sanscript.DEVANAGARI)
                # 2. Create a second version without hyphens 
                deva_key_solid = deva_key_hyphenated.replace("-", "")
                
                # Map BOTH versions to the dictionary
                mapping[deva_key_hyphenated] = meaning
                mapping[deva_key_solid] = meaning
            except:
                mapping[raw_iast] = meaning 
    return mapping

# --- UPDATED FUNCTION SIGNATURE (Fixes the Line 344 Error) ---
def process_tokens(tokens, contextual_dict=None):
    if contextual_dict is None:
        contextual_dict = {}
        
    analysis_results = []
    detailed_views = [] 
    
    for token in tokens:
        lookup_token = token
        if lookup_token.endswith("ं"):
            lookup_token = lookup_token[:-1] + "म्"
            
        if token in contextual_dict:
            meaning = contextual_dict[token]
            analysis_results.append({"Word": token, "Meaning(s)": meaning, "Status": "✨ Verse Context"})
            detailed_views.append({"word": token, "status": "contextual", "meaning": meaning})
            continue
        elif lookup_token in contextual_dict:
            meaning = contextual_dict[lookup_token]
            analysis_results.append({"Word": token, "Meaning(s)": meaning, "Status": "✨ Verse Context"})
            detailed_views.append({"word": token, "status": "contextual", "meaning": meaning})
            continue
            
        db_response = query_database(lookup_token)
        
        if db_response["source"] == "sutra":
            slp1, typeDisp, udd, vid, meaning, expl, anuv, adhi, examples_str, notes = db_response["data"]
            devanagari_sutra = transliterate(slp1, sanscript.SLP1, sanscript.DEVANAGARI)
            examples_list = json.loads(examples_str) if examples_str else []
            analysis_results.append({"Word": token, "Meaning(s)": "Pāṇinian Sūtra", "Status": "📜 Sūtra"})
            detailed_views.append({
                "word": token, "status": "sutra", "slp1": slp1, "deva": devanagari_sutra,
                "type": typeDisp, "udd": udd, "vid": vid, "meaning": meaning, 
                "expl": expl, "anuv": anuv, "adhi": adhi, "examples": examples_list, "notes": notes
            })
            
        elif db_response["source"] == "gita":
            meaning = db_response["data"][0]
            analysis_results.append({"Word": token, "Meaning(s)": meaning, "Status": "🕉️ Gītā Glossary"})
            detailed_views.append({"word": token, "status": "gita", "meaning": meaning})

        elif db_response["source"] == "ashtadhyayi":
            meaning, members_str, aliases_str, iast, slp1 = db_response["data"]
            aliases_list = json.loads(aliases_str) if aliases_str else []
            members_list = json.loads(members_str) if members_str else []
            analysis_results.append({"Word": token, "Meaning(s)": meaning, "Status": "📘 Technical Term"})
            detailed_views.append({
                "word": token, "status": "ashtadhyayi", "meaning": meaning, 
                "members": members_list, "aliases": aliases_list, "iast": iast, "slp1": slp1
            })
            
        elif db_response["source"] == "primary":
            pos_list = [row[0] for row in db_response["data"]]
            unique_meanings = " | ".join(set([row[1] for row in db_response["data"]]))
            analysis_results.append({"Word": token, "Meaning(s)": unique_meanings, "Status": "✅ Recognized"})
            detailed_views.append({"word": token, "status": "primary", "meanings": unique_meanings, "tags": pos_list})
            
        elif db_response["source"] == "amarakosha":
            artha, synonyms, linga = db_response["data"]
            analysis_results.append({"Word": token, "Meaning(s)": artha, "Status": "⚠️ Synonym Match"})
            detailed_views.append({"word": token, "status": "amara", "meanings": artha, "synonyms": synonyms, "linga": linga})
            
        else:
            analysis_results.append({"Word": token, "Meaning(s)": "-", "Status": "❌ Unknown"})
            detailed_views.append({"word": token, "status": "unknown"})
            
    return analysis_results, detailed_views

def render_detailed_views(detailed_views):
    for item in detailed_views:
        if item["status"] == "contextual":
            with st.expander(f"✨ **{item['word']}** (Verse Context)"):
                st.markdown(f"<span class='badge-gita'>Contextual Definition</span>", unsafe_allow_html=True)
                st.markdown(f"**Meaning:** {item['meaning']}")
                
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
                    
        elif item["status"] == "gita":
            with st.expander(f"🕉️ **{item['word']}** (Gītā Glossary)"):
                st.markdown(f"<span class='badge-gita'>Contextual Definition</span>", unsafe_allow_html=True)
                st.markdown(f"**Meaning:** {item['meaning']}")
                
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
                
        else:
            with st.expander(f"❌ **{item['word']}** - Unknown"):
                st.markdown("Word not found in databases.")

def color_rows(val):
    if val == '❌ Unknown': return 'background-color: #ffe6e6; color: black;'
    elif val == '⚠️ Synonym Match': return 'background-color: #fff3cd; color: black;'
    elif val == '📘 Technical Term': return 'background-color: #B5C6D8; color: black;'
    elif val == '📜 Sūtra': return 'background-color: #E6B97A; color: black;'
    elif val == '🕉️ Gītā Glossary': return 'background-color: #FFF2CC; color: black;'
    elif val == '✨ Verse Context': return 'background-color: #d1ecf1; color: black;' 
    return 'background-color: #e6ffe6; color: black;' if val == '✅ Recognized' else ''

st.markdown("<h1 style='color: #2B3A55; font-family: Georgia, serif;'>Sanskrit Morphological Analyzer</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Morphological Analyzer", "Gītā Explorer"])

with tab1:
    input_scheme = st.radio("Select Input Script:", ["Devanagari", "IAST", "SLP1"], horizontal=True)
    user_input = st.text_area("Input Text (Enter a word, sentence, or Sūtra ID like 1.1.1):", height=100)

    if st.button("Analyze Text", type="primary"):
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            is_sutra_id = bool(re.match(r'^\d+\.\d+\.\d+$', user_input.strip()))
            
            if not is_sutra_id:
                if input_scheme == "IAST":
                    devanagari_text = transliterate(user_input, sanscript.IAST, sanscript.DEVANAGARI)
                elif input_scheme == "SLP1":
                    devanagari_text = transliterate(user_input, sanscript.SLP1, sanscript.DEVANAGARI)
                else:
                    devanagari_text = user_input
            else:
                devanagari_text = user_input.strip()

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
    cursor.execute("SELECT DISTINCT chapter FROM gita_verses ORDER BY chapter")
    chapters = [row[0] for row in cursor.fetchall() if row[0] != 0]
    
    if chapters:
        col1, col2 = st.columns(2)
        with col1:
            selected_chapter = st.selectbox("Select Chapter", chapters)
        
        cursor.execute("SELECT verse FROM gita_verses WHERE chapter = ? ORDER BY verse", (selected_chapter,))
        verses = [row[0] for row in cursor.fetchall()]
        
        with col2:
            selected_verse = st.selectbox("Select Verse", verses)
            
        verse_id = f"{selected_chapter}:{selected_verse}"
        
        cursor.execute("SELECT text_sa, text_iast, overrides, pada_sa, pada_iast, anvaya_sa, anvaya_iast, translation, explanation, word_meanings FROM gita_verses WHERE id = ?", (verse_id,))
        verse_data = cursor.fetchone()
        
        if verse_data:
            text_sa = json.loads(verse_data[0]) if verse_data[0] else []
            overrides = json.loads(verse_data[2]) if verse_data[2] else {}
            pada_sa = verse_data[3]
            pada_iast = verse_data[4]
            anvaya_sa = verse_data[5]
            anvaya_iast = verse_data[6]
            translation = verse_data[7]
            explanation = verse_data[8]
            word_meanings_str = verse_data[9]
            
            img_path = os.path.join("gita_assets", "images", f"ch{selected_chapter}", f"page_{selected_verse + 1}.webp")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"Image not found at path: {img_path}")
            
            st.markdown("---")
            
            if not text_sa:
                st.warning("⚠️ Verse text missing. Please ensure your JavaScript files were parsed correctly.")
            else:
                v_tab1, v_tab2 = st.tabs(["Saṃhitā Pāṭha", "Pada Anvaya & Morphology"])
                
                with v_tab1:
                    for line in text_sa:
                        st.markdown(f"**{line}**")
                        
                    if translation:
                        st.markdown("---")
                        st.markdown(f"**Translation:** {translation}")
                    if explanation:
                        st.info(f"**Explanation:** {explanation}")
                
                with v_tab2:
                    if word_meanings_str:
                        st.markdown("**Contextual Word Meanings:**")
                        st.caption(word_meanings_str)
                        st.markdown("---")
                        
                    if anvaya_sa:
                        st.markdown(f"**Anvaya (Prose Order):** {anvaya_sa}")
                        st.markdown(f"*{anvaya_iast}*")
                        st.markdown("<br>", unsafe_allow_html=True)
                        
                    if pada_sa:
                        st.markdown(f"**Padapāṭha (Split Words):** {pada_sa}")
                        st.markdown(f"*{pada_iast}*")
                        st.markdown("---")
                        
                    final_tokens = []
                    for line in text_sa:
                        line_tokens = tokenize_text(line)
                        for w in line_tokens:
                            if w in overrides:
                                final_tokens.extend(overrides[w].split())
                            else:
                                final_tokens.append(w)
                    
                    contextual_dict = parse_contextual_meanings(word_meanings_str)
                    analysis_results, detailed_views = process_tokens(final_tokens, contextual_dict)
                    
                    if analysis_results:
                        df = pd.DataFrame(analysis_results)
                        st.dataframe(df.style.map(color_rows, subset=['Status']), use_container_width=True, hide_index=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                        render_detailed_views(detailed_views)
    else:
        st.info("No Gītā verses found in the database. Ensure the SQLite database has been built correctly.")
    conn.close()