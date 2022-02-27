from fastapi import FastAPI
from typing import Optional
import pickle
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return "Arany nyaklanc prediktalashoz meghivas: /predict?weight=2.0"

@app.get("/predict/{weight}")
def read_item(weight: int, q: Optional [str] = None):
    model = pickle.load(open('nyaklanc_first_rf.pickle', 'rb'))
    width = 7.1
    
    pred = model.predict(pd.DataFrame({'weight': [weight], 'width': [width]}))
    # http://127.0.0.1:8000/items/5?q=sas
    return {"predicted price": pred}


#     //main.py
# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)


# host on heroku in 6 mins: https://www.youtube.com/watch?v=H7zAJf20Moc


# import pickle
# from pydantic import BaseModel
# class Features(BaseModel):
#      Persons_age: float
#      Gender: float
#      Height_in_cm: float
#      Weight_in_kg: float
#      Upper_blood_pressure: float
#      Lower_blood_pressure: float
#      Cholesterol_level: float
#      Glucose_level: float
#      Smoking_status: float
#      Alcohol_status: float 
# model = pickle.load(open('Healthcare.pkl', 'rb'))
# app = FastAPI()
# @app.get("/")
# def home():
#     return {'ML model for cardiac arrest prediction'}
# @app.post('/predict')
# def predict(data: Features):
#     data = data.dict()
#     Persons_age = data['Persons_age']
#     Gender = data['Gender']
#     Height_in_cm = data['Height_in_cm']
#     Weight_in_kg = data['Weight_in_kg']
#     Upper_blood_pressure = data['Upper_blood_pressure']
#     Lower_blood_pressure = data['Lower_blood_pressure']
#     Cholesterol_level = data['Cholesterol_level']
#     Glucose_level = data['Glucose_level']
#     Smoking_status = data['Smoking_status']
#     Alcohol_status = data['Alcohol_status']
#     pred = model.predict([[Persons_age, Gender, Height_in_cm, Weight_in_kg, Upper_blood_pressure,
#                         Lower_blood_pressure, Cholesterol_level, Glucose_level, Smoking_status, Alcohol_status]])
#     def statement():
#         if pred == 0:
#             return 'Result:- The model has predicted that you will not suffer from any cardic arresst but you should take care of your self.'
#         elif pred == 1:
#             return 'Result:- You should consult with doctor, The model has predicted that you will suffer form cardic arrest.'
#     return {'prediction':statement()}

# cron-job/koffeine heroku 30min limit ellen: https://towardsdatascience.com/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9
# cron-job.org
# http://kaffeine.herokuapp.com/#decaf

# BeautifulSoup
# https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/