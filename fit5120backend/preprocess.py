from transformers import BertForPreTraining,BertTokenizer
import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
stopwords = set(stopwords.words('english'))
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
    tokens = word_tokenize(text)
    
    tokens = [token for token in tokens if token not in stopwords]
    text = ' '.join(tokens)

    return text