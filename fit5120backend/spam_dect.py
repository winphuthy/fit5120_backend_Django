from preprocess import preprocess
from transformers import BertForSequenceClassification, BertTokenizer
import torch

def spam_dect(text):
    # Load the saved model state dictionary
    path = '/Django/fit5120backend/to_use.pth'
    state_dict = torch.load(path)

    # Instantiate the model class and load the saved state dictionary
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
    model.load_state_dict(state_dict)

        # Move the model to the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    # Tokenize the text
    text = preprocess(text)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    inputs.to(device)

    # Pass the input through the model to get the logits
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # Get the predicted label
    _, predicted_label = torch.max(logits, dim=1)

    # Print the percentage of label 1
    label_1_percentage = torch.softmax(logits, dim=1)[0][1].item() * 100 
    return "RESULT: Your message is " + str(round(label_1_percentage,2))+ " percent chance to be a scam."