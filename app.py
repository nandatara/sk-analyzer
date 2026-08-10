import streamlit as st
import sqlite3
import os
import pandas as pd
import re
import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

st.set_page_config(page_title="Sanskrit Morphological Analyzer", layout="wide")

# --- UI Theme Injection ---
st.markdown("""
<style>
    .stApp { background-color: #F8F0E3; }
    header[data-testid="stHeader"] { background-color: #2B3A55 !important; }
    .streamlit-expanderHeader { background-color: #F0E6D2 !important; color: #2B3A55 !important; border-radius: 8px; font-family: 'Georgia', serif; }
    div[data-testid="stExpander"] { background-color: #FAF4EB !important; border: 1px solid #E8DCC4 !important; border-radius: 8px; }
    .badge-sutra { background-color: #E6B97A; color: #4A3515; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
    .badge-term { background-color: #B5C6D8; color: #1D2A40; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: bold; }
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
    
    # 0. Check Sutras
    cursor.execute('''
        SELECT slp1, typeDisplay, uddeshya, vidheya, meaning, explanation, 
               anuvritti, adhikara, examples, notes 
        FROM sutras WHERE id = ?
    ''', (lookup_token,))
    sutra_result = cursor.fetchone()
    if sutra_result:
        conn.close()
        return {"source": "sutra", "data": sutra_result}
    
    # 1. Check Glossary & Pratyaharas
    cursor.execute('SELECT meaning, members, aliases, iast, slp1 FROM ashtadhyayi WHERE word = ?', (lookup_token,))
    ash_result = cursor.fetchone()
    if ash_result:
        conn.close()
        return {"source": "ashtadhyayi", "data": ash_result}
    
    # 2. Check Primary Engine
    cursor.execute('SELECT pos, meaning FROM dictionary WHERE word = ?', (lookup_token,))
    primary_results = cursor.fetchall()
    if primary_results:
        conn.close()
        return {"source": "primary", "data": primary_results}
        
    # 3. Check Amarakośa Fallback
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

# -----------------------------------------------------------------------------
# Main UI
# -----------------------------------------------------------------------------
st.markdown("<h1 style='color: #2B3A55; font-family: Georgia, serif;'>Sanskrit Morphological Analyzer</h1>", unsafe_allow_html=True)

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
        analysis_results = []
        detailed_views = [] 
        
        for token in tokens:
            lookup_token = token
            if lookup_token.endswith("ं"):
                lookup_token = lookup_token[:-1] + "म्"
                
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

        # -----------------------------------------------------------------------------
        # Render Results
        # -----------------------------------------------------------------------------
        if analysis_results:
            df = pd.DataFrame(analysis_results)
            def color_rows(val):
                if val == '❌ Unknown': return 'background-color: #ffe6e6; color: black;'
                elif val == '⚠️ Synonym Match': return 'background-color: #fff3cd; color: black;'
                elif val == '📘 Technical Term': return 'background-color: #B5C6D8; color: black;'
                elif val == '📜 Sūtra': return 'background-color: #E6B97A; color: black;'
                return 'background-color: #e6ffe6; color: black;' if val == '✅ Recognized' else ''
            
            st.dataframe(df.style.map(color_rows, subset=['Status']), use_container_width=True, hide_index=True)
            
            st.markdown("<h3 style='color: #2B3A55;'>Detailed Breakdown</h3>", unsafe_allow_html=True)
            
            for item in detailed_views:
                if item["status"] == "sutra":
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
                        
                else:
                    with st.expander(f"❌ **{item['word']}** - Unknown"):
                        st.markdown("Word not found in databases.")