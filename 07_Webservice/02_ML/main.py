# pip install fastapi
# pip install "uvicorn[standard]"
# >uvicorn main:app --reload



import os 
import joblib 
from fastapi import FastAPI
from pathlib import Path 


os.chdir(Path(__file__).parent)



# 1. Create Fast API Application
app = FastAPI() 


# 2. Root 
@app.get("/")
def root():
    return {"message": "Welcome by Webservice ML WBS"} 


@app.get("/predict")
def predict_area_price(area:int):
    
    # Load the model 
    model = load_model()

    # Predict the price using the model 
    predicted_price = int(model.predict( [ [area]]))

    # Return the result  
    return {
        "requiredarea": area,
        "predictedprice": predicted_price,
        "message": "Good luck"
    }



def load_model():
    model = joblib.load("./models/model_linear_reg_v2.jlb")
    return model