const fs = require('fs');
const vm = require('vm');

// Create a safe sandbox with a simulated 'window' object
const sandbox = { window: {} };
vm.createContext(sandbox);

// Map your original JS files to their window keys and desired JSON outputs
const filesToConvert = [
    { in: 'glossary-db.js', key: 'GLOSSARY_DB', out: 'glossary.json' },
    { in: 'pratyahara-db.js', key: 'PRATYAHARA_DB', out: 'pratyahara.json' },
    { in: 'sutras-1-1.js', key: 'SUTRAS_1_1', out: 'sutras-1-1.json' },
    { in: 'sutras-1-2.js', key: 'SUTRAS_1_2', out: 'sutras-1-2.json' }
];

filesToConvert.forEach(file => {
    if (fs.existsSync(file.in)) {
        // Read the JS file
        const code = fs.readFileSync(file.in, 'utf8');
        
        // Execute it inside our sandbox
        vm.runInContext(code, sandbox);
        
        // Extract the data and stringify it to strict JSON
        const data = sandbox.window[file.key];
        fs.writeFileSync(file.out, JSON.stringify(data, null, 4));
        
        console.log(`✅ Successfully converted ${file.in} -> ${file.out}`);
    } else {
        console.log(`⚠️ Warning: ${file.in} not found in the directory.`);
    }
});