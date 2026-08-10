const fs = require('fs');
const path = require('path');
const vm = require('vm');

const RAW_DIR = path.join(__dirname, 'gita_assets', 'raw_data');
const OUTPUT_FILE = path.join(__dirname, 'gita_assets', 'gita_data.json');

const sandbox = {};
vm.createContext(sandbox);

const compiledData = { verses: {}, glossary: {} };
console.log("Starting Gītā data consolidation...\n");

if (fs.existsSync(RAW_DIR)) {
    const files = fs.readdirSync(RAW_DIR);
    
    // 1. Parse JS Files (Overrides & Text)
    const jsFiles = files.filter(f => f.endsWith('.js'));
    jsFiles.forEach(file => {
        const filePath = path.join(RAW_DIR, file);
        let code = fs.readFileSync(filePath, 'utf8');
        
        // Force attachment to the sandbox
        code = code.replace(/\b(const|let|var)\s+([a-zA-Z0-9_]+)\s*=/g, 'this.$2 =');
        
        try {
            vm.runInContext(code, sandbox);
            console.log(`✅ Parsed JS: ${file}`);
        } catch (err) {
            console.log(`⚠️ Error parsing ${file}: ${err.message}`);
        }
    });

    if (sandbox.VERSE_TEXT_OVERRIDES) {
        let verseCount = Object.keys(sandbox.VERSE_TEXT_OVERRIDES).length;
        for (const [verseId, textData] of Object.entries(sandbox.VERSE_TEXT_OVERRIDES)) {
            if (!compiledData.verses[verseId]) compiledData.verses[verseId] = {};
            compiledData.verses[verseId].text = textData;
        }
        console.log(`\n➡️ Extracted Saṃhitā text for ${verseCount} verses.`);
    }

    let overridesFound = 0;
    for (let i = 1; i <= 18; i++) {
        const padded = i.toString().padStart(2, '0');
        const chKey = `WORD_DISPLAY_OVERRIDES_CH${padded}`;
        
        if (sandbox[chKey]) {
            for (const [verseId, overrides] of Object.entries(sandbox[chKey])) {
                if (!compiledData.verses[verseId]) compiledData.verses[verseId] = {};
                compiledData.verses[verseId].overrides = overrides;
                overridesFound++;
            }
        }
    }
    if (overridesFound > 0) console.log(`➡️ Extracted ${overridesFound} grammatical overrides.`);

    // 2. Parse Padapāṭha and Anvaya Text Files
    const padaSaPath = path.join(RAW_DIR, 'pada_sa.txt');
    const padaIastPath = path.join(RAW_DIR, 'pada_iast.txt');
    const anvayaSaPath = path.join(RAW_DIR, 'anvaya_sa.txt');
    const anvayaIastPath = path.join(RAW_DIR, 'anvaya_iast.txt');

    if (fs.existsSync(padaSaPath) && fs.existsSync(anvayaSaPath)) {
        const padaSaLines = fs.readFileSync(padaSaPath, 'utf8').split(/\r?\n/);
        const padaIastLines = fs.existsSync(padaIastPath) ? fs.readFileSync(padaIastPath, 'utf8').split(/\r?\n/) : [];
        const anvayaSaLines = fs.readFileSync(anvayaSaPath, 'utf8').split(/\r?\n/);
        const anvayaIastLines = fs.existsSync(anvayaIastPath) ? fs.readFileSync(anvayaIastPath, 'utf8').split(/\r?\n/) : [];

        let mappedCount = 0;
        
        padaSaLines.forEach((line, index) => {
            const match = line.match(/<pc ref="BG_C(\d+)_V(\d+)">(.*?)<\/pc>/);
            if (match) {
                // Convert 01 -> 1, 05 -> 5 to match the "1:1" ID format
                const chapter = parseInt(match[1], 10);
                const verse = parseInt(match[2], 10);
                const verseId = `${chapter}:${verse}`;
                const padaSaText = match[3].trim();
                
                if (!compiledData.verses[verseId]) compiledData.verses[verseId] = {};
                
                compiledData.verses[verseId].pada_sa = padaSaText;
                compiledData.verses[verseId].anvaya_sa = anvayaSaLines[index] ? anvayaSaLines[index].trim() : "";
                
                if (padaIastLines[index]) {
                    const iastMatch = padaIastLines[index].match(/<pc ref="BG_C\d+_V\d+">(.*?)<\/pc>/);
                    compiledData.verses[verseId].pada_iast = iastMatch ? iastMatch[1].trim() : "";
                }
                
                if (anvayaIastLines[index]) {
                    compiledData.verses[verseId].anvaya_iast = anvayaIastLines[index].trim();
                }
                
                mappedCount++;
            }
        });
        console.log(`➡️ Extracted Pada and Anvaya data for ${mappedCount} verses.`);
    } else {
        console.log(`⚠️ Missing Pada or Anvaya text files in ${RAW_DIR}. Skipping horizontal mapping.`);
    }

    // 3. Parse Glossary
    const possibleGlossaryNames = ['glossary_source.txt', 'glossary-source.txt'];
    for (const gName of possibleGlossaryNames) {
        const gPath = path.join(RAW_DIR, gName);
        if (fs.existsSync(gPath)) {
            const lines = fs.readFileSync(gPath, 'utf8').split(/\r?\n/);
            lines.forEach(line => {
                const match = line.match(/^(.*?)[–\-—](.*)$/); 
                if (match) {
                    compiledData.glossary[match[1].trim()] = match[2].trim();
                }
            });
            console.log(`➡️ Parsed Glossary: ${gName}`);
            break;
        }
    }

    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(compiledData, null, 4));
    console.log(`\n🎉 Success! Unified data saved to: ./gita_assets/gita_data.json`);
} else {
    console.log(`❌ Error: Directory ${RAW_DIR} does not exist.`);
}