import pickle
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,BaggingClassifier,StackingClassifier
from xgboost import XGBClassifier
import numpy as np
import pandas as pd

model_path = 'fit5120backend/static/stack_model.pkl'
vector_path = 'fit5120backend/static/vectorizer2.pkl'
common = pd.read_csv('fit5120backend/static/common.csv')

def password_evaluator(text):
    if text in list(common['password']):
         print('This is a common word, please do not use this as a password')
         return None

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(vector_path, "rb") as f:
        vectorizer = pickle.load(f)
    
    X = vectorizer.transform([text])
    y_pred = model.predict_proba(X)
    
    max_prob_index = y_pred.argmax(axis=1)[0]
    max_prob = y_pred[0, max_prob_index]
    
    if max_prob_index == 0:
        color = (int(max_prob * 255), 0, 0)  # Pure red
        result_str = f'Your password is too simplistic. We strongly recommend using a more intricate combination of uppercase and lowercase letters, as well as special characters, to enhance its complexity and strengthen its security.'
    elif max_prob_index == 1:
        color = (int(max_prob * 255), int(max_prob * 255), 0)  # Pure yellow
        result_str = f'Your password exhibits a reasonable level of strength; however, it may still be vulnerable to sophisticated hacking algorithms. Consider adding more '
    elif max_prob_index == 2:
        result_str = f'Great job on creating a highly robust password! To maintain your account security, we recommend periodically updating your password every 6 months to stay ahead of potential security risks.'
        color = (0, int(max_prob * 255), 0)  # Pure green
    else:
        # Handle the case where the max_prob_index is not within expected range
        color = (255, 255, 255)  # Default to white
        
    return color,result_str
