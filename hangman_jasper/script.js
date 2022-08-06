// List of words
// import * as fs from 'fs'; 
const a_span = document.getElementById('a');
const b_span = document.getElementById('b');
const c_span = document.getElementById('c');
const d_span = document.getElementById('d');
const e_span = document.getElementById('e');
const f_span = document.getElementById('f');
const g_span = document.getElementById('g');
const h_span = document.getElementById('h');
const i_span = document.getElementById('i');
const j_span = document.getElementById('j');
const k_span = document.getElementById('k');
const l_span = document.getElementById('l');
const m_span = document.getElementById('m');
const n_span = document.getElementById('n');
const o_span = document.getElementById('o');
const p_span = document.getElementById('p');
const q_span = document.getElementById('q');
const r_span = document.getElementById('r');
const s_span = document.getElementById('s');
const t_span = document.getElementById('t');
const u_span = document.getElementById('u');
const v_span = document.getElementById('v');
const w_span = document.getElementById('w');
const x_span = document.getElementById('x');
const y_span = document.getElementById('y');
const z_span = document.getElementById('z');
const word_div = document.getElementById('word');
const usedLetters_p = document.querySelector(".used-letters p");
const gallows_img = document.querySelector(".gallow img");
const message_div = document.querySelector(".message");
const winLose_h1 = document.querySelector('#win-lose h1');
const continueButton_p = document.querySelector("#win-lose p");
var errors = 0;
const wrongGuesses = [];
const usedLetters = [];





// setTimeout(function(){ gallows_img.src = images[6]}, 5000)



