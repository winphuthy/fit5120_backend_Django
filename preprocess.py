from transformers import BertForPreTraining,BertTokenizer
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def preprocess(text):
    # Lowercase the text
    text = str(text).lower()

    # Remove special characters and symbols
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # Remove \n symbol
    text = re.sub(r'\n','',text )
    # Remove multiple spaces
    text = re.sub('\s+', ' ', text)
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    text = ' '.join(tokens)

    return text