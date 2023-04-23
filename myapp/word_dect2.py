# %%
import re
import nltk
nltk.download('punkt')
import string
import pandas as pd
ban_wds = pd.read_csv('swearWords.csv',header=None)
ban_wds = ban_wds.values.tolist()[0]
#Filter function
def word_dect(text):
    text_cln = text.lower()
    text_cln = re.sub('[^A-Za-z0-9]+', ' ', text_cln) #word tokenization and preporcessing
    text_cln = re.sub(r'[^\w\s]', '', text_cln)
    tokens = nltk.word_tokenize(text_cln)
    for i in tokens:
        if i in ban_wds:
            return 'Sensitive word detected!' 
            break
        else:
            continue
    return text

# %%