var words = [
    "ability", "about", "above", "accept", "according", "account", "across", 
    "action", "activity", "actually", "address", "admit", "adult", "affect", 
    "after", "again", "against", "agency", "agent", "agree", "agreement", "ahead",
    "allow", "almost", "alone", "along", "already", "although", "always", "american",
    "among", "amount", "analysis", "animal", "another", "answer", "anyone", "anything",
    "appear", "apply", "approach", "argue", "around", "arrive", "article", "artist",
    "assume", "attack", "attention", "attorney", "audience", "author", "authority",
    "available", "avoid", "beautiful", "because", "become", "before", "begin", "behavior",
    "behind", "believe", "benefit", "better", "between", "beyond", "billion", "black",
    "blood", "board", "break", "bring", "brother", "budget", "build", "building",
    "business", "camera", "campaign", "cancer", "candidate", "capital", "career",
    "carry", "catch", "cause", "center", "central", "century", "certain", "certainly",
    "chair", "challenge", "chance", "change", "character", "charge", "check", "child",
    "choice", "choose", "church", "citizen", "civil", "claim", "class", "clear", "clearly",
    "close", "coach", "collection", "college", "color", "commercial", "common", "community",
    "company", "compare", "computer", "concern", "condition", "conference", "congress",
    "consider", "consumer", "contain", "continue", "control", "could", "country", "couple",
    "course", "court", "cover", "create", "crime", "cultural", "culture", "current", "customer",
    "daughter", "death", "debate", "decade", "decide", "decision", "defense", "degree",
    "democrat", "democratic", "describe", "design", "despite", "detail", "determine", "develop",
    "difference", "different", "difficult", "dinner", "direction", "director", "discover",
    "discuss", "discussion", "disease", "doctor", "dream", "drive", "during", "early",
    "economic", "economy", "education", "effect", "effort", "eight", "either", "election",
    "employee", "energy", "enjoy", "enough", "enter", "entire", "especially", "establish",
    "evening", "event", "every", "everybody", "everyone", "everything", "evidence",
    "exactly", "example", "executive", "exist", "expect", "experience", "expert", "explain",
    "factor", "family", "father", "federal", "feeling", "field", "fight", "figure", "final",
    "finally", "financial", "finger", "finish", "first", "floor", "focus", "follow", "force",
    "foreign", "forget", "former", "forward", "friend", "front", "future", "garden", "general",
    "generation", "glass", "government", "great", "green", "ground", "group", "growth", "guess",
    "happen", "happy", "health", "heart", "heavy", "herself", "himself", "history", "hospital",
    "hotel", "house", "however", "human", "hundred", "husband", "identify", "image", "imagine",
    "impact", "important", "improve", "include", "including", "increase", "indeed", "indicate",
    "individual", "industry", "inside", "instead", "interest", "interview", "investment", "involve",
    "issue", "itself", "kitchen", "knowledge", "language", "large", "later", "laugh", "lawyer", "leader",
    "learn", "least", "leave", "legal", "letter", "level", "light", "likely", "listen", "little", "local",
    "machine", "magazine", "maintain", "major", "majority", "manage", "management", "manager", "market",
    "marriage", "material", "matter", "maybe", "measure", "media", "medical", "meeting", "member", "memory",
    "mention", "message", "method", "middle", "might", "military", "million", "minute", "mission", "model",
    "modern", "moment", "money", "month", "morning", "mother", "mouth", "movement", "movie", "music",
    "myself", "nation", "national", "natural", "nature", "nearly", "necessary", "network", "never", 
    "newspaper", "night", "north", "nothing", "notice", "number", "occur", "offer", "office", "officer",
    "official", "often", "operation", "option", "order", "other", "others", "outside", "owner",
    "painting", "paper", "parent", "particular", "partner", "party", "patient", "pattern", "peace", 
    "people", "perform", "perhaps", "period", "person", "personal", "phone", "physical", "picture", 
    "piece", "place", "plant", "player", "point", "police", "policy", "political", "politics", "popular",
    "population", "position", "positive", "possible", "power", "practice", "prepare", "present", 
    "president", "pressure", "pretty", "prevent", "price", "private", "probably", "problem", "process",
    "produce", "product", "production", "professor", "program", "project", "property", "protect", 
    "prove", "provide", "public", "purpose", "quality", "question", "quickly", "quite", "radio",
    "raise", "range", "rather", "reach", "ready", "reality", "realize", "really", "reason", "receive",
    "recent", "recently", "recognize", "record", "reduce", "reflect", "region", "relate", "religious",
    "remain", "remember", "remove", "report", "represent", "republican", "require", "research",
    "resource", "respond", "response", "result", "return", "reveal", "right", "scene", "school",
    "science", "scientist", "score", "season", "second", "section", "security", "senior", "sense",
    "series", "serious", "serve", "service", "seven", "several", "sexual", "shake", "share",
    "shoot", "short", "should", "shoulder", "similar", "simple", "simply", "since", "single", 
    "sister", "situation", "skill", "small", "smile", "social", "society", "soldier", "somebody", 
    "someone", "something", "sometimes", "sound", "source", "south", "southern", "space", 
    "speak", "special", "specific", "speech", "spend", "sport", "spring", "staff", "stage", "stand", 
    "standard", "start", "state", "statement", "station", "still", "stock", "store", "story", "strategy",
    "street", "strong", "structure", "student", "study", "stuff", "style", "subject", "success", "successful",
    "suddenly", "suffer", "suggest", "summer", "support", "surface", "system", "table", "teach", "teacher",
    "technology", "television", "thank", "their", "themselves", "theory", "there", "these", "thing", "think", 
    "third", "those", "though", "thought", "thousand", "threat", "three", "through", "throughout", "throw", 
    "today", "together", "tonight", "total", "tough", "toward", "trade", "training", "travel", "treat", 
    "treatment", "trial", "trouble", "truth", "under", "understand", "until", "usually", "value", "various", 
    "victim", "violence", "visit", "voice", "watch", "water", "weapon", "weight", "western", "whatever",
    "where", "whether", "which", "while", "white", "whole", "whose", "window", "within", "without", "woman",
    "wonder", "worker", "world", "worry", "would", "write", "writer", "wrong", "young", "yourself"
];


const images = [
    'images/strike1.png',
    'images/strike2.png',
    'images/strike3.png',
    'images/strike4.png',
    'images/strike5.png',
    'images/dead.png',
    'images/super-dead.png',
];

function pickRandomWord () {
    var randomWord = words[Math.floor(Math.random()*614)];
    var runningWord = "_".repeat(randomWord.length);
    word_div.innerHTML =  runningWord.split('').join(' ');
    return { randomWord, runningWord };
};

function continueGame() {
    console.log("win")
    continueButton_p.innerHTML = "New Game?";
    console.log("win1");
    continueButton_p.addEventListener("click", function(){
        window.location.reload();
    });
}

function checkLetter (letter) {
    if (!usedLetters.includes(letter)) {

        usedLetters.push(letter);

        if (randomWord.includes(letter)) {

            for (let i = 0; i < runningWord.length; i++){

                if (randomWord[i] == letter) {
    
                    runningWord = runningWord.split('');
    
                    runningWord[i] = letter;
    
                    runningWord = runningWord.join('');

                    if (runningWord == randomWord) {
                        disableKeys();
                        winLose_h1.style.color = "greenyellow";
                        winLose_h1.innerHTML = "YOU WIN!";
                        message_div.innerHTML = "The word was: " + randomWord;
                        continueGame();
                    };
    
    
                };
            };
        } else {

            wrongGuesses.push(letter);

            if (errors < 5) {

                usedLetters_p.innerHTML = wrongGuesses.join(' ');
                gallows_img.src = images[errors];
                errors++;
                
            } else {
                disableKeys();
                gallows_img.src = images[errors];
                winLose_h1.style.color = "#ff0000";
                winLose_h1.innerHTML = "DEAD."
                setTimeout(function(){ gallows_img.src = images[errors+1]}, 1000);
                message_div.innerHTML = "The word was: " + randomWord;
                continueGame();
            };
        };



    } else {
        console.log('You have already guessed this letter!');
        message_div.innerHTML = "You have already guessed this letter"
        disableKeys();
        setTimeout(function(){
            message_div.innerHTML = "Guess a letter!";
            enableKeys();
        }, 2000)
    };

    word_div.innerHTML = runningWord.split('').join(' ')

};


function aListener(){checkLetter('a');};
function bListener(){checkLetter('b');};
function cListener(){checkLetter('c');};
function dListener(){checkLetter('d');};
function eListener(){checkLetter('e');};
function fListener(){checkLetter('f');};
function gListener(){checkLetter('g');};
function hListener(){checkLetter('h');};
function iListener(){checkLetter('i');};
function jListener(){checkLetter('j');};
function kListener(){checkLetter('k');};
function lListener(){checkLetter('l');};
function mListener(){checkLetter('m');};
function nListener(){checkLetter('n');};
function oListener(){checkLetter('o');};
function pListener(){checkLetter('p');};
function qListener(){checkLetter('q');};
function rListener(){checkLetter('r');};
function sListener(){checkLetter('s');};
function tListener(){checkLetter('t');};
function uListener(){checkLetter('u');};
function vListener(){checkLetter('v');};
function wListener(){checkLetter('w');};
function xListener(){checkLetter('x');};
function yListener(){checkLetter('y');};
function zListener(){checkLetter('z');};


function enableKeys() {
    a_span.addEventListener('click', aListener);
    b_span.addEventListener('click', bListener);
    c_span.addEventListener('click', cListener);
    d_span.addEventListener('click', dListener);
    e_span.addEventListener('click', eListener);
    f_span.addEventListener('click', fListener);
    g_span.addEventListener('click', gListener);
    h_span.addEventListener('click', hListener);
    i_span.addEventListener('click', iListener);
    j_span.addEventListener('click', jListener);
    k_span.addEventListener('click', kListener);
    l_span.addEventListener('click', lListener);
    m_span.addEventListener('click', mListener);
    n_span.addEventListener('click', nListener);
    o_span.addEventListener('click', oListener);
    p_span.addEventListener('click', pListener);
    q_span.addEventListener('click', qListener);
    r_span.addEventListener('click', rListener);
    s_span.addEventListener('click', sListener);
    t_span.addEventListener('click', tListener);
    u_span.addEventListener('click', uListener);
    v_span.addEventListener('click', vListener);
    w_span.addEventListener('click', wListener);
    x_span.addEventListener('click', xListener);
    y_span.addEventListener('click', yListener);
    z_span.addEventListener('click', zListener);
};

function disableKeys() {
    a_span.removeEventListener('click', aListener);
    b_span.removeEventListener('click', bListener);
    c_span.removeEventListener('click', cListener);
    d_span.removeEventListener('click', dListener);
    e_span.removeEventListener('click', eListener);
    f_span.removeEventListener('click', fListener);
    g_span.removeEventListener('click', gListener);
    h_span.removeEventListener('click', hListener);
    i_span.removeEventListener('click', iListener);
    j_span.removeEventListener('click', jListener);
    k_span.removeEventListener('click', kListener);
    l_span.removeEventListener('click', lListener);
    m_span.removeEventListener('click', mListener);
    n_span.removeEventListener('click', nListener);
    o_span.removeEventListener('click', oListener);
    p_span.removeEventListener('click', pListener);
    q_span.removeEventListener('click', qListener);
    r_span.removeEventListener('click', rListener);
    s_span.removeEventListener('click', sListener);
    t_span.removeEventListener('click', tListener);
    u_span.removeEventListener('click', uListener);
    v_span.removeEventListener('click', vListener);
    w_span.removeEventListener('click', wListener);
    x_span.removeEventListener('click', xListener);
    y_span.removeEventListener('click', yListener);
    z_span.removeEventListener('click', zListener);
};



var {randomWord, runningWord} =  pickRandomWord();
enableKeys();
console.log(runningWord);
console.log(randomWord);

// var audio = new Audio('audio_file.mp3');
// audio.play();
