import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
# Import your functions here
from preprocess import in_preprocess
from spam_dect import spam_dect
from password_ev import password_evaluator

# Define your FastAPI app
app = FastAPI()

# Define the input data schema
class Message(BaseModel):
    text: str

class PasswordRequest(BaseModel):
    password: str

# Define the endpoint for spam detection
@app.post("/spam-detection/")
async def predict_spam(message: Message):
    # Preprocess the message
    preprocessed_text = in_preprocess(message.text)
    
    # Call your spam detection function
    result,result_num = spam_dect(preprocessed_text)
    
    # Return the prediction as a response
    return {"result": result,"result_percentage":result_num}

# Define the endpoint for spam detection
@app.post("/evaluate_password/")
async def password_evaluation(message: PasswordRequest):
    password = message.password

    color, result_str = password_evaluator(str(password))
    
    # Return the prediction as a response
    return {"color": color,"result_percentage":result_str}

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8999)

