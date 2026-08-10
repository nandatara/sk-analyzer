window.SUTRAS_1_1 = [
  {
    id: "1.1.1",
    slp1: "vfdDirAdEc",
    slp1Display: "vfdDir AdEc",

    type: "saMjYA",
    typeDisplay: "संज्ञा-सूत्र",
	
	glossary: ["vfdDi", "saMjYA"],

    adhikara: "",
    anuvritti: "",

    uddeshya: "वृद्धि",
    vidheya: "आ, ऐ, औ",

    purpose: "Defines the technical term वृद्धि.",
    explanation: "The sounds आ, ऐ, and औ receive the technical name वृद्धि.",

	examples: [
	  {
		slp1: "A",
		note: "Long ā is called वृद्धि."
	  },
	  {
		slp1: "E",
		note: "The diphthong ai is called वृद्धि."
	  },
	  {
		slp1: "O",
		note: "The diphthong au is called वृद्धि."
	  }
	],	

    related: ["1.1.2"]
  },

  {
    id: "1.1.2",
    slp1: "adeNguRaH",
    slp1Display: "adeN guRaH",

    type: "saMjYA",
    typeDisplay: "संज्ञा-सूत्र",
	
	glossary: ["guRa", "saMjYA"],

    adhikara: "",
    anuvritti: "",

    uddeshya: "गुण",
    vidheya: "अ, ए, ओ",

    purpose: "Defines the technical term गुण.",
    explanation: "The sounds अ, ए, and ओ receive the technical name गुण.",

    examples: [
	  {
		slp1: "a",
		note: "Short a is called गुण."
	  },
	  {
		slp1: "e",
		note: "The vowel e is called गुण."
	  },
	  {
		slp1: "o",
		note: "The vowel o is called गुण."
	  }
	],

    related: ["1.1.1"]
  },
  
    {
    id: "1.1.3",
    slp1: "iko guRavfdDI",
    slp1Display: "iko guRavfdDI",

    type: "pariBAzA",
    typeDisplay: "परिभाषा-सूत्र",
	
	glossary: ["ik", "guRa", "vfdDi", "pariBAzA"],
	
	pratyaharas: ["ik"],

    adhikara: "",
    anuvritti: "",

    uddeshya: "इक्",
    vidheya: "गुण और वृद्धि",

    purpose: "States that when the terms गुण or वृद्धि are used in connection with इक् vowels, the substitution is understood according to the standard vowel scale.",
    explanation: "इक् refers to इ, उ, ऋ, ऌ. Their गुण substitutes are ए, ओ, अर्, अल्; their वृद्धि substitutes are ऐ, औ, आर्, आल्.",

	examples: [
	  {
		slp1: "i -> e / E",
		note: "For इ, गुण is ए and वृद्धि is ऐ."
	  },
	  {
		slp1: "u -> o / O",
		note: "For उ, गुण is ओ and वृद्धि is औ."
	  },
	  {
		slp1: "f -> ar / Ar",
		note: "For ऋ, गुण is अर् and वृद्धि is आर्."
	  },
	  {
		slp1: "x -> al / Al",
		note: "For ऌ, गुण is अल् and वृद्धि is आल्."
	  }
	],
related: ["1.1.4", "1.1.5", "1.1.6"],
  },
  
  {
  id: "1.1.4",
  slp1: "na DAtulopa ArDaDAtuke",
  slp1Display: "na DAtulopa ArDaDAtuke",

  type: "pariBAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: ["DAtu", "lopa", "ArDaDAtuka", "pariBAzA"],

  adhikara: "",
  anuvritti: "गुण-वृद्धि from the previous rule is understood in context.",

  uddeshya: "धातुलोपे आर्धधातुके",
  vidheya: "गुण-वृद्धी न",

  purpose: "Restricts the application of गुण or वृद्धि when a dhātu undergoes elision before an ārdhadhātuka affix.",
  explanation: "When there is lopa of a dhātu in the environment of an ārdhadhātuka affix, the expected गुण or वृद्धि substitution does not take place.",

examples: [
  {
    slp1: "DAtu-lopa",
    note: "If the root is elided, the expected guṇa/vṛddhi is blocked in this context."
  },
  {
    slp1: "ArDaDAtuka",
    note: "The rule applies in the environment of an ārdhadhātuka affix."
  }
],

related: ["1.1.3", "1.1.4", "1.1.6"],
},

{
  id: "1.1.5",
  slp1: "kNiti ca",
  slp1Display: "kNiti ca",

  type: "atiDeSa",
  typeDisplay: "अतिदेश-सूत्र",

  glossary: ["kit", "Nit", "it", "guRa", "vfdDi"],

  adhikara: "",
  anuvritti: "गुण-वृद्धी from 1.1.3 is understood.",

  uddeshya: "कित् / ङित् प्रत्यय",
  vidheya: "गुण-वृद्धि behavior is extended to this environment",

  purpose: "Extends the previous guṇa/vṛddhi principle to contexts involving affixes marked with क् or ङ्.",
  explanation: "When an affix is marked as कित् or ङित्, that marker affects whether guṇa or vṛddhi operations apply. The visible marker is later deleted, but its grammatical effect remains.",

examples: [
  {
    slp1: "kit",
    note: "An affix marked with indicatory क् is called kit."
  },
  {
    slp1: "Nit",
    note: "An affix marked with indicatory ङ् is called ṅit."
  }
],

related: ["1.1.3", "1.1.4", "1.1.6"],
},

{
  id: "1.1.6",
  slp1: "dIDIvevIwAm",
  slp1Display: "dIDI vevI iwAm",

  type: "niyama",
  typeDisplay: "नियम-सूत्र",

  glossary: [
    "dIDI",
    "vevI",
    "iw",
    "guRa",
    "vfdDi"
  ],

  pratyaharas: ["ik"],

  adhikara: "",
  anuvritti: "इको गुणवृद्धी न",

  uddeshya: "दीधी वेवी इटाम्",
  vidheya: "गुणवृद्धी न",

  meaning: "For dīdhī, vevī, and iṭ, the expected guṇa or vṛddhi substitution of an ik vowel is blocked.",

  explanation: "This rule continues the blocking idea from the previous rules. Where guṇa or vṛddhi would otherwise be expected for an ik vowel, it is not applied in connection with dīdhī, vevī, and iṭ. This is a technical exception and should be studied together with 1.1.3, 1.1.4, and 1.1.5.",

  examples: [
    {
      slp1: "dIDI",
      note: "The root dīdhī is included in this exception."
    },
    {
      slp1: "vevI",
      note: "The root vevī is included in this exception."
    },
    {
      slp1: "iw",
      note: "The augment iṭ is included in this exception."
    }
  ],

  related: ["1.1.3", "1.1.4", "1.1.5"],

  notes: "This is a compact technical rule. We can refine the examples later when the app has a fuller dhātu and augment module."
},

{
  id: "1.1.7",
  slp1: "halo'nantarAH saMyogaH",
  slp1Display: "halaH anantarAH saMyogaH",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: ["hal", "anantara", "saMyoga", "saMjYA"],
  pratyaharas: ["hal"],

  adhikara: "",
  anuvritti: "",

  uddeshya: "हलः अनन्तराः",
  vidheya: "संयोग-संज्ञा",

  purpose: "Defines the technical term संयोग.",
  explanation: "When consonants occur immediately next to one another, with no intervening vowel, that group is called संयोग.",

examples: [
  {
    slp1: "kta",
    note: "क् + त् form a consonant cluster."
  },
  {
    slp1: "gna",
    note: "ग् + न् form a संयोग."
  },
  {
    slp1: "stra",
    note: "स् + त् + र् form a larger consonant cluster."
  }
],

  related: []
},

{
  id: "1.1.8",
  slp1: "muKanAsikAvacano'nunAsikaH",
  slp1Display: "muKanAsikAvacanaH anunAsikaH",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: ["muKa", "nAsikA", "vacana", "anunAsika", "saMjYA"],

  adhikara: "",
  anuvritti: "",

  uddeshya: "मुखनासिकावचनः",
  vidheya: "अनुनासिक-संज्ञा",

  purpose: "Defines the technical term अनुनासिक.",
  explanation: "A sound whose articulation involves both the mouth and the nose is called अनुनासिक.",

examples: [
  {
    slp1: "a~",
    note: "A nasalized vowel may be marked with candrabindu."
  },
  {
    slp1: "i~",
    note: "The vowel is pronounced with nasal resonance."
  },
  {
    slp1: "u~",
    note: "The sound passes through both oral and nasal channels."
  }
],

  related: []
},
{
  id: "1.1.9",
  slp1: "tulyAsyaprayatnaM savarRam",
  slp1Display: "tulyAsyaprayatnaM savarRam",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: ["Asya", "prayatna", "savarRa", "saMjYA"],

  adhikara: "",
  anuvritti: "",

  uddeshya: "तुल्यास्यप्रयत्नम्",
  vidheya: "सवर्ण-संज्ञा",

  purpose: "Defines the technical term सवर्ण.",
  explanation: "Sounds that have the same place of articulation and the same articulatory effort are called सवर्ण.",

examples: [
  {
    slp1: "a / A",
    note: "Short and long forms of the same vowel are savarṇa."
  },
  {
    slp1: "i / I",
    note: "Both share the same articulatory basis."
  },
  {
    slp1: "u / U",
    note: "Both share the same articulatory basis."
  }
],

  related: ["1.1.8", "1.1.10"]
},

{
  id: "1.1.10",
  slp1: "nAjJalO",
  slp1Display: "na ac JalO",

  type: "niyama",
  typeDisplay: "नियम-सूत्र",

  glossary: ["ac", "Jal", "savarRa"],
  pratyaharas: ["ac", "Jal"],

  adhikara: "",
  anuvritti: "सवर्णम् from 1.1.9 is understood.",

  uddeshya: "अच् / झल्",
  vidheya: "सवर्ण-संबंध का निषेध",

  purpose: "Limits the scope of the previous definition of सवर्ण.",
  explanation: "Vowels and झल् consonants are not treated as mutually savarṇa, even if some articulatory similarity might otherwise be considered.",

examples: [
  {
    slp1: "a / k",
    note: "A vowel and a consonant are not savarṇa with each other."
  },
  {
    slp1: "i / c",
    note: "The rule prevents treating such vowel-consonant pairs as savarṇa."
  }
],

  related: ["1.1.9"]
},
{
  id: "1.1.11",
  slp1: "IdUdeddivacanaM pragfhyam",
  slp1Display: "It Ut et dvivacanaM pragfhyam",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "pragfhya",
    "dvivacana",
    "It_dvivacana",
    "Ut_dvivacana",
    "et_dvivacana",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "ईत् ऊत् एत् द्विवचनम्",
  vidheya: "प्रगृह्यम्",

  meaning: "Final ī, ū, and e in certain dual forms are called pragṛhya.",

  explanation: "This is a saṃjñā-sūtra. It assigns the technical name pragṛhya to certain dual forms ending in ī, ū, or e. A pragṛhya sound is preserved before a following vowel and resists ordinary vowel sandhi.",

  examples: [
    {
      slp1: "harI etO",
      note: "The final ī of the dual form harī is treated as pragṛhya."
    },
    {
      slp1: "vizRU imO",
      note: "The final ū of the dual form viṣṇū is treated as pragṛhya."
    }
  ],

related: ["1.1.12", "1.1.13", "1.1.14", "1.1.15", "1.1.16", "1.1.17", "1.1.18", "1.1.19"],

  notes: "Pragṛhya is a technical designation used later to block ordinary sandhi."
},
{
  id: "1.1.12",
  slp1: "adaso mAt",
  slp1Display: "adasaH mAt",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "adas",
    "mAt",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "प्रगृह्यम्",

  uddeshya: "अदसः मात्",
  vidheya: "प्रगृह्यम्",

  meaning: "After the m of the pronoun adas, final ī and ū are called pragṛhya.",

  explanation: "This rule extends the pragṛhya designation from 1.1.11. In forms of the pronoun adas, ī and ū following m are treated as pragṛhya. Such forms resist ordinary vowel sandhi with a following vowel.",

  examples: [
    {
      slp1: "amI ISAH",
      note: "The final ī in amī is treated as pragṛhya, so it is preserved before the following vowel."
    },
    {
      slp1: "amU AsAte",
      note: "The final ū in amū is treated as pragṛhya and is preserved before the following vowel."
    }
  ],

related: ["1.1.11", "1.1.13"],

  notes: "This sūtra depends on the continuation of pragṛhyam from 1.1.11."
},
{
  id: "1.1.13",
  slp1: "Se",
  slp1Display: "Se",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "Se",
    "pragfhya",
    "saMjYA",
    "CAndasa"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "प्रगृह्यम्",

  uddeshya: "शे",
  vidheya: "प्रगृह्यम्",

  meaning: "The Vedic form śe is called pragṛhya.",

  explanation: "This rule continues the pragṛhya designation from 1.1.11. The form śe is a Vedic substitute related to case endings. Since it is pragṛhya, it is preserved and does not undergo ordinary vowel sandhi.",

  examples: [
    {
      slp1: "asme indrAbfhaspatI",
      note: "The Vedic form asme contains śe and is treated as pragṛhya before the following vowel."
    },
    {
      slp1: "yuzme iti",
      note: "The Vedic form yuṣme is another example where the śe element is treated as pragṛhya."
    }
  ],

  related: ["1.1.11", "1.1.12"],

  notes: "This is mainly relevant for Vedic usage and can be studied more deeply when we handle chāndasa forms."
},
{
  id: "1.1.14",
  slp1: "nipAta ekAjanAN",
  slp1Display: "nipAtaH ekAc anAN",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "nipAta",
    "ekAc",
    "anAN",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: ["ac"],

  adhikara: "",
  anuvritti: "प्रगृह्यम्",

  uddeshya: "निपातः एकाच् अनाङ्",
  vidheya: "प्रगृह्यम्",

  meaning: "A nipāta consisting of a single vowel, except āṅ, is called pragṛhya.",

  explanation: "This rule continues the pragṛhya designation from 1.1.11. A nipāta that consists of one vowel is treated as pragṛhya, provided it is not āṅ. Because it is pragṛhya, it is preserved before a following vowel and does not undergo ordinary vowel sandhi.",

  examples: [
    {
      slp1: "i indram paSya",
      note: "The single-vowel nipāta i is treated as pragṛhya before the following vowel."
    },
    {
      slp1: "u umeSaH",
      note: "The single-vowel nipāta u is treated as pragṛhya before the following vowel."
    },
    {
      slp1: "A evaM nu manyase",
      note: "Here ā is treated as pragṛhya in the sense of sentence-reference or recollection, not as āṅ."
    }
  ],

related: ["1.1.11", "1.1.12", "1.1.13", "1.1.15"],

  notes: "The exclusion anāṅ is important: not every ā-form is included here."
},
{
  id: "1.1.15",
  slp1: "ot",
  slp1Display: "ot",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "ot",
    "nipAta",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "निपातः प्रगृह्यम्",

  uddeshya: "ओत्",
  vidheya: "प्रगृह्यम्",

  meaning: "A nipāta ending in o is called pragṛhya.",

  explanation: "This rule continues the pragṛhya section. A particle ending in o receives the pragṛhya designation. Because it is pragṛhya, the final o is preserved before a following vowel and does not undergo ordinary vowel sandhi.",

  examples: [
    {
      slp1: "aho ISAH",
      note: "The final o in the particle aho is treated as pragṛhya before the following vowel."
    },
    {
      slp1: "aho ayam",
      note: "The final o is preserved because the particle is pragṛhya."
    }
  ],

related: ["1.1.11", "1.1.14", "1.1.16"],

  notes: "This rule extends the pragṛhya designation to o-ending particles."
},

{
  id: "1.1.16",
  slp1: "sambudDO SAkalyasyetAvanarze",
  slp1Display: "sambudDO SAkalyasya itO anarze",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "sambudDi",
    "SAkalya",
    "itO",
    "anarza",
    "ot",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "ओत् प्रगृह्यम्",

  uddeshya: "सम्बुद्धौ शाकल्यस्य इतौ अनार्षे",
  vidheya: "प्रगृह्यम्",

  meaning: "According to Śākalya, an o-ending vocative is called pragṛhya before iti in non-ṛṣi usage.",

  explanation: "This rule continues the pragṛhya section. From 1.1.15, ot is continued, and from 1.1.11, pragṛhyam is continued. In Śākalya's view, an o-ending vocative is treated as pragṛhya before iti, when the usage is not ārṣa. Therefore the final o is preserved before iti.",

  examples: [
	{
	 slp1: "he vizRo iti",
	 note: "The vocative viṣṇo ends in o. Before iti, according to Śākalya, the final o is treated as pragṛhya."
	},
    {
      slp1: "he vAyo iti",
      note: "The vocative vāyo ends in o and is preserved before iti under this rule."
    }
  ],

related: ["1.1.11", "1.1.15", "1.1.17"],

  notes: "This is a more specialized pragṛhya rule. We keep it conservative for now and can refine examples later if we add a fuller Vedic/ārṣa discussion."
},

{
  id: "1.1.17",
  slp1: "uYaH",
  slp1Display: "uYaH",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "uY",
    "SAkalya",
    "itO",
    "anarza",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "शाकल्यस्य इतौ अनार्षे प्रगृह्यम्",

  uddeshya: "उञः",
  vidheya: "प्रगृह्यम्",

  meaning: "According to Śākalya, the particle uñ is called pragṛhya before iti in non-ārṣa usage.",

  explanation: "This rule continues the pragṛhya designation. The particle uñ, when followed by iti, may be treated as pragṛhya according to Śākalya, in non-ārṣa usage. This means the sound is preserved rather than undergoing ordinary sandhi.",

  examples: [
    {
      slp1: "u iti",
      note: "The particle u is preserved before iti when treated as pragṛhya."
    },
    {
      slp1: "viti",
      note: "This shows the alternate non-pragṛhya result."
    },
    {
      slp1: "Uz iti",
      note: "A nasalized long ū form is mentioned in the traditional discussion."
    }
  ],

related: ["1.1.11", "1.1.16", "1.1.18"],

  notes: "This is a specialized rule in the pragṛhya section. We keep the card conservative and can refine the examples later."
},

{
  id: "1.1.18",
  slp1: "U~",
  slp1Display: "U~",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "U_candrabindu",
    "uY",
    "SAkalya",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "उञः शाकल्यस्य प्रगृह्यम्",

  uddeshya: "ऊँ",
  vidheya: "प्रगृह्यम्",

  meaning: "The nasalized ū substitute of uñ is called pragṛhya according to Śākalya.",

  explanation: "This rule continues the pragṛhya section. The particle uñ may have a nasalized ū substitute. According to Śākalya, this ū form receives the pragṛhya designation. Therefore it is preserved before a following vowel rather than undergoing ordinary sandhi.",

  examples: [
    {
      slp1: "U~ iti",
      note: "The nasalized ū form is treated as pragṛhya before iti."
    }
  ],

related: ["1.1.11", "1.1.17", "1.1.19"],

  notes: "This rule should be studied together with 1.1.17, because it depends on the particle uñ."
},

{
  id: "1.1.19",
  slp1: "IdUtO ca saptamyarTe",
  slp1Display: "It UtO ca saptamyarTe",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "It_saptami",
    "Ut_saptami",
    "saptamyarTa",
    "pragfhya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "प्रगृह्यम्",

  uddeshya: "ईत् ऊतौ सप्तम्यर्थे",
  vidheya: "प्रगृह्यम्",

  meaning: "An ī-ending or ū-ending form used in a locative sense is called pragṛhya.",

  explanation: "This rule continues the pragṛhya designation from 1.1.11. An ī-ending or ū-ending form, when it conveys the meaning of the locative case, is treated as pragṛhya. Therefore its final vowel is preserved before a following vowel and does not undergo ordinary vowel sandhi.",

  examples: [
    {
      slp1: "somo gOrI aDiSritaH",
      note: "The ī-ending form gaurī is used in a locative sense and is treated as pragṛhya."
    },
    {
      slp1: "aDyasyAM mAmakI tanU",
      note: "The ī-ending māmaki and ū-ending tanū are discussed as locative-sense forms under this rule."
    }
  ],

  related: ["1.1.11", "1.1.18"],

  notes: "This rule marks ī-ending and ū-ending forms as pragṛhya when they express a locative meaning."
},

{
  id: "1.1.20",
  slp1: "dADAGvadAp",
  slp1Display: "dA DA Gu adAp",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "dA_root",
    "DA_root",
    "Gu",
    "adAp",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "दा धा अदाप्",
  vidheya: "घु",

  meaning: "The roots dā and dhā, excluding dāp, are called ghu.",

  explanation: "This is a saṃjñā-sūtra. It assigns the technical name ghu to the roots dā and dhā. The expression adāp excludes the root dāp from this designation.",

  examples: [
    {
      slp1: "dA",
      note: "The root dā, meaning 'to give', receives the technical name ghu."
    },
    {
      slp1: "DA",
      note: "The root dhā, meaning 'to place' or 'to put', receives the technical name ghu."
    },
    {
      slp1: "dAp",
      note: "The root dāp is excluded by adāp and is not included under this ghu designation."
    }
  ],

  related: [],

  notes: "This technical designation will matter later when rules refer specifically to ghu roots."
},

{
  id: "1.1.21",
  slp1: "Adyantavadekasmin",
  slp1Display: "Adi anta vat ekasmin",

  type: "atideSa",
  typeDisplay: "अतिदेश-सूत्र",

  glossary: [
    "Adi",
    "anta",
    "vat",
    "eka",
    "atideSa",
    "paribAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "एकस्मिन्",
  vidheya: "आद्यन्तवत्",

  meaning: "A single item is treated as though it had both an initial and a final position.",

  explanation: "This rule gives an atideśa. Some grammatical operations are stated with reference to the beginning or the end of an expression. But when there is only one item, it has no separate first and last member. This rule allows that single item to be treated like an initial item and also like a final item where required.",

  examples: [
    {
      slp1: "AByAm",
      note: "Traditional discussions use forms like ābhyām to show how a single vowel may be treated as final for an operation."
    },
    {
      slp1: "OpagavaH",
      note: "Traditional discussions use forms like aupagavaḥ to show how a single item may be treated as initial for an operation."
    }
  ],

  related: [],

  notes: "This is a powerful interpretive rule. We should revisit it later when rules depending on initial or final position become active."
},

{
  id: "1.1.22",
  slp1: "taraptamapO GaH",
  slp1Display: "tarap tamapO GaH",

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "tarap",
    "tamap",
    "Ga",
    "pratyaya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "तरप् तमपौ",
  vidheya: "घः",

  meaning: "The affixes tarap and tamap are called gha.",

  explanation: "This is a saṃjñā-sūtra. It gives the technical name gha to the affixes tarap and tamap. Later rules can then refer compactly to these affixes by using the term gha.",

  examples: [
    {
      slp1: "kumArI tarA",
      note: "The affix tarap appears in a comparative-type form such as kumārītarā."
    },
    {
      slp1: "kumArI tamA",
      note: "The affix tamap appears in a superlative-type form such as kumārītamā."
    },
    {
      slp1: "brAhmaRI tarA",
      note: "Traditional examples also include forms such as brāhmaṇītarā."
    }
  ],

  related: [],

  notes: "This technical designation will matter later when rules refer to gha-affixes."
},

{
  id: "1.1.23",
  slp1: "bahugaRavatuqati saMKyA",
  slp1Display: "bahu gaRa vatu qati saMKyA",
  
  searchAliases: [
    "bahugaṇavatuḍati",
    "bahuganavatudati",
    "bahugaṇavatuḍati saṃkhyā",
    "bahuganavatudati sankhya"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "bahu",
    "gaRa",
    "vatu",
    "qati",
    "saMKyA",
    "pratyaya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "बहु गण वतु डति",
  vidheya: "संख्या",

  meaning: "The words bahu and gaṇa, and words ending in the affixes vatu and ḍati, are called saṃkhyā.",

  explanation: "This is a saṃjñā-sūtra. It assigns the technical name saṃkhyā to bahu, gaṇa, and forms ending in the affixes vatu and ḍati. Later rules can then refer to this whole class compactly by using the term saṃkhyā.",

  examples: [
    {
      slp1: "bahu",
      note: "The word bahu, meaning 'many', receives the technical name saṃkhyā."
    },
    {
      slp1: "gaRa",
      note: "The word gaṇa, meaning 'group' or 'class', receives the technical name saṃkhyā."
    },
    {
      slp1: "tAvat",
      note: "A word ending in the affix vatu is included under saṃkhyā."
    },
    {
      slp1: "kati",
      note: "A word ending in the affix ḍati is included under saṃkhyā."
    }
  ],

  related: ["1.1.24", "1.1.25"],

  notes: "This starts a small saṃkhyā section. The following rules refine which forms are included."
},

{
  id: "1.1.24",
  slp1: "zRAntA zaw",
  slp1Display: "zRa antA zaw",

  searchAliases: [
    "ṣṇāntā ṣaṭ",
    "snanta sat",
    "ष्णान्ता षट्",
    "ṣāntā nāntā saṃkhyā ṣaṭ"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "zRAnta",
    "zAnta",
    "nAnta",
    "zaw",
    "saMKyA",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "संख्या",
  uddeshya: "ष्णान्ता संख्या",
  vidheya: "षट्",

  meaning: "A saṃkhyā word ending in ṣ or n is called ṣaṭ.",

  explanation: "This rule continues saṃkhyā from 1.1.23. A number-word ending in ṣ or n receives the technical designation ṣaṭ. Later rules can then refer to this class compactly by using the term ṣaṭ.",

  examples: [
    {
      slp1: "zaw",
      note: "The number word ṣaṭ is traditionally included in this ṣaṭ designation."
    },
    {
      slp1: "paYcan",
      note: "The number word pañcan is n-ending in its grammatical form and is included under ṣaṭ."
    },
    {
      slp1: "saptan",
      note: "The number word saptan is another traditional n-ending example."
    }
  ],

  related: ["1.1.23", "1.1.25"],

  notes: "This rule depends on the continuation of saṃkhyā from 1.1.23. The technical term ṣaṭ will become important later in rules such as ṣaḍbhyo luk."
},

{
  id: "1.1.25",
  slp1: "qati ca",
  slp1Display: "qati ca",

  searchAliases: [
    "ḍati ca",
    "dati ca",
    "डति च",
    "ḍati-ending saṃkhyā ṣaṭ"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "qati",
    "ca",
    "zaw",
    "saMKyA",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "संख्या षट्",
  uddeshya: "डति",
  vidheya: "षट्",

  meaning: "A saṃkhyā word ending in the affix ḍati is also called ṣaṭ.",

  explanation: "This rule extends the ṣaṭ designation from 1.1.24. A saṃkhyā word formed with the affix ḍati is also treated as ṣaṭ. Thus the ṣaṭ category includes not only the ṣ- and n-ending number-words of 1.1.24, but also ḍati-ending saṃkhyā words.",

  examples: [
    {
      slp1: "kati",
      note: "The word kati is a ḍati-ending number-word and is included under the ṣaṭ designation."
    },
    {
      slp1: "yati",
      note: "A ḍati-ending form such as yati is included by this extension."
    }
  ],

  related: ["1.1.23", "1.1.24"],

  notes: "This rule is short because most of its meaning comes by anuvṛtti: saṃkhyā from 1.1.23 and ṣaṭ from 1.1.24."
},
{
  id: "1.1.26",
  slp1: "ktaktavatU nizWA",
  slp1Display: "kta ktavatU nizWA",

  searchAliases: [
    "ktaktavatū niṣṭhā",
    "kta ktavatu nishtha",
    "क्तक्तवतू निष्ठा",
    "kta ktavat niṣṭhā",
    "निष्ठा"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "kta",
    "ktavatu",
    "nizWA",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",
  uddeshya: "क्त क्तवतू",
  vidheya: "निष्ठा",

  meaning: "The affixes kta and ktavatu receive the technical designation niṣṭhā.",

  explanation: "This rule gives the technical name niṣṭhā to the two affixes kta and ktavatu. Later rules can then refer to both of them together by using the single term niṣṭhā.",

  examples: [
    {
      slp1: "BU + kta",
      note: "With the affix kta, a form such as bhūta is a niṣṭhā form."
    },
    {
      slp1: "BU + ktavatu",
      note: "With the affix ktavatu, a form such as bhūtavat is also a niṣṭhā form."
    }
  ],

  related: [],

  notes: "The term niṣṭhā is a saṃjñā covering both kta and ktavatu. This becomes important later in rules dealing with past participial formations."
},
{
  id: "1.1.27",
  slp1: "sarvAdIni sarvanAmAni",
  slp1Display: "sarva AdIni sarvanAmAni",

  searchAliases: [
    "sarvādīni sarvanāmāni",
    "sarva adini sarvanamani",
    "सर्वादीनि सर्वनामानि",
    "sarva-ādi sarvanāman",
    "सर्वनाम"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "sarva",
    "Adi",
    "sarvanAman",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",
  uddeshya: "सर्वादीनि",
  vidheya: "सर्वनामानि",

  meaning: "The words beginning with sarva are called sarvanāman, pronouns.",

  explanation: "This rule gives the technical designation sarvanāman to the gaṇa beginning with sarva. In Pāṇinian grammar, sarvanāman is not just an ordinary semantic label meaning pronoun; it is a technical class used by later rules.",

  examples: [
    {
      slp1: "sarva",
      note: "sarva is the first member of the sarvādi group and receives the designation sarvanāman."
    },
    {
      slp1: "viSva",
      note: "viśva is traditionally included in the sarvādi group and is treated as sarvanāman."
    },
    {
      slp1: "anya",
      note: "anya is also included in the traditional sarvādi list and receives the sarvanāman designation."
    }
  ],

related: ["1.1.28", "1.1.29"],

  notes: "This rule depends on a gaṇa-list, the sarvādi-gaṇa. The word ādi indicates a listed group beginning with sarva, not merely every word that happens to begin with sarva."
},
{
  id: "1.1.28",
slp1: "viBAzA diksamAse bahuvrIhO",
slp1Display: "viBAzA dik samAse bahuvrIhO",

  searchAliases: [
    "vibhāṣā diksamāse bahuvrīhau",
    "vibhasha diksamase bahuvrihau",
    "विभाषा दिक्समासे बहुव्रीहौ",
    "dik samasa bahuvrihi",
    "directional bahuvrihi optional sarvanaman"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "viBAzA",
    "dik",
    "samAsa",
    "bahuvrIhi",
    "sarvAdi",
    "sarvanAman",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वादीनि सर्वनामानि",
  uddeshya: "दिक्समासे बहुव्रीहौ सर्वादीनि",
  vidheya: "विभाषा सर्वनामानि",

  meaning: "In a directional bahuvrīhi compound, the sarvādi words are optionally called sarvanāman.",

  explanation: "This rule continues sarvādīni and sarvanāmāni from 1.1.27. When a sarvādi word occurs in a bahuvrīhi compound connected with direction, the sarvanāman designation applies optionally. The word vibhāṣā signals this optionality.",

  examples: [
    {
      slp1: "uttarapUrva",
      note: "A directional compound such as uttarapūrva can be treated optionally under the sarvanāman designation in the relevant bahuvrīhi context."
    },
    {
      slp1: "dakziRottara",
      note: "A compound involving direction words such as dakṣiṇa and uttara illustrates the directional-compound environment."
    }
  ],

  related: ["1.1.27", "1.1.29"],

  notes: "This rule is an optional extension of the sarvanāman designation from 1.1.27. The condition is specifically a dik-samāsa that is also a bahuvrīhi."
},
{
  id: "1.1.29",
  slp1: "na bahuvrIhO",
  slp1Display: "na bahuvrIhO",

  searchAliases: [
    "na bahuvrīhau",
    "na bahuvrihau",
    "न बहुव्रीहौ",
    "not in bahuvrihi",
    "sarvanaman blocked in bahuvrihi"
  ],

  type: "niyama",
  typeDisplay: "निषेध-सूत्र",

  glossary: [
    "na",
    "bahuvrIhi",
    "sarvAdi",
    "sarvanAman"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वादीनि सर्वनामानि",
  uddeshya: "बहुव्रीहौ सर्वादीनि",
  vidheya: "न सर्वनामानि",

  meaning: "In a bahuvrīhi compound, sarvādi words are not called sarvanāman.",

  explanation: "This rule restricts the sarvanāman designation given in 1.1.27. Although sarvādi words normally receive the technical designation sarvanāman, that designation is blocked when they occur in a bahuvrīhi compound. The previous rule, 1.1.28, gives a special optional exception for directional bahuvrīhi compounds.",

  examples: [
    {
      slp1: "priyaviSva",
      note: "In a bahuvrīhi compound such as priyaviśva, the sarvādi member viśva does not receive the sarvanāman designation."
    },
    {
      slp1: "dvyanya",
      note: "In a bahuvrīhi compound involving anya, the sarvanāman designation is blocked by this rule."
    }
  ],

  related: ["1.1.27", "1.1.28", "1.1.30", "1.1.31"],

  notes: "This is a pratiṣedha, a blocking rule. It should be read together with 1.1.27 and 1.1.28: 1.1.27 gives the general sarvanāman designation, 1.1.28 allows it optionally in directional bahuvrīhis, and 1.1.29 blocks it in other bahuvrīhis."
},
{
  id: "1.1.30",
  slp1: "tftIyAsamAse",
  slp1Display: "tftIyA samAse",

  searchAliases: [
    "tṛtīyāsamāse",
    "tritiyasamase",
    "तृतीयासमासे",
    "tṛtīyā samāse",
    "third-case compound sarvanaman"
  ],

  type: "niyama",
  typeDisplay: "नियम-सूत्र",

  glossary: [
    "tftIyA",
    "samAsa",
    "sarvAdi",
    "sarvanAman"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वादीनि सर्वनामानि न बहुव्रीहौ",
  uddeshya: "तृतीयासमासे सर्वादीनि",
  vidheya: "सर्वनामानि",

  meaning: "In a tṛtīyā-samāsa, sarvādi words retain the sarvanāman designation.",

  explanation: "This rule limits the previous prohibition, 1.1.29 न बहुव्रीहौ. Although sarvādi words do not receive the sarvanāman designation in a bahuvrīhi generally, they do receive it in the specific case of a tṛtīyā-samāsa. Here tṛtīyā-samāsa means a compound connected with the instrumental, or third-case, relation.",

  examples: [
    {
      slp1: "mAsapUrva",
      note: "A compound with a prior member standing in a third-case relation illustrates the tṛtīyā-samāsa environment."
    },
    {
      slp1: "sarvapUrva",
      note: "When a sarvādi word occurs in the relevant tṛtīyā-samāsa environment, the sarvanāman designation is retained."
    }
  ],

related: ["1.1.27", "1.1.29", "1.1.31"],

  notes: "This rule should be read with 1.1.27 and 1.1.29. The general designation sarvanāman comes from 1.1.27; 1.1.29 blocks it in bahuvrīhi compounds; 1.1.30 gives a specific exception in the tṛtīyā-samāsa environment."
},
{
  id: "1.1.31",
  slp1: "dvandve ca",
  slp1Display: "dvandve ca",

  searchAliases: [
    "dvandve ca",
    "द्वन्द्वे च",
    "dvandva compound",
    "sarvanaman blocked in dvandva"
  ],

  type: "niyama",
  typeDisplay: "निषेध-सूत्र",

  glossary: [
    "dvandva",
    "ca",
    "sarvAdi",
    "sarvanAman"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वादीनि सर्वनामानि न",
  uddeshya: "द्वन्द्वे सर्वादीनि",
  vidheya: "न सर्वनामानि",

  meaning: "In a dvandva compound also, sarvādi words are not called sarvanāman.",

  explanation: "This rule continues the restriction on the sarvanāman designation. Sarvādi words normally receive the designation sarvanāman by 1.1.27, but in a dvandva compound that designation is blocked. The word ca connects this rule with the previous restrictional sequence.",

  examples: [
    {
      slp1: "pUrvAparA",
      note: "In a dvandva such as pūrvāparā, the sarvādi words pūrva and apara do not receive the sarvanāman designation."
    },
    {
      slp1: "katarakatamA",
      note: "In a dvandva involving words such as katara and katama, the sarvanāman designation is blocked."
    }
  ],

related: ["1.1.27", "1.1.29", "1.1.30", "1.1.32"],

  notes: "This rule should be read with 1.1.27–1.1.30. The general sarvanāman designation is given by 1.1.27, while 1.1.29 and 1.1.31 block it in certain compound environments."
},
{
  id: "1.1.32",
  slp1: "viBAzA jasi",
  slp1Display: "viBAzA jasi",

  searchAliases: [
    "vibhāṣā jasi",
    "vibhasha jasi",
    "विभाषा जसि",
    "jas nominative plural",
    "optional sarvanaman in jas"
  ],

  type: "niyama",
  typeDisplay: "विभाषा-सूत्र",

  glossary: [
    "viBAzA",
    "jas",
    "dvandva",
    "sarvAdi",
    "sarvanAman"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "द्वन्द्वे सर्वादीनि सर्वनामानि न",
  uddeshya: "जसि द्वन्द्वे सर्वादीनि",
  vidheya: "विभाषा न सर्वनामानि",

  meaning: "When jas occurs in a dvandva compound, the blocking of the sarvanāman designation is optional.",

  explanation: "This rule qualifies 1.1.31 द्वन्द्वे च. In a dvandva compound, sarvādi words are generally not called sarvanāman. But when the case ending jas is involved, that prohibition becomes optional. Thus the sarvanāman designation may or may not apply in this jas environment.",

  examples: [
    {
      slp1: "katarakatame",
      note: "One form shows the result when the sarvanāman-related operation applies in the jas environment."
    },
    {
      slp1: "katarakatamAH",
      note: "The alternate form shows the optionality indicated by vibhāṣā in the jas environment."
    }
  ],

related: ["1.1.27", "1.1.31", "1.1.33"],

  notes: "Here jas is the nominative plural case ending. This rule does not create a new sarvanāman class; it makes the previous dvandva restriction optional for jas-related operations."
},
{
  id: "1.1.33",
  slp1: "praTamacaramatayAlpArDakatipayanemASca",
  slp1Display: "praTama carama taya alpa arDa katipaya nemAS ca",

  searchAliases: [
    "prathamacaramatayālpārdhakatipayanemāśca",
    "prathama carama taya alpa ardha katipaya nema ca",
    "प्रथमचरमतयाल्पार्धकतिपयनेमाश्च",
    "प्रथम चरम तय अल्प अर्ध कतिपय नेमाश्च",
    "optional sarvanaman before jas"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "praTama",
    "carama",
    "taya",
    "alpa",
    "arDa",
    "katipaya",
    "nema",
    "ca",
    "jas",
    "viBAzA",
    "sarvanAman",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वनामानि विभाषा जसि",
  uddeshya: "प्रथम चरम तय अल्प अर्ध कतिपय नेमाः",
  vidheya: "विभाषा सर्वनामानि",

  meaning: "The words prathama, carama, taya-ending words, alpa, ardha, katipaya, and nema are optionally called sarvanāman before jas.",

  explanation: "This rule continues sarvanāmāni from 1.1.27 and vibhāṣā jasi from 1.1.32. In the jas environment, these listed words optionally receive the technical designation sarvanāman. This means that sarvanāman-related operations may apply optionally to them before jas.",

  examples: [
    {
      slp1: "praTame / praTamAH",
      note: "For prathama, both prathame and prathamāḥ are possible in the jas environment."
    },
    {
      slp1: "carame / caramAH",
      note: "For carama, the optional sarvanāman designation gives alternate forms."
    },
    {
      slp1: "katipaye / katipayAH",
      note: "For katipaya also, the jas environment allows optional sarvanāman treatment."
    },
    {
      slp1: "neme / nemAH",
      note: "The word nema is specifically included in this optional rule."
    }
  ],

  related: ["1.1.27", "1.1.32", "1.1.34", "1.1.36"],

  notes: "The source list is a dvandva-style enumeration: prathama, carama, taya, alpa, ardha, katipaya, and nema. The carried-over words are sarvanāmāni, vibhāṣā, and jasi."
},
{
  id: "1.1.34",
  slp1: "pUrvaparAvaradakziRottarAparADarARi vyavasTAyAmasaMjYAyAm",
  slp1Display: "pUrva para avara dakziRa uttara apara aDara ARi vyavasTAyAm asaMjYAyAm",

  searchAliases: [
    "pūrvaparāvaradakṣiṇottarāparādharāṇi vyavasthāyāmasaṃjñāyām",
    "purva para avara dakshina uttara apara adhara",
    "पूर्वपरावरदक्षिणोत्तरापराधराणि व्यवस्थायामसंज्ञायाम्",
    "पूर्व पर अवर दक्षिण उत्तर अपर अधर",
    "optional sarvanaman in vyavastha not as samjna"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "pUrva",
    "para",
    "avara",
    "dakziRa",
    "uttara",
    "apara",
    "aDara",
    "vyavasTA",
    "asaMjYA",
    "jas",
    "viBAzA",
    "sarvanAman",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वनामानि विभाषा जसि",
  uddeshya: "पूर्व पर अवर दक्षिण उत्तर अपर अधराणि व्यवस्थायाम् असंज्ञायाम्",
  vidheya: "विभाषा सर्वनामानि",

  meaning: "The words pūrva, para, avara, dakṣiṇa, uttara, apara, and adhara are optionally called sarvanāman before jas, when used for relative position and not as names.",

  explanation: "This rule continues sarvanāmāni, vibhāṣā, and jasi. The listed words, such as pūrva, para, dakṣiṇa, and uttara, optionally receive the sarvanāman designation in the jas environment, but only when they express relative arrangement, direction, order, or position. If one of these words is being used as a name, the rule does not apply.",

  examples: [
    {
      slp1: "pUrve / pUrvAH",
      note: "When pūrva expresses relative position, optional sarvanāman treatment before jas gives alternate forms."
    },
    {
      slp1: "uttare / uttarAH",
      note: "When uttara is used in a relative sense such as northern/later, the optional designation may apply."
    },
    {
      slp1: "dakziRe / dakziRAH",
      note: "When dakṣiṇa expresses relative direction, optional sarvanāman treatment is possible in the jas environment."
    }
  ],

  related: ["1.1.27", "1.1.33", "1.1.35"],

  notes: "The important conditions are vyavasthāyām and asaṃjñāyām: the words must express relative position or arrangement, and they must not be used as names."
},
{
  id: "1.1.35",
slp1: "svamajYAtiDanAKyAyAm",
slp1Display: "svam ajYAti Dana AKyAyAm",

  searchAliases: [
    "svamajñātidhanākhyāyām",
    "svam ajñāti dhana ākhyāyām",
    "स्वमज्ञातिधनाख्यायाम्",
    "स्वम् अज्ञाति धन आख्यायाम्",
    "sva not meaning kinsman or wealth",
    "optional sarvanaman for sva before jas"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "sva",
    "ajYAti",
    "jYAti",
    "dhana",
    "AKyA",
    "jas",
    "viBAzA",
    "sarvanAman",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वनामानि विभाषा जसि",
  uddeshya: "स्वम् अज्ञातिधनाख्यायाम्",
  vidheya: "विभाषा सर्वनाम",

  meaning: "The word sva is optionally called sarvanāman before jas, when it does not denote kinsman or wealth.",

  explanation: "This rule continues sarvanāmāni, vibhāṣā, and jasi. The word sva can mean one’s own, self, kinsman, or property/wealth. Here Pāṇini says that sva optionally receives the sarvanāman designation before jas only when it is not being used as a word for jñāti, kinsman, or dhana, wealth/property.",

  examples: [
    {
      slp1: "sve putrAH / svAH putrAH",
      note: "When sva means 'one’s own', optional sarvanāman treatment before jas gives alternate forms."
    },
    {
      slp1: "sve gAvaH / svAH gAvaH",
      note: "When sva means 'one’s own cows', optional treatment is possible."
    },
    {
      slp1: "svAH jYAtayaH",
      note: "When sva itself denotes kinsmen, the optional sarvanāman designation is excluded."
    }
  ],

  related: ["1.1.27", "1.1.32", "1.1.34"],

  notes: "The key restriction is ajñāti-dhana-ākhyāyām: the rule applies when sva is not used as a designation for kinsman or wealth/property. The carried-over condition is jas, with optionality from vibhāṣā."
},
{
  id: "1.1.36",
  slp1: "antaraM bahiryogopasaMvyAnayoH",
  slp1Display: "antaraM bahiryoga upasaMvyAnayoH",

  searchAliases: [
    "antaraṃ bahiryogopasaṃvyānayoḥ",
    "antaram bahiryogopasamvyanayoh",
    "अन्तरं बहिर्योगोपसंव्यानयोः",
    "अन्तरम् बहिर्योग उपसंव्यानयोः",
    "antara as sarvanaman in bahiryoga and upasamvyana"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "antara",
    "bahiryoga",
    "upasaMvyAna",
    "jas",
    "viBAzA",
    "sarvanAman",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वनामानि विभाषा जसि",
  uddeshya: "अन्तरं बहिर्योगोपसंव्यानयोः",
  vidheya: "विभाषा सर्वनाम",

  meaning: "The word antara is optionally called sarvanāman before jas when it denotes external relation or an under-garment.",

  explanation: "This rule continues sarvanāmāni, vibhāṣā, and jasi. The word antara has many meanings, but in the two specific senses named here — bahiryoga, relation to the outside, and upasaṃvyāna, an under-garment or lower garment — it optionally receives the sarvanāman designation before jas.",

  examples: [
    {
      slp1: "antare / antarAH",
      note: "When antara has the relevant external or garment-related sense, optional sarvanāman treatment before jas gives alternate forms."
    },
    {
      slp1: "antarARi vastrARi",
      note: "In the sense of inner/lower garments, antara is included by this rule."
    }
  ],

  related: ["1.1.27", "1.1.32", "1.1.35"],

  notes: "This is another conditional extension of the sarvanāman designation. The two conditions are bahiryoga and upasaṃvyāna. The carried-over environment is jas, with optionality from vibhāṣā."
},
{
  id: "1.1.37",
  slp1: "svarAdinipAtamavyayam",
  slp1Display: "svarAdi nipAtam avyayam",

  searchAliases: [
    "svarādinipātamavyayam",
    "svaradi nipatam avyayam",
    "स्वरादिनिपातमव्ययम्",
    "स्वरादि निपातम् अव्ययम्",
    "avyaya saṃjñā",
    "indeclinable"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "svarAdi",
    "nipAta",
    "avyaya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "अव्ययम्",
  anuvritti: "",
  uddeshya: "स्वरादि निपातम्",
  vidheya: "अव्ययम्",

  meaning: "The words of the svarādi group and the nipātas are called avyaya.",

  explanation: "This rule gives the technical designation avyaya to two groups: the svarādi-gaṇa and the nipātas. Avyaya means an indeclinable word, one that does not change across gender, case, or number. Later rules can refer to these words compactly by using the term avyaya.",

  examples: [
    {
      slp1: "svar",
      note: "svar is the first member of the svarādi group and is included under the avyaya designation."
    },
    {
      slp1: "antar",
      note: "antar is traditionally listed in the svarādi group and is treated as avyaya."
    },
    {
      slp1: "ca",
      note: "Particles such as ca are nipātas and therefore receive the avyaya designation."
    },
    {
      slp1: "vA",
      note: "vā is another nipāta-type indeclinable."
    }
  ],

related: ["1.1.38"],

  notes: "This starts the avyaya-saṃjñā section. The following rules, beginning with 1.1.38, add more classes to the avyaya designation."
},
{
  id: "1.1.38",
  slp1: "taddhitaScAsarvaviBaktiH",
  slp1Display: "taddhitaH ca asarvaviBaktiH",

  searchAliases: [
    "taddhitaścāsarvavibhaktiḥ",
    "taddhitash ca asarvavibhaktih",
    "तद्धितश्चासर्वविभक्तिः",
    "तद्धितः च असर्वविभक्तिः",
    "taddhita avyaya",
    "asarvavibhakti"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "taddhita",
    "ca",
    "asarvaviBakti",
    "viBakti",
    "avyaya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "अव्ययम्",
  anuvritti: "अव्ययम्",
  uddeshya: "तद्धितः असर्वविभक्तिः",
  vidheya: "अव्ययम्",

  meaning: "A taddhita formation that is asarvavibhakti is called avyaya.",

  explanation: "This rule extends the avyaya designation from 1.1.37. A taddhita form receives the technical designation avyaya when it is asarvavibhakti, meaning it does not take all case endings like a normally declined noun. Such forms behave as indeclinables.",

  examples: [
    {
      slp1: "tatas",
      note: "A taddhita-type indeclinable such as tatas is treated as avyaya."
    },
    {
      slp1: "yatas",
      note: "A similar asarvavibhakti taddhita formation receives the avyaya designation."
    }
  ],

related: ["1.1.37", "1.1.39"],

  notes: "This belongs to the avyaya-saṃjñā section. The word avyayam is carried over from 1.1.37. The condition asarvavibhakti restricts the rule to taddhita forms that do not have a full case-ending paradigm."
},
{
  id: "1.1.39",
  slp1: "kfnmejantaH",
  slp1Display: "kfn m ejantaH",

  searchAliases: [
    "kṛnmejantaḥ",
    "krnmejantah",
    "कृन्मेजन्तः",
    "कृत् म् एजन्तः",
    "krt ending in m or ec",
    "avyaya krt affix"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "kft",
    "makArAnta",
    "ejanta",
    "ec",
    "avyaya",
    "saMjYA"
  ],

  pratyaharas: ["ec"],

  adhikara: "अव्ययम्",
  anuvritti: "अव्ययम्",
  uddeshya: "कृत् मकारान्तः एजन्तः च",
  vidheya: "अव्ययम्",

  meaning: "Kṛt formations ending in m, and kṛt formations ending in eC, are called avyaya.",

  explanation: "This rule continues the avyaya designation from 1.1.37. Certain kṛt formations become indeclinables: those ending in m, and those ending in the eC vowels. The form of the sūtra is compact: kṛnmejantaḥ is understood as referring to kṛt forms that are m-ending and eC-ending.",

  examples: [
    {
      slp1: "svAduMkAram",
      note: "An m-ending kṛt-type formation is treated as avyaya in the relevant usage."
    },
    {
      slp1: "jIvase",
      note: "An e-ending kṛt-type form illustrates the eC-ending side of the rule."
    },
    {
      slp1: "dfSe",
      note: "Another e-ending form treated under the avyaya designation."
    }
  ],

  related: ["1.1.37", "1.1.38", "1.1.40"],

  notes: "The expression ejantaḥ means eC-ending. The pratyāhāra eC includes e, o, ai, and au. This rule belongs to the ongoing avyaya-saṃjñā group."
},
{
  id: "1.1.40",
  slp1: "ktvAtosunkasunaH",
  slp1Display: "ktvA tosun kasunaH",

  searchAliases: [
    "ktvātosunkasunaḥ",
    "ktva tosun kasun",
    "क्त्वातोसुन्कसुनः",
    "क्त्वा तोसुन् कसुन्",
    "avyaya ktva tosun kasun"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "ktvA",
    "tosun",
    "kasun",
    "avyaya",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "अव्ययम्",
  anuvritti: "अव्ययम्",
  uddeshya: "क्त्वा तोसुन् कसुन्",
  vidheya: "अव्ययम्",

  meaning: "The affixes ktvā, tosun, and kasun are called avyaya.",

  explanation: "This rule continues the avyaya designation from 1.1.37. The affixes ktvā, tosun, and kasun form indeclinable expressions, so Pāṇini gives them the technical designation avyaya.",

  examples: [
    {
      slp1: "gatvA",
      note: "A ktvā form such as gatvā is an indeclinable meaning 'having gone'."
    },
    {
      slp1: "BuktvA",
      note: "A ktvā form such as bhuktvā is treated as avyaya."
    },
    {
      slp1: "kartum",
      note: "Infinitive-like indeclinable formations are part of the same broad avyaya discussion, though this example is mainly for comparison."
    }
  ],

related: ["1.1.37", "1.1.39", "1.1.41"],

  notes: "The sūtra is a compact dvandva listing: ktvā, tosun, and kasun. These are treated as avyaya. The next rule, 1.1.41, will add avyayībhāva compounds to the avyaya class."
},
{
  id: "1.1.41",
  slp1: "avyayIBAvaSca",
  slp1Display: "avyayIBAvaH ca",

  searchAliases: [
    "avyayībhāvaśca",
    "avyayibhavash ca",
    "अव्ययीभावश्च",
    "अव्ययीभावः च",
    "avyayibhava compound",
    "avyaya compound"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "avyayIBAva",
    "ca",
    "avyaya",
    "samAsa",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "अव्ययम्",
  anuvritti: "अव्ययम्",
  uddeshya: "अव्ययीभावः",
  vidheya: "अव्ययम्",

  meaning: "An avyayībhāva compound is also called avyaya.",

  explanation: "This rule completes the current avyaya-saṃjñā sequence. An avyayībhāva compound, a compound usually headed by an indeclinable element, receives the technical designation avyaya. The word ca connects it with the preceding avyaya rules.",

  examples: [
    {
      slp1: "upakfzwam",
      note: "An avyayībhāva compound such as upakṛṣṭam can be treated as avyaya."
    },
    {
      slp1: "yathASakti",
      note: "A compound such as yathāśakti illustrates the avyayībhāva type, with an indeclinable-like first member."
    }
  ],

  related: ["1.1.37", "1.1.40"],

  notes: "This is the last rule in the avyaya-saṃjñā cluster before the next topic begins with 1.1.42 शि सर्वनामस्थानम्."
},

{
  id: "1.1.42",
  slp1: "Si sarvanAmasTAnam",
  slp1Display: "Si sarvanAmasTAnam",

  searchAliases: [
    "śi sarvanāmasthānam",
    "shi sarvanamasthanam",
    "शि सर्वनामस्थानम्",
    "sarvanamasthana",
    "सर्वनामस्थान"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "Si",
    "sarvanAmasTAna",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",
  uddeshya: "शि",
  vidheya: "सर्वनामस्थानम्",

  meaning: "The affix śi is called sarvanāmasthāna.",

  explanation: "This sūtra begins the sarvanāmasthāna-saṃjñā section. Pāṇini gives the technical name sarvanāmasthāna to the affix śi. Later rules use this technical label to trigger operations in nominal declension.",

  examples: [
    {
      slp1: "Si",
      note: "The affix śi receives the technical designation sarvanāmasthāna."
    },
    {
      slp1: "sarvanAmasTAna",
      note: "This is a technical name used later in nominal operations."
    }
  ],

  related: [],

  notes: "This starts a new cluster: sarvanāmasthāna-saṃjñā. The next rule extends this designation to a group of nominal endings."
},

{
  id: "1.1.43",
  slp1: "suwanapuMsakasya",
  slp1Display: "suw anapuMsakasya",

  searchAliases: [
    "suḍ anapuṃsakasya",
    "sud anapumsakasya",
    "सुडनपुंसकस्य",
    "सुट् अनपुंसकस्य",
    "anapumsakasya",
    "sarvanamasthana"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "suw",
    "anapuMsaka",
    "sarvanAmasTAna",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "सर्वनामस्थानम्",
  uddeshya: "सुट् अनपुंसकस्य",
  vidheya: "सर्वनामस्थानम्",

  meaning: "The affixes included in suṭ, when following a non-neuter stem, are called sarvanāmasthāna.",

  explanation: "The term suṭ here refers to the first five nominal endings: सु, औ, जस्, अम्, and औट्. These endings receive the technical name sarvanāmasthāna when they are used after a masculine or feminine stem, but not after a neuter stem.",

examples: [
  {
    slp1: "suw",
    note: "This covers the first five nominal endings: सु, औ, जस्, अम्, औट्."
  },
  {
    slp1: "rAma + su",
    note: "After masculine rāma, सु is treated as sarvanāmasthāna."
  },
  {
    slp1: "latA + su",
    note: "After feminine latā, सु is treated as sarvanāmasthāna."
  }
],

  related: [
    "1.1.42"
  ],

  notes: "This rule continues the sarvanāmasthāna-saṃjñā cluster. The anuvṛtti of सर्वनामस्थानम् comes from 1.1.42."
},

{
  id: "1.1.44",
  slp1: "na veti viBAzA",
  slp1Display: "na vA iti viBAzA",

  searchAliases: [
    "na veti vibhāṣā",
    "na va iti vibhasha",
    "न वेति विभाषा",
    "न वा इति विभाषा",
    "vibhasha",
    "vibhāṣā",
    "विभाषा"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "na",
    "vA",
    "iti",
    "viBAzA",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "न वा इति",
  vidheya: "विभाषा",

  meaning: "The expression ‘not, or’ is called vibhāṣā, indicating optionality.",

  explanation: "This sūtra defines the technical term विभाषा. When Pāṇini uses this idea, the operation is optional: it may occur, or it may not occur. The word न gives the sense of non-application, and वा gives the sense of option.",

  examples: [
    {
      slp1: "na vA",
      note: "The sense is: it may not occur, or it may occur."
    },
    {
      slp1: "viBAzA",
      note: "This technical term marks optional application."
    }
  ],

  related: [],

  notes: "This sūtra is not part of the sarvanāmasthāna cluster. It defines the important paribhāṣā-like technical term विभाषा, used for optional rules."
},

{
  id: "1.1.45",
  slp1: "igyaRaH samprasAraRam",
  slp1Display: "ik yaRaH samprasAraRam",

  searchAliases: [
    "igyaṇaḥ samprasāraṇam",
    "ik yanah samprasaranam",
    "इग्यणः सम्प्रसारणम्",
    "इक् यणः सम्प्रसारणम्",
    "सम्प्रसारण",
    "samprasarana"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "samprasAraRa",
    "saMjYA"
  ],

  pratyaharas: [
    "ik",
    "yaR"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "इक् यणः",
  vidheya: "सम्प्रसारणम्",

  meaning: "An ik vowel occurring in place of a yaṇ semivowel is called samprasāraṇa.",

  explanation: "This sūtra defines the technical term सम्प्रसारण. The pratyāhāra यण् includes the semivowels य्, व्, र्, ल्. The corresponding इक् vowels are इ, उ, ऋ, ऌ. When one of these vowels replaces its corresponding semivowel, that replacement is called samprasāraṇa.",

  examples: [
    {
      slp1: "y -> i",
      note: "When य् is replaced by इ, the replacement is called samprasāraṇa."
    },
    {
      slp1: "v -> u",
      note: "When व् is replaced by उ, the replacement is called samprasāraṇa."
    },
    {
      slp1: "r -> f",
      note: "When र् is replaced by ऋ, the replacement is called samprasāraṇa."
    }
  ],

  related: [],

  notes: "This is an independent saṃjñā-sūtra defining सम्प्रसारण. Later rules will use this technical term."
},

{
  id: "1.1.46",
  slp1: "AdyantO wakitO",
  slp1Display: "AdyantO wakitO",

  searchAliases: [
    "ādyantau ṭakitau",
    "adyantau takitau",
    "आद्यन्तौ टकितौ",
    "आदि अन्त",
    "ṭit",
    "kit",
    "टित्",
    "कित्"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

glossary: [
  "Adi",
  "anta",
  "wit",
  "kit",
  "it",
  "Agama",
  "saMjYA"
],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "टित् कित्",
  vidheya: "आदि अन्त",

  meaning: "Elements marked with ṭ are placed at the beginning, and elements marked with k are placed at the end.",

  explanation: "This sūtra explains the positional force of the indicatory letters ट् and क्. A ṭit element is treated as initial, while a kit element is treated as final. This is especially important for augments, because their it-markers tell us where the augment is inserted.",

  examples: [
    {
      slp1: "wit",
      note: "A ṭit element is placed at the beginning."
    },
    {
      slp1: "kit",
      note: "A kit element is placed at the end."
    },
    {
      slp1: "Agama",
      note: "For augments, these markers help determine position."
    }
  ],

  related: [
    "1.1.5"
  ],

  notes: "This rule is useful for understanding it-markers. It is related to 1.1.5, where कित् and ङित् were already introduced."
},

{
  id: "1.1.47",
  slp1: "midaco'ntyAt paraH",
  slp1Display: "mit acaH antyAt paraH",

  searchAliases: [
    "midaco'ntyāt paraḥ",
    "mit acah antyat parah",
    "मिदचोऽन्त्यात्परः",
    "मित् अचः अन्त्यात् परः",
    "mit",
    "मित्"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "mit",
    "antya",
    "para",
    "Agama",
    "it",
    "saMjYA"
  ],

  pratyaharas: [
    "ac"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "मित्",
  vidheya: "अचः अन्त्यात् परः",

  meaning: "A mit element is placed after the final vowel.",

  explanation: "This sūtra gives the positional force of the indicatory marker म्. A mit augment is not simply placed at the absolute beginning or end. It is placed after the final vowel of the base to which it is added.",

  examples: [
    {
      slp1: "mit",
      note: "An element marked with indicatory म् is called mit."
    },
    {
      slp1: "ac antya",
      note: "The position is after the final vowel."
    },
    {
      slp1: "Agama",
      note: "This rule is especially useful for locating certain augments."
    }
  ],

  related: [
    "1.1.46"
  ],

  notes: "This rule continues the positional discussion of it-markers. 1.1.46 covers ṭit and kit placement; this rule covers mit placement."
},

{
  id: "1.1.48",
  slp1: "eco'igGrasvAdeSe",
  slp1Display: "ecaH ik hrasvAdeSe",

  searchAliases: [
    "eco igghrasvadeshe",
    "ecaḥ ik hrasvādeśe",
    "ecah ik hrasvadeshe",
    "एच इग्घ्रस्वादेशे",
    "एच् इक् ह्रस्वादेशे",
    "hrasvadesha",
    "ह्रस्वादेश"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "hrasva",
    "AdeSa",
    "saMjYA"
  ],

  pratyaharas: [
    "ec",
    "ik"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "एच्",
  vidheya: "इक् ह्रस्वादेशे",

  meaning: "When a short substitute is prescribed for an ec vowel, the corresponding ik vowel is used.",

  explanation: "The pratyāhāra ec includes ए, ओ, ऐ, औ. If a rule requires a short replacement for one of these vowels, the replacement is not a short ए or short ओ. Instead, the corresponding ik vowel is used: ए or ऐ gives इ, and ओ or औ gives उ.",

  examples: [
    {
      slp1: "e -> i",
      note: "When ए receives a short substitute, the substitute is इ."
    },
    {
      slp1: "o -> u",
      note: "When ओ receives a short substitute, the substitute is उ."
    },
    {
      slp1: "E/O",
      note: "ऐ and औ also take corresponding ik substitutes in this context."
    }
  ],

  related: [
    "1.1.2",
    "1.1.3"
  ],

  notes: "This rule is important because Sanskrit has no independent short ए or short ओ in the ordinary vowel system. So short replacement of ec vowels is handled through the corresponding ik vowels."
},

{
  id: "1.1.49",
  slp1: "zazWI sTAneyogA",
  slp1Display: "zazWI sTAne-yogA",

  searchAliases: [
    "ṣaṣṭhī sthāneyogā",
    "shashthi sthaneyoga",
    "षष्ठी स्थानेयोगा",
    "षष्ठी स्थाने योगा",
    "sthane yoga",
    "स्थान",
    "षष्ठी"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "zazWI",
    "sTAna",
    "yoga",
    "AdeSa",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "षष्ठी",
  vidheya: "स्थानेयोगा",

  meaning: "A sixth-case expression is understood as connected with replacement in place of something.",

  explanation: "This rule tells us how to interpret a genitive expression in many substitution rules. When an element is stated in the sixth case, it often marks the original item whose place is taken by the substitute. Thus the genitive points to the sthānin, the item to be replaced.",

  examples: [
    {
      slp1: "ikas yaR",
      note: "In a rule like iko yaṇ aci, इकः points to the ik vowels whose place is taken."
    },
    {
      slp1: "sTAna",
      note: "The sixth case is interpreted with the idea of स्थान, the place of replacement."
    },
    {
      slp1: "AdeSa",
      note: "This rule is central to understanding substitution rules."
    }
  ],

  related: [
    "1.1.48"
  ],

  notes: "This begins a very important set of interpretation rules for substitution. It helps identify the original element replaced by an ādeśa."
},

{
  id: "1.1.50",
  slp1: "sTAne'ntaratamaH",
  slp1Display: "sTAne antaratamaH",

  searchAliases: [
    "sthāne'ntaratamaḥ",
    "sthane antaratamah",
    "स्थानेऽन्तरतमः",
    "स्थाने अन्तरतमः",
    "antaratama",
    "अन्तरतम"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "sTAna",
    "antaratama",
    "AdeSa",
    "sTAnin",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "स्थाने",
  vidheya: "अन्तरतमः",

  meaning: "In the place of something, the most similar substitute is chosen.",

  explanation: "This rule guides the choice of substitute. When more than one substitute is possible, the one most similar to the original element is selected. Similarity may depend on place of articulation, effort, quantity, or other relevant features.",

  examples: [
    {
      slp1: "i -> y",
      note: "इ is most closely matched by य् among the yaṇ substitutes."
    },
    {
      slp1: "u -> v",
      note: "उ is most closely matched by व्."
    },
    {
      slp1: "f -> r",
      note: "ऋ is most closely matched by र्."
    }
  ],

  related: [
    "1.1.49"
  ],

  notes: "This rule works closely with 1.1.49. First the genitive identifies the sthānin, the item to be replaced; then 1.1.50 helps choose the most similar ādeśa."
},

{
  id: "1.1.51",
  slp1: "uraR raparaH",
  slp1Display: "uH aR raparaH",

  searchAliases: [
    "uraṇ raparaḥ",
    "uran raparah",
    "उरण् रपरः",
    "उः अण् रपरः",
    "rapara",
    "रपर",
    "ऋ",
    "ar",
    "Ar"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "uH",
    "rapara",
    "AdeSa",
    "sTAnin",
    "paribhAzA"
  ],

pratyaharas: [
  "aR_long"
],

  adhikara: "",
  anuvritti: "",

  uddeshya: "उः अण्",
  vidheya: "रपरः",

  meaning: "When an aṇ substitute comes in place of ṛ, it is followed by r.",

  explanation: "This rule explains a special detail in substitutions for ऋ. When an aṇ-type substitute is used in place of ऋ, the substitute is followed by र्. Therefore the guṇa of ऋ becomes अर्, and the vṛddhi of ऋ becomes आर्.",

  examples: [
    {
      slp1: "f -> ar",
      note: "The guṇa substitute of ऋ is अर्."
    },
    {
      slp1: "f -> Ar",
      note: "The vṛddhi substitute of ऋ is आर्."
    },
    {
      slp1: "rapara",
      note: "The substitute is followed by र्."
    }
  ],

  related: [
    "1.1.3",
    "1.1.49",
    "1.1.50"
  ],

  notes: "This rule is especially useful when explaining why ऋ gives अर् and आर् in guṇa and vṛddhi contexts. Note: अण् is ambiguous because the marker ण् occurs twice in the Māheśvara-sūtras. Here we use the longer अण्, ending at the second ण्, and distinguish it internally as aR_long to avoid an ID conflict."
},

{
  id: "1.1.52",
  slp1: "alo'ntyasya",
  slp1Display: "alaH antyasya",

  searchAliases: [
    "alo'ntyasya",
    "alah antyasya",
    "alo antyasya",
    "अलोऽन्त्यस्य",
    "अलः अन्त्यस्य",
    "antyasya",
    "अन्त्यस्य"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "antya",
    "AdeSa",
    "sTAnin",
    "paribhAzA"
  ],

  pratyaharas: [
    "al"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "अलः अन्त्यस्य",
  vidheya: "आदेशः",

  meaning: "A substitute normally replaces the final sound of the expression to which it applies.",

  explanation: "This rule tells us the normal scope of a substitution. When an ādeśa is prescribed for something, it does not necessarily replace the whole expression. By default, it replaces the final sound, the antya al, of the sthānin.",

  examples: [
    {
      slp1: "al",
      note: "The rule concerns a final sound."
    },
    {
      slp1: "antya",
      note: "The substitute applies to the final element."
    },
    {
      slp1: "AdeSa",
      note: "This is a default rule for interpreting substitutions."
    }
  ],

  related: [
    "1.1.49",
    "1.1.50"
  ],

  notes: "This rule is central for substitution. After 1.1.49 identifies the sthānin through the genitive, 1.1.52 says that the replacement normally affects only the final sound."
},

{
  id: "1.1.53",
  slp1: "Ricca",
  slp1Display: "Rit ca",

  searchAliases: [
    "ṅic ca",
    "ngic ca",
    "ङिच्च",
    "ङित् च",
    "ङित्",
    "ṅit",
    "ngit"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "Rit",
    "it",
    "AdeSa",
    "antya",
    "sTAnin",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "अलोऽन्त्यस्य",

  uddeshya: "ङित्",
  vidheya: "अन्त्यस्य आदेशः",

  meaning: "A ṅit substitute is also treated as replacing the final sound.",

  explanation: "This rule continues the principle from 1.1.52. Normally a substitute replaces the final sound of the expression concerned. Here Pāṇini explicitly includes substitutes marked with the indicatory letter ङ् within that final-sound replacement principle.",

  examples: [
    {
      slp1: "Rit",
      note: "A substitute marked with indicatory ङ् is called ṅit."
    },
    {
      slp1: "antya",
      note: "The replacement is connected with the final element."
    },
    {
      slp1: "AdeSa",
      note: "This continues the substitution interpretation from 1.1.52."
    }
  ],

  related: [
    "1.1.52"
  ],

  notes: "This rule should be read together with 1.1.52 अलोऽन्त्यस्य. It extends or confirms the final-sound replacement principle for ṅit substitutes."
},

{
  id: "1.1.54",
  slp1: "AdeH parasya",
  slp1Display: "AdeH parasya",

  searchAliases: [
    "ādeḥ parasya",
    "adeh parasya",
    "आदेः परस्य",
    "आदि परस्य",
    "initial of the following",
    "parasya",
    "परस्य"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "Adi",
    "para",
    "AdeSa",
    "sTAnin",
    "paribhAzA"
  ],

  pratyaharas: [
    "al"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "परस्य",
  vidheya: "आदेः",

meaning: "When a substitute is prescribed for a following element, it applies to the initial sound of that following element.",

  explanation: "This rule gives another special interpretation for the scope of substitution. While 1.1.52 states the normal principle that a substitute replaces the final sound, this rule says that in the case of a following element, the initial sound of that following element is intended.",

examples: [
  {
    slp1: "parasya AdiH",
    note: "When an operation is stated with reference to a following element, its initial sound is intended."
  },
  {
    slp1: "para + al",
    note: "The relevant sound is the first sound of the following element, not its final sound."
  },
  {
    slp1: "AdeSa",
    note: "This rule helps decide the exact target of a substitute when the target is a following element."
  }
],

  related: [
    "1.1.52",
    "1.1.53"
  ],

  notes: "This belongs to the same substitution-interpretation cluster as 1.1.49–1.1.53. It contrasts with the default final-sound rule of 1.1.52 by specifying the initial sound of a following element."
},

{
  id: "1.1.55",
  slp1: "anekAl Sit sarvasya",
  slp1Display: "anekAl Sit sarvasya",

  searchAliases: [
    "anekāl śit sarvasya",
    "anekal shit sarvasya",
    "अनेकाल्शित्सर्वस्य",
    "अनेकाल् शित् सर्वस्य",
    "anekal",
    "sarvasya",
    "śit",
    "shit",
    "शित्"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "anekAl",
    "Sit",
    "sarva",
    "AdeSa",
    "sTAnin",
    "paribhAzA"
  ],

  pratyaharas: [
    "al"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "अनेकाल् शित्",
  vidheya: "सर्वस्य",

  meaning: "A substitute that has more than one sound, or that is marked with ś, replaces the whole original item.",

  explanation: "This rule gives an exception to the normal final-sound replacement rule of 1.1.52. If the substitute consists of more than one sound, or if it is marked with the indicatory letter श्, then it replaces the whole sthānin, not merely the final sound.",

examples: [
  {
    slp1: "anekAl AdeSa",
    note: "If the substitute has more than one sound, it replaces the whole sthānin."
  },
  {
    slp1: "Sit AdeSa",
    note: "If the substitute is marked with indicatory श्, it also replaces the whole sthānin."
  },
  {
    slp1: "sarvasya",
    note: "Here सर्वस्य means the entire original item is replaced, not only its final sound."
  }
],

  related: [
    "1.1.52",
    "1.1.53",
    "1.1.54"
  ],

  notes: "This rule is important because it limits the default principle of 1.1.52. Normally a substitute replaces the final sound, but an anekāl or śit substitute replaces the whole original expression."
},

{
  id: "1.1.56",
  slp1: "sTAnivadAdeSo'nalviDO",
  slp1Display: "sTAnivat AdeSaH analviDO",

  searchAliases: [
    "sthānivad ādeśo'nalvidhau",
    "sthanivad adeso analvidhau",
    "स्थानिवदादेशोऽनल्विधौ",
    "स्थानिवत् आदेशः अनल्विधौ",
    "sthanivat",
    "analvidhi",
    "स्थानिवत्",
    "अनल्विधि"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "sTAnivat",
    "AdeSa",
    "sTAnin",
    "al",
    "viDi",
    "analviDi",
    "paribhAzA"
  ],

  pratyaharas: [
    "al"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "आदेशः",
  vidheya: "स्थानिवत् अनल्विधौ",

  meaning: "A substitute behaves like the original item, except in operations depending specifically on sounds.",

  explanation: "This paribhāṣā says that an ādeśa, a substitute, is treated like the sthānin, the original item, for further grammatical operations. But this equivalence does not apply in al-vidhi, that is, in operations that depend specifically on the actual sound or letter present.",

  examples: [
    {
      slp1: "AdeSaH sTAnivat",
      note: "A substitute may behave like the original item for later operations."
    },
    {
      slp1: "sTAnin",
      note: "The substitute inherits the grammatical status of the replaced item where allowed."
    },
    {
      slp1: "analviDi",
      note: "This equivalence does not apply where a rule depends on the actual sound."
    }
  ],

  related: [
    "1.1.49",
    "1.1.52",
    "1.1.55"
  ],

  notes: "This is one of the most important paribhāṣās in the Aṣṭādhyāyī. It controls how far a substitute can inherit the grammatical behavior of the original item. The exception अनल्विधौ prevents this inheritance in sound-specific operations."
},

{
  id: "1.1.57",
  slp1: "acaH parasmin pUrvaviDO",
  slp1Display: "acaH parasmin pUrvaviDO",

  searchAliases: [
    "acaḥ parasmin pūrvavidhau",
    "acah parasmin purvavidhau",
    "अचः परस्मिन् पूर्वविधौ",
    "अच् परस्मिन् पूर्वविधौ",
    "purvavidhi",
    "pūrvavidhi",
    "पूर्वविधि"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

glossary: [
  "parasmin",
  "pUrvaviDi",
  "AdeSa",
  "sTAnin",
  "sTAnivat",
  "viDi",
  "paribhAzA"
],

  pratyaharas: [
    "ac"
  ],

  adhikara: "",
  anuvritti: "स्थानिवदादेशः",

  uddeshya: "अचः आदेशः",
  vidheya: "परस्मिन् पूर्वविधौ स्थानिवत्",

  meaning: "In a pūrvavidhi, a substitute for a vowel is treated like the original when the conditioning element is following.",

  explanation: "This rule continues the discussion of sthānivad-bhāva from 1.1.56. It deals with cases where a vowel has been replaced, and a later rule concerns something preceding while depending on a following element. In such a pūrvavidhi context, the substitute may be treated like the original vowel.",

  examples: [
    {
      slp1: "ac AdeSa",
      note: "The rule concerns a substitute that has replaced a vowel."
    },
    {
      slp1: "parasmin",
      note: "The conditioning factor is in a following element."
    },
    {
      slp1: "pUrvaviDi",
      note: "The operation concerns something earlier or preceding."
    }
  ],

  related: [
    "1.1.56"
  ],

  notes: "This rule should be read as a continuation of 1.1.56 स्थानिवदादेशोऽनल्विधौ. It is a specialized rule about sthānivad treatment in pūrvavidhi contexts."
},

{
  id: "1.1.58",
  slp1: "na padAntadvirvacanavareyalopasvarasavarRAnusvAradIrGajaScarvidhizu",
  slp1Display: "na padAnta-dvirvacana-vare-ya-lopa-svara-savarRa-anusvAra-dIrGa-jaS-car-vidhizu",

  searchAliases: [
    "na padānta dvirvacana vare yalopa svara savarṇa anusvāra dīrgha jaś car vidhiṣu",
    "na padanta dvirvacana vare yalopa svara savarna anusvara dirgha jas car vidhishu",
    "न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु",
    "पदान्त",
    "द्विर्वचन",
    "लोप",
    "स्वर",
    "सवर्ण",
    "अनुस्वार",
    "दीर्घ",
    "जश्",
    "चर्"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "padAnta",
    "dvirvacana",
    "lopa",
    "svara",
    "savarRa",
    "anusvAra",
    "dIrGa",
    "viDi",
    "sTAnivat",
    "AdeSa",
    "paribhAzA"
  ],

pratyaharas: [
  "jaS",
  "car"
],

  adhikara: "",
  anuvritti: "स्थानिवदादेशः; अचः परस्मिन् पूर्वविधौ",

  uddeshya: "पदान्त-द्विर्वचन-वरे-यलोप-स्वर-सवर्ण-अनुस्वार-दीर्घ-जश्-चर्-विधिषु",
  vidheya: "न स्थानिवत्",

  meaning: "In the listed operations, the substitute is not treated like the original item.",

  explanation: "This rule limits the sthānivad principle from 1.1.56 and 1.1.57. Although a substitute may often behave like the original item, that treatment is blocked in the specific operations listed here, such as padānta, reduplication, lopa, accent, savarṇa, anusvāra, dīrgha, jaś, and car operations.",

  examples: [
    {
      slp1: "na sTAnivat",
      note: "In these listed contexts, the substitute is not treated like the original."
    },
    {
      slp1: "dvirvacana",
      note: "Reduplication is one of the operations excluded from sthānivad treatment here."
    },
    {
      slp1: "lopa / svara / dIrGa",
      note: "Operations such as elision, accent, and lengthening are also included in the exclusion list."
    }
  ],

  related: [
    "1.1.56",
    "1.1.57"
  ],

  notes: "This is a limiting rule for स्थानिवद्भाव. The compound is long and contains a list of operations where the substitute should not be treated as if it were the original. We may refine the individual examples later when the relevant downstream rules are added."
},

{
  id: "1.1.59",
  slp1: "dvirvacane'ci",
  slp1Display: "dvirvacane aci",

  searchAliases: [
    "dvirvacane aci",
    "dvirvacane'ci",
    "द्विर्वचनेऽचि",
    "द्विर्वचने अचि",
    "द्विर्वचन",
    "अचि",
    "reduplication"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "dvirvacana",
    "sTAnivat",
    "AdeSa",
    "sTAnin",
    "paribhAzA"
  ],

  pratyaharas: [
    "ac"
  ],

  adhikara: "",
  anuvritti: "स्थानिवदादेशः",

  uddeshya: "द्विर्वचने अचि",
  vidheya: "स्थानिवत्",

  meaning: "In reduplication before a following vowel, the substitute may be treated like the original.",

  explanation: "This rule gives a specific sthānivad allowance after the exclusion stated in 1.1.58. In the context of reduplication, when a following vowel is involved, the substitute can be treated like the original item for the relevant operation.",

  examples: [
    {
      slp1: "dvirvacana",
      note: "The rule concerns reduplication."
    },
    {
      slp1: "aci",
      note: "The context is before or in relation to a following vowel."
    },
    {
      slp1: "sTAnivat",
      note: "Here the substitute is treated like the original for the reduplication-related operation."
    }
  ],

  related: [
    "1.1.56",
    "1.1.57",
    "1.1.58"
  ],

  notes: "This rule should be read immediately after 1.1.58. Although 1.1.58 blocks sthānivad treatment in dvirvacana and related operations, 1.1.59 gives a special allowance for reduplication in the context of a following ac vowel."
},

{
  id: "1.1.60",
  slp1: "adarSanaM lopaH",
  slp1Display: "adarSanam lopaH",

  searchAliases: [
    "adarśanaṃ lopaḥ",
    "adarshanam lopah",
    "अदर्शनं लोपः",
    "अदर्शनम् लोपः",
    "lopa",
    "लोप"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "adarSana",
    "lopa",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "अदर्शनम्",
  vidheya: "लोपः",

  meaning: "Non-appearance of an element is called lopa.",

  explanation: "This sūtra defines the technical term लोप. When a grammatical element is not visibly or audibly present, that non-appearance is called lopa. The element is treated as elided, not necessarily as never having existed in the grammatical derivation.",

  examples: [
    {
      slp1: "lopa",
      note: "Lopa means that an expected element is not seen or heard."
    },
    {
      slp1: "adarSana",
      note: "Adarśana literally means non-appearance."
    },
    {
      slp1: "it-lopa",
      note: "Indicatory letters are often removed by lopa after serving their grammatical function."
    }
  ],

  related: [
    "1.1.58"
  ],

  notes: "This is the basic definition of लोप. It is important throughout the grammar because many operations remove visible elements while still allowing their grammatical effect to remain."
},

{
  id: "1.1.61",
  slp1: "pratyayasya lukSlulupaH",
  slp1Display: "pratyayasya luk-Slu-lupaH",

  searchAliases: [
    "pratyayasya luk ślu lupaḥ",
    "pratyayasya luk shlu lupah",
    "प्रत्ययस्य लुक्श्लुलुपः",
    "प्रत्ययस्य लुक् श्लु लुपः",
    "luk",
    "ślu",
    "shlu",
    "lup"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "pratyaya",
    "luk",
    "Slu",
    "lup",
    "lopa",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "अदर्शनं लोपः",

  uddeshya: "प्रत्ययस्य अदर्शनम्",
  vidheya: "लुक् श्लु लुप्",

  meaning: "The terms luk, ślu, and lup denote special cases of elision of an affix.",

  explanation: "This sūtra continues from 1.1.60, where non-appearance was defined as lopa. Here Pāṇini gives three special technical terms—लुक्, श्लु, and लुप्—for cases where an affix is elided. These terms are important because later rules may prescribe लुक्, श्लु, or लुप् rather than simply saying लोप.",

  examples: [
    {
      slp1: "pratyaya-lopa",
      note: "The rule concerns the non-appearance of an affix."
    },
    {
      slp1: "luk / Slu / lup",
      note: "These are special technical labels for affix-elision."
    },
    {
      slp1: "lopa",
      note: "They are connected with the general idea of lopa defined in 1.1.60."
    }
  ],

  related: [
    "1.1.60"
  ],

  notes: "This rule should be read immediately after 1.1.60 अदर्शनं लोपः. लुक्, श्लु, and लुप् are special labels used when the elided item is a प्रत्यय."
},

{
  id: "1.1.62",
  slp1: "pratyayalope pratyayalakzaRam",
  slp1Display: "pratyaya-lope pratyaya-lakzaRam",

  searchAliases: [
    "pratyayalope pratyayalakṣaṇam",
    "pratyayalope pratyayalakshanam",
    "प्रत्ययलोपे प्रत्ययलक्षणम्",
    "प्रत्यय लोपे प्रत्यय लक्षणम्",
    "pratyaya lopa",
    "pratyayalakshana",
    "प्रत्ययलक्षण"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "pratyaya",
    "lopa",
    "lakzaRa",
    "pratyayalakzaRa",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "प्रत्ययलोपे",
  vidheya: "प्रत्ययलक्षणम्",

  meaning: "When an affix is elided, the grammatical effect based on that affix may still remain.",

  explanation: "This rule states that even if a pratyaya is removed by lopa, rules that depend on the presence or character of that pratyaya may still apply. In other words, disappearance of the affix does not necessarily erase its grammatical effect.",

  examples: [
    {
      slp1: "pratyaya-lopa",
      note: "The affix may disappear visibly or audibly."
    },
    {
      slp1: "pratyaya-lakzaRa",
      note: "A rule may still operate because of the elided affix."
    },
    {
      slp1: "luk / Slu / lup",
      note: "Special elisions of affixes can still leave grammatical effects behind."
    }
  ],

  related: [
    "1.1.60",
    "1.1.61"
  ],

  notes: "This is a key paribhāṣā. It prevents us from assuming that an elided affix becomes grammatically irrelevant. Even after lopa, the affix can still condition later operations."
},

{
  id: "1.1.63",
  slp1: "na lumatANgasya",
  slp1Display: "na lumatA aNgasya",

  searchAliases: [
    "na lumatāṅgasya",
    "na lumata angasya",
    "न लुमताङ्गस्य",
    "न लुमता अङ्गस्य",
    "lumat",
    "aṅga",
    "anga",
    "अङ्ग"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "lumat",
    "aNga",
    "pratyaya",
    "lopa",
    "luk",
    "Slu",
    "lup",
    "pratyayalakzaRa",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "प्रत्ययलोपे प्रत्ययलक्षणम्",

  uddeshya: "लुमता अङ्गस्य",
  vidheya: "न प्रत्ययलक्षणम्",

  meaning: "When an affix is elided by a lu-class elision, operations on the aṅga based on that affix do not apply.",

  explanation: "This rule limits 1.1.62. Although an elided affix may normally still produce grammatical effects, that principle is blocked for operations on the aṅga when the affix has disappeared through लुक्, श्लु, or लुप्. The term lumat refers to these lu-marked elisions.",

  examples: [
    {
      slp1: "luk / Slu / lup",
      note: "These lu-class elisions are intended by lumat."
    },
    {
      slp1: "aNga",
      note: "The restriction concerns operations on the base or stem."
    },
    {
      slp1: "na pratyayalakzaRa",
      note: "Here the elided affix does not trigger affix-based operations on the aṅga."
    }
  ],

  related: [
    "1.1.61",
    "1.1.62"
  ],

  notes: "This rule is an exception to 1.1.62. प्रत्ययलक्षण normally survives affix-elision, but not for aṅga operations when the elision is by लुक्, श्लु, or लुप्."
},

{
  id: "1.1.64",
  slp1: "aco'ntyAdi wi",
  slp1Display: "acaH antyAdi wi",

  searchAliases: [
    "aco'ntyādi ṭi",
    "acah antyadi ti",
    "अचोऽन्त्यादि टि",
    "अचः अन्त्यादि टि",
    "antyadi",
    "ṭi",
    "ti",
    "टि"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "antya",
    "Adi",
    "wi",
    "saMjYA"
  ],

  pratyaharas: [
    "ac"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "अचः अन्त्यादि",
  vidheya: "टि",

  meaning: "The portion beginning with the final vowel is called ṭi.",

  explanation: "This sūtra defines the technical term टि. In an expression, identify the final vowel. The part beginning with that final vowel and continuing to the end is called ṭi. This term is useful in later rules that operate on the final vowel-plus-following portion of a word or base.",

  examples: [
    {
      slp1: "rAma",
      note: "The final vowel is अ; the ṭi portion is अ."
    },
    {
      slp1: "Bavat",
      note: "The final vowel is अ; the ṭi portion is अत्."
    },
    {
      slp1: "pacati",
      note: "The final vowel is इ; the ṭi portion is इ."
    }
  ],

  related: [
    "1.1.52"
  ],

  notes: "This is a saṃjñā-sūtra defining टि. It is based on locating the final vowel, not merely the final sound."
},

{
  id: "1.1.65",
  slp1: "alo'ntyAt pUrva upaDA",
  slp1Display: "alaH antyAt pUrvaH upaDA",

  searchAliases: [
    "alo'ntyāt pūrva upadhā",
    "alah antyat purvah upadha",
    "अलोऽन्त्यात् पूर्व उपधा",
    "अलः अन्त्यात् पूर्वः उपधा",
    "upadha",
    "उपधा"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "antya",
    "pUrva",
    "upaDA",
    "saMjYA"
  ],

  pratyaharas: [
    "al"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "अलः अन्त्यात् पूर्वः",
  vidheya: "उपधा",

  meaning: "The sound immediately before the final sound is called upadhā.",

  explanation: "This sūtra defines the technical term उपधा. In a word or base, first identify the final sound. The sound immediately before that final sound is called upadhā. Later rules use this term to prescribe operations on the penultimate sound.",

  examples: [
    {
      slp1: "Bavat",
      note: "In भवत्, the final sound is त्, and the preceding अ is the upadhā."
    },
    {
      slp1: "pac",
      note: "In पच्, the final sound is च्, and the preceding अ is the upadhā."
    },
    {
      slp1: "rAjan",
      note: "In राजन्, the final sound is न्, and the preceding अ is the upadhā."
    }
  ],

  related: [
    "1.1.52",
    "1.1.64"
  ],

  notes: "This is a basic positional saṃjñā. Unlike टि in 1.1.64, which begins from the final vowel, उपधा is simply the sound immediately before the final sound."
},

{
  id: "1.1.66",
  slp1: "tasminniti nirdizwe pUrvasya",
  slp1Display: "tasmin iti nirdizwe pUrvasya",

  searchAliases: [
    "tasminn iti nirdiṣṭe pūrvasya",
    "tasmin iti nirdishte purvasya",
    "तस्मिन्निति निर्दिष्टे पूर्वस्य",
    "तस्मिन् इति निर्दिष्टे पूर्वस्य",
    "tasmin",
    "nirdishta",
    "pūrvasya",
    "पूर्वस्य"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "tasmin",
    "nirdizwa",
    "pUrva",
    "saptamI",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "तस्मिन् इति निर्दिष्टे",
  vidheya: "पूर्वस्य",

  meaning: "When a condition is stated in the locative, the operation applies to the preceding element.",

  explanation: "This rule explains how to read rules where the conditioning element is stated in the locative case. If a rule says that something happens ‘in’ or ‘before’ a certain following environment, the actual operation applies to the element immediately preceding that stated environment.",

  examples: [
    {
      slp1: "aci",
      note: "When a rule says ‘aci’ — before a vowel — the operation usually applies to the preceding element."
    },
    {
      slp1: "pUrvasya",
      note: "The affected item is the one before the locative condition."
    },
    {
      slp1: "tasmin nirdizwe",
      note: "A locative expression identifies the following environment."
    }
  ],

  related: [
    "1.1.57"
  ],

  notes: "This is a key interpretation rule. It helps read many later sūtras where a condition is given in the locative case, such as अचि, हलि, परे, etc."
},

{
  id: "1.1.67",
  slp1: "tasmAdityuttarasya",
  slp1Display: "tasmAt iti uttarasya",

  searchAliases: [
    "tasmād ity uttarasya",
    "tasmad ity uttarasya",
    "तस्मादित्युत्तरस्य",
    "तस्मात् इति उत्तरस्य",
    "tasmad",
    "uttarasya",
    "उत्तरस्य",
    "ablative"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "tasmAt",
    "iti",
    "uttara",
    "paYcamI",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "तस्मात् इति निर्दिष्टे",
  vidheya: "उत्तरस्य",

  meaning: "When a condition is stated in the ablative, the operation applies to the following element.",

  explanation: "This rule complements 1.1.66. There, a locative condition points to the preceding element. Here, an ablative expression points to the following element. Thus when a rule says ‘after X’ or uses an ablative expression, the item after that stated condition is the one affected.",

  examples: [
    {
      slp1: "tasmAt",
      note: "An ablative expression marks the point after which the operation is understood."
    },
    {
      slp1: "uttarasya",
      note: "The affected item is the following element."
    },
    {
      slp1: "tasmAt nirdizwe",
      note: "When something is specified by an ablative expression, look to what follows it."
    }
  ],

  related: [
    "1.1.66"
  ],

  notes: "This should be learned together with 1.1.66. Locative wording points to the preceding element; ablative wording points to the following element."
},

{
  id: "1.1.68",
  slp1: "svaM rUpaM SabdasyASabdasaMjYA",
  slp1Display: "svaM rUpaM Sabdasya aSabdasaMjYA",

  searchAliases: [
    "svaṃ rūpaṃ śabdasyāśabdasaṃjñā",
    "svam rupam shabdasya ashabdasamjna",
    "स्वं रूपं शब्दस्याशब्दसंज्ञा",
    "स्वं रूपं शब्दस्य अशब्दसंज्ञा",
    "svarupa",
    "śabda",
    "shabda",
    "अशब्दसंज्ञा"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "sva",
    "rUpa",
    "Sabda",
    "saMjYA",
    "aSabdasaMjYA",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "शब्दस्य",
  vidheya: "स्वं रूपम्",

  meaning: "A grammatical word denotes its own form, except when it is a technical term.",

  explanation: "This rule explains how words are to be understood inside grammatical rules. Normally, when Pāṇini mentions a word or sound-form, that form itself is intended. But if the word is a technical saṃjñā, then it denotes the class or concept assigned by that saṃjñā, not merely its own phonetic form.",

  examples: [
    {
      slp1: "agni",
      note: "If the word agni is mentioned in a rule, the form agni itself is intended."
    },
    {
      slp1: "pratyaya",
      note: "A technical term such as pratyaya denotes the grammatical category, not merely the sound-form pratyaya."
    },
    {
      slp1: "saMjYA",
      note: "Technical designations are excluded by the expression aśabdasaṃjñā."
    }
  ],

  related: [
    "1.1.44"
  ],

  notes: "This is a key interpretive rule. It prevents confusion between a word as a sound-form and a word as a technical grammatical label."
},

{
  id: "1.1.69",
  slp1: "aRuditsavarRasya cApratyayaH",
  slp1Display: "aR udit savarRasya ca apratyayaH",

  searchAliases: [
    "aṇudit savarṇasya cāpratyayaḥ",
    "anuditsavarnasya capratyayah",
    "अणुदित्सवर्णस्य चाप्रत्ययः",
    "अण् उदित् सवर्णस्य च अप्रत्ययः",
    "udit",
    "savarṇa",
    "savarna",
    "apratyaya",
    "अप्रत्यय"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "udit",
    "savarRa",
    "pratyaya",
    "apratyaya",
    "paribhAzA"
  ],

  pratyaharas: [
    "aR_short"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "अण् उदित्",
  vidheya: "सवर्णस्य च अप्रत्ययः",

  meaning: "Aṇ and udit references include their savarṇa members also, except when the item is an affix.",

  explanation: "This rule expands certain sound references. The pratyāhāra अण् and sounds marked with indicatory उ include not only the directly stated sounds, but also their savarṇa counterparts. However, this extension does not apply when the item concerned is a pratyaya.",

  examples: [
    {
      slp1: "aR_short",
      note: "Here अण् is the short अण्: अ, इ, उ."
    },
    {
      slp1: "savarRa",
      note: "The reference extends to homogeneous sounds, such as short and long vowel counterparts."
    },
    {
      slp1: "apratyaya",
      note: "The extension applies where the item is not an affix."
    }
  ],

  related: [
    "1.1.9",
    "1.1.51"
  ],

  notes: "Important: अण् is ambiguous because ण् occurs twice in the Māheśvara-sūtras. In this rule, use the shorter अण्, already stored internally as aR_short. This contrasts with 1.1.51, where we used aR_long."
},

{
  id: "1.1.70",
  slp1: "taparastatkAlasya",
  slp1Display: "taparaH tatkAlasya",

  searchAliases: [
    "taparaḥ tatkālasya",
    "taparas tatkalasya",
    "तपरस्तत्कालस्य",
    "तपरः तत्कालस्य",
    "tapara",
    "tatkala",
    "तत्काल"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "tapara",
    "tatkAla",
    "kAla",
    "savarRa",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "तपरः",
  vidheya: "तत्कालस्य",

  meaning: "A sound followed by indicatory त् denotes only sounds of the same duration.",

  explanation: "This rule limits the range of reference. When a sound is marked as tapara, that is, followed by indicatory त्, it refers only to sounds having the same time-measure or duration. This is especially relevant after 1.1.69, where savarṇa extension was stated. The त् marker prevents the reference from spreading to sounds of different duration.",

  examples: [
    {
      slp1: "at",
      note: "The त् marker restricts the reference to short अ only, not long आ."
    },
    {
      slp1: "it",
      note: "The reference is to short इ only, not long ई."
    },
    {
      slp1: "tatkAla",
      note: "The intended sound must have the same duration or time-measure."
    }
  ],

  related: [
    "1.1.9",
    "1.1.69"
  ],

  notes: "This rule is best read after 1.1.69. While 1.1.69 allows savarṇa extension, 1.1.70 restricts that extension when a sound is marked with following त्."
},

{
  id: "1.1.71",
  slp1: "Adirantyena sahetA",
  slp1Display: "AdiH antyena saha itA",

  searchAliases: [
    "ādir antyena sahetā",
    "adir antyena saheta",
    "आदिरन्त्येन सहेता",
    "आदिः अन्त्येन सह इता",
    "pratyahara",
    "प्रत्याहार",
    "it marker",
    "इत्"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "Adi",
    "antya",
    "saha",
    "it",
    "pratyAhAra",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

uddeshya: "आदिः अन्त्येन इता सह",
vidheya: "स्वस्य मध्यवर्तिनां च ग्रहणम्",

  meaning: "An initial sound, together with a final indicatory marker, denotes the intervening sounds.",

  explanation: "This rule explains how pratyāhāras are formed from the Māheśvara-sūtras. A starting sound is taken together with a later indicatory marker. The expression then denotes all the sounds from the starting sound up to, but not including, that final marker. For example, अच् begins with अ and ends with the marker च्, so it denotes the vowels अ, इ, उ, ऋ, ऌ, ए, ओ, ऐ, औ.",

  examples: [
    {
      slp1: "ac",
      note: "अ + च् denotes the vowels from अ up to the marker च्."
    },
    {
      slp1: "hal",
      note: "ह + ल् denotes the consonants from ह् up to the final marker ल्."
    },
    {
      slp1: "ik",
      note: "इ + क् denotes इ, उ, ऋ, ऌ."
    }
  ],

  related: [
    "1.1.68",
    "1.1.69"
  ],

  notes: "This is the foundational rule for understanding pratyāhāras. The final marker, such as च् in अच् or ल् in हल्, is an इत् marker and is not itself included in the set."
},

{
  id: "1.1.72",
  slp1: "yena vidhistadantasya",
  slp1Display: "yena viDiH tadantasya",

  searchAliases: [
    "yena vidhis tadantasya",
    "yena vidhiḥ tadantasya",
    "येन विधिस्तदन्तस्य",
    "येन विधिः तदन्तस्य",
    "tadanta",
    "तदन्त",
    "vidhi"
  ],

  type: "paribhAzA",
  typeDisplay: "परिभाषा-सूत्र",

  glossary: [
    "yena",
    "viDi",
    "tadanta",
    "anta",
    "paribhAzA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "",

  uddeshya: "येन विधिः",
  vidheya: "तदन्तस्य",

  meaning: "A rule stated by means of an element applies to something ending in that element.",

  explanation: "This paribhāṣā explains the scope of many rules. When a rule mentions an element as the basis of an operation, the rule is often understood to apply not only to that element alone, but to a larger expression ending in that element. This is called tadanta-vidhi.",

  examples: [
    {
      slp1: "tadanta",
      note: "The rule applies to something ending in the stated element."
    },
    {
      slp1: "viDi",
      note: "The prescription is extended to an expression ending in the mentioned item."
    },
    {
      slp1: "yena",
      note: "The element by which the rule is stated determines the ending of the target expression."
    }
  ],

  related: [
    "1.1.68"
  ],

  notes: "This is a very important interpretive rule. It introduces the idea of tadanta-vidhi: a rule mentioning X may apply to something ending in X."
},

{
  id: "1.1.73",
  slp1: "vfdDiryasyAcAmAdistadvfdDam",
  slp1Display: "vfdDiH yasya acAm AdiH tat vfdDam",

  searchAliases: [
    "vṛddhir yasyācām ādis tad vṛddham",
    "vrddhir yasyacam adis tad vrddham",
    "वृद्धिर्यस्याचामादिस्तद् वृद्धम्",
    "वृद्धिः यस्य अचाम् आदिः तत् वृद्धम्",
    "vṛddha",
    "vrddha",
    "वृद्ध"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "vfdDi",
    "Adi",
    "vfdDa",
    "saMjYA"
  ],

  pratyaharas: [
    "ac"
  ],

  adhikara: "",
  anuvritti: "",

  uddeshya: "यस्य अचाम् आदिः वृद्धिः",
  vidheya: "वृद्धम्",

  meaning: "An expression whose first vowel is a vṛddhi vowel is called vṛddha.",

  explanation: "This sūtra defines the technical term वृद्ध. In a word or expression, look at the first vowel among its vowels. If that first vowel is a vṛddhi vowel — आ, ऐ, or औ — then the expression is called vṛddha.",

  examples: [
    {
      slp1: "Aditi",
      note: "The first vowel is आ, a vṛddhi vowel, so the word is vṛddha."
    },
    {
      slp1: "Eka",
      note: "The first vowel is ऐ, so the word is vṛddha."
    },
    {
      slp1: "Odumbara",
      note: "The first vowel is औ, so the word is vṛddha."
    }
  ],

  related: [
    "1.1.1"
  ],

  notes: "This rule depends on the definition of वृद्धि in 1.1.1. The important point is not the first sound of the word, but the first vowel among the ac sounds."
},

{
  id: "1.1.74",
  slp1: "tyadAdIni ca",
  slp1Display: "tyadAdIni ca",

  searchAliases: [
    "tyadādīni ca",
    "tyadadini ca",
    "त्यदादीनि च",
    "त्यद् आदीनि च",
    "tyadadi",
    "tyadādi",
    "वृद्ध"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "tyadAdi",
    "Adi",
    "vfdDa",
    "saMjYA"
  ],

  pratyaharas: [],

  adhikara: "",
  anuvritti: "वृद्धम्",

  uddeshya: "त्यदादीनि",
  vidheya: "वृद्धम्",

  meaning: "The words beginning with tyad are also called vṛddha.",

  explanation: "This sūtra extends the designation वृद्ध beyond the phonetic condition stated in 1.1.73. Even if these words do not have a vṛddhi vowel as their first vowel, the group beginning with त्यद् is also given the technical name वृद्ध.",

  examples: [
    {
      slp1: "tyad",
      note: "The word त्यद् belongs to the tyadādi group and is called vṛddha by this rule."
    },
    {
      slp1: "tad",
      note: "Words in this pronominal group are included under the tyadādi listing."
    },
    {
      slp1: "vfdDa",
      note: "The designation वृद्ध is extended here by list, not by first-vowel condition."
    }
  ],

  related: [
    "1.1.73"
  ],

  notes: "This rule should be read with 1.1.73. Rule 1.1.73 defines वृद्ध by first-vowel condition; 1.1.74 extends वृद्ध-saṃjñā to the tyadādi group."
},

{
  id: "1.1.75",
  slp1: "eN prAcAM deSe",
  slp1Display: "eN prAcAM deSe",

  searchAliases: [
    "eṅ prācāṃ deśe",
    "eng pracham deshe",
    "एङ् प्राचां देशे",
    "एङ् प्राचाम् देशे",
    "pracam",
    "prācām",
    "desha",
    "deśa",
    "देश",
    "वृद्ध"
  ],

  type: "saMjYA",
  typeDisplay: "संज्ञा-सूत्र",

  glossary: [
    "prAc",
    "deSa",
    "vfdDa",
    "saMjYA"
  ],

  pratyaharas: [
    "eN"
  ],

  adhikara: "",
  anuvritti: "यस्य अचाम् आदिः; वृद्धम्",

  uddeshya: "प्राचां देशे एङ् यस्य अचाम् आदिः",
  vidheya: "वृद्धम्",

  meaning: "In eastern country-names, an expression whose first vowel is eṅ is called vṛddha.",

  explanation: "This sūtra extends the designation वृद्ध in a specific domain. In the usage of the eastern grammarians, when a country-name has एङ् as the first vowel among its vowels, that expression receives the technical designation वृद्ध.",

  examples: [
    {
      slp1: "eRIpacanIya",
      note: "A derivative connected with the country-name एणीपचन; used as a traditional example."
    },
    {
      slp1: "BojakawIya",
      note: "A derivative connected with भोजकट; cited as an example in the eastern-country context."
    },
    {
      slp1: "gonardIya",
      note: "A derivative connected with गोनर्द; another traditional example."
    }
  ],

  related: [
    "1.1.73",
    "1.1.74"
  ],

  notes: "This completes the first pāda. It should be read with the वृद्ध-saṃjñā rules 1.1.73–1.1.74. The condition is restricted by प्राचाम् and देशे, so it concerns eastern country-names/usages, not every word beginning with ए or ओ."
}
];