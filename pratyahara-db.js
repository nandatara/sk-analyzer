window.PRATYAHARA_DB = [
  {
    id: "ac",
    devanagari: "अच्",
    iast: "ac",
    slp1: "ac",
    members: ["अ", "इ", "उ", "ऋ", "ऌ", "ए", "ओ", "ऐ", "औ"],
    meaning: "All vowels."
  },
  {
    id: "hal",
    devanagari: "हल्",
    iast: "hal",
    slp1: "hal",
    members: ["ह", "य", "व", "र", "ल", "ञ", "म", "ङ", "ण", "न", "झ", "भ", "घ", "ढ", "ध", "ज", "ब", "ग", "ड", "द", "ख", "फ", "छ", "ठ", "थ", "च", "ट", "त", "क", "प", "श", "ष", "स"],
    meaning: "All consonants."
  },
  {
    id: "ik",
    devanagari: "इक्",
    iast: "ik",
    slp1: "ik",
    members: ["इ", "उ", "ऋ", "ऌ"],
	aliases: ["i", "u", "r", "l", "ri", "li", "lri", "x", "ऋ", "ऌ"],
    meaning: "The vowels इ, उ, ऋ, ऌ."
  },
{
  id: "yaR",
  devanagari: "यण्",
  iast: "yaṇ",
  slp1: "yaR",
  members: ["य्", "व्", "र्", "ल्"],
  aliases: ["y", "v", "r", "l", "ya", "va", "ra", "la", "य", "व", "र", "ल"],
  meaning: "The semivowels य्, व्, र्, ल्."
},
{
  id: "aR",
  devanagari: "अण्",
  iast: "aṇ",
  slp1: "aR",
  members: ["अ", "इ", "उ"],
  aliases: ["a", "i", "u", "अ", "इ", "उ", "an", "aṇ"],
  meaning: "The vowels अ, इ, उ. In 1.1.51, the practically relevant substitute is the अ-class substitute selected for ऋ."
},
{
  id: "aR_short",
  devanagari: "अण्",
  iast: "aṇ",
  slp1: "aR",
  members: ["अ", "इ", "उ"],
  aliases: ["aR", "an", "aṇ", "a", "i", "u", "अ", "इ", "उ"],
  meaning: "The short अण् pratyāhāra from अ to the first ण्: अ, इ, उ."
},

{
  id: "aR_long",
  devanagari: "अण्",
  iast: "aṇ",
  slp1: "aR",
  members: ["अ", "इ", "उ", "ऋ", "ऌ", "ए", "ओ", "ऐ", "औ", "ह्", "य्", "व्", "र्", "ल्"],
  aliases: ["aR", "an", "aṇ", "अण्", "long aR", "long an"],
  meaning: "The longer अण् pratyāhāra from अ to the second ण्: vowels plus ह्, य्, व्, र्, ल्."
},
{
  id: "al",
  devanagari: "अल्",
  iast: "al",
  slp1: "al",
  members: [
    "अ", "इ", "उ", "ऋ", "ऌ",
    "ए", "ओ", "ऐ", "औ",
    "ह्", "य्", "व्", "र्", "ल्",
    "ञ्", "म्", "ङ्", "ण्", "न्",
    "झ्", "भ्",
    "घ्", "ढ्", "ध्",
    "ज्", "ब्", "ग्", "ड्", "द्",
    "ख्", "फ्", "छ्", "ठ्", "थ्",
    "च्", "ट्", "त्",
    "क्", "प्",
    "श्", "ष्", "स्",
    "ह्"
  ],
  aliases: [
    "al", "अल्",
    "all sounds", "all phonemes",
    "vowels and consonants"
  ],
  meaning: "All sounds: vowels and consonants."
},
  {
    id: "eN",
    devanagari: "एङ्",
    iast: "eṅ",
    slp1: "eN",
    members: ["ए", "ओ"],
    meaning: "The vowels ए and ओ."
  },
  {
  id: "ec",
  devanagari: "एच्",
  iast: "ec",
  slp1: "ec",
  members: ["ए", "ओ", "ऐ", "औ"],
  aliases: ["e", "o", "ai", "au", "E", "O", "ए", "ओ", "ऐ", "औ"],
  meaning: "The vowels ए, ओ, ऐ, औ."
},
  {
    id: "Ec",
    devanagari: "ऐच्",
    iast: "aic",
    slp1: "Ec",
    members: ["ऐ", "औ"],
    meaning: "The vowels ऐ and औ."
  },
{
  id: "Jal",
  devanagari: "झल्",
  iast: "jhal",
  slp1: "Jal",
  members: ["झ", "भ", "घ", "ढ", "ध", "ज", "ब", "ग", "ड", "द", "ख", "फ", "छ", "ठ", "थ", "च", "ट", "त", "क", "प", "श", "ष", "स"],
  aliases: ["jhal", "Jal", "झल्"],
  meaning: "The pratyāhāra झल्, a major consonant class."
},
{
  id: "jaS",
  devanagari: "जश्",
  iast: "jaś",
  slp1: "jaS",
  members: ["ज्", "ब्", "ग्", "ड्", "द्"],
  aliases: ["jaS", "jash", "jas", "जश्", "j", "b", "g", "D", "d"],
  meaning: "The voiced unaspirated stops ज्, ब्, ग्, ड्, द्."
},
{
  id: "car",
  devanagari: "चर्",
  iast: "car",
  slp1: "car",
  members: ["च्", "ट्", "त्", "क्", "प्", "श्", "ष्", "स्"],
  aliases: ["car", "char", "चर्", "c", "w", "t", "k", "p", "S", "z", "s"],
  meaning: "The sounds च्, ट्, त्, क्, प्, श्, ष्, स्."
},
];