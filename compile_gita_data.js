const fs = require('fs');
const path = require('path');

const RAW_DIR = path.join(__dirname, 'gita_assets', 'raw_data');
const OUTPUT_FILE = 'gita_data.json';

function extractObject(fileName, varName) {
    const filePath = path.join(RAW_DIR, fileName);
    if (!fs.existsSync(filePath)) {
        console.log(`⚠️ ${fileName} not found in ${RAW_DIR}.`);
        return {};
    }
    const fileContent = fs.readFileSync(filePath, 'utf8');
    try {
        return new Function(`${fileContent}\nreturn ${varName};`)();
    } catch (error) {
        console.error(`❌ Error parsing ${fileName}:`, error.message);
        return {};
    }
}

console.log("🚀 Initiating Gītā compilation...");

const grammarDb = extractObject('grammar-db.js', 'GRAMMAR_DB');
const glossaryEn = extractObject('glossary-en.js', 'GLOSSARY_EN');
const glossaryHi = extractObject('glossary-hi.js', 'GLOSSARY_HI');
const glossaryDb = extractObject('glossary-db.js', 'GLOSSARY_DB');

// Extract your pristine verse lines
const verseTextDb = extractObject('verse-text-clean.js', 'VERSE_TEXT_OVERRIDES');
console.log(`   -> Extracted ${Object.keys(verseTextDb).length} Saṃhitā verse blocks from verse-text-clean.js`);

const compiledData = { verses: {}, dictionaries: { en: glossaryEn, hi: glossaryHi, philosophical: glossaryDb } };

let verseCount = 0;
for (const [verseId, data] of Object.entries(grammarDb)) {
    compiledData.verses[verseId] = {
        // Automatically injects the clean text arrays for EVERY verse
        text_sa: verseTextDb[verseId] ? verseTextDb[verseId].sa : [],
        text_iast: verseTextDb[verseId] ? verseTextDb[verseId].iast : [],
        
        pada_sa: data.padaccheda_sa ? data.padaccheda_sa.join(" ") : "",
        pada_iast: data.padaccheda ? data.padaccheda.join(" ") : "",
        anvaya_sa: data.anvaya_sa ? data.anvaya_sa.join(" ") : "",
        anvaya_iast: data.anvaya ? data.anvaya.join(" ") : "",
        analysis: data.analysis || {}
    };
    verseCount++;
}

fs.writeFileSync(OUTPUT_FILE, JSON.stringify(compiledData, null, 2), 'utf8');
console.log(`✅ Compilation complete! Data saved to ${OUTPUT_FILE}`);