from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch
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

def spam_dect(text):
    # Load the saved model state dictionary
    model_path = 'static/model_backup'
    path = 'static/to_use.pth'
    state_dict = torch.load(path)

    # Instantiate the model class and load the saved state dictionary
    model = AutoModelForSequenceClassification.from_pretrained(model_path,num_labels = 2)
    model.load_state_dict(state_dict)

        # Move the model to the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    # Tokenize the text
    text = preprocess(text)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    inputs.to(device)
    input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)

    # Pass the input through the model to get the logits
    with torch.no_grad():
        outputs = model(**inputs,output_attentions=True)
        logits = outputs.logits
        attentions = outputs.attentions[0]
    avg_attentions = torch.mean(attentions, dim=1)[0]

    # Get the predicted label
    _, predicted_label = torch.max(logits, dim=1)

    # Get the important words
    important_words = []
    for i in torch.topk(avg_attentions, k=3).indices:
        important_words.append(tokenizer.decode(input_ids[0][i].tolist()))

    # Print the percentage of label 1
    label_1_percentage = torch.softmax(logits, dim=1)[0][1].item() * 100 
    label_1_str = None
    if label_1_percentage > 85:
        label_1_str = 'very high chance'
    elif label_1_percentage > 70:
        label_1_str = 'high chance'
    elif label_1_percentage > 50:
        label_1_str = 'decent chance'
    elif label_1_percentage > 20:
        label_1_str = 'low chance'
    else:
        label_1_str = 'very low chance'
        result_str = f"Your message has a {label_1_str} to be a scam, however please still be caution. {str(important_words[:1])} are the words that contributing the most to this prediction."
        label_1_percentage = round(label_1_percentage,2)
        return result_str,label_1_percentage
    
    result_str = f"Your message has a {label_1_str} to be a scam. {str(important_words[:1])} are the words that contributing the most to this prediction."
    label_1_percentage = round(label_1_percentage,2)
    return result_str,label_1_percentage