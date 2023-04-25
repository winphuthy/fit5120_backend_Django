import re
import nltk
nltk.download('punkt')
import string

ban_wds = ['anal',
 'anus',
 'arse',
 'ass',
 'ballsack',
 'balls',
 'bastard',
 'bitch',
 'biatch',
 'bloody',
 'blowjob',
 'blow job',
 'bollock',
 'bollok',
 'boner',
 'boob',
 'bugger',
 'bum',
 'butt',
 'buttplug',
 'clitoris',
 'cock',
 'coon',
 'crap',
 'cunt',
 'damn',
 'dick',
 'dildo',
 'dyke',
 'fag',
 'feck',
 'fellate',
 'fellatio',
 'felching',
 'fuck',
 'f u c k',
 'fudgepacker',
 'fudge packer',
 'flange',
 'Goddamn',
 'God damn',
 'hell',
 'homo',
 'jerk',
 'jizz',
 'knobend',
 'knob end',
 'labia',
 'lmao',
 'lmfao',
 'muff',
 'nigger',
 'nigga',
 'omg',
 'penis',
 'piss',
 'poop',
 'prick',
 'pube',
 'pussy',
 'queer',
 'scrotum',
 'sex',
 'shit',
 's hit',
 'sh1t',
 'slut',
 'smegma',
 'spunk',
 'tit',
 'tosser',
 'turd',
 'twat',
 'vagina',
 'wank',
 'whore',
 'wtf',
 'sucker',
 'pornhub',
 'xvideo',
 'assfuck',
 'chinkchong',
 'nigger',
 'chinkn',
 'negro',
 'smalleye',
 'porn',
 'pron']
#Filter function
def word_dect(text):
    text_cln = text.lower()
    text_cln = re.sub('[^A-Za-z0-9]+', ' ', text_cln) #word tokenization and preporcessing
    text_cln = re.sub(r'[^\w\s]', '', text_cln)
    tokens = nltk.word_tokenize(text_cln)
    if len(tokens) > 2: # check if the number of tokens is larger than 2
        return False
    for i in tokens:
        if i in ban_wds:
            return False
            break
        else:
            continue
    return True



