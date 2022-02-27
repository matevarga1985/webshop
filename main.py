from fastapi import FastAPI
# from typing import Optional
import pickle
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return "Arany nyaklanc árának prediktalashoz meghívásra példa: /predict?weight=1.2&width=10  (weight eseten a dimenzió gramm, width esetén mm)"

@app.get("/predict/")
def predict_price(weight: float, width: float):
    model = pickle.load(open('./nyaklanc_first_rf.pickle', 'rb'))

    pred = model.predict(pd.DataFrame({'weight': [weight], 'width': [width]}))[0]
    pred_rounded = round(pred, 2)
    return str(weight) + " grammos, " + str(width) + " mm szeles nyaklanc prediktalt ara: " + str(pred_rounded) + ' Ft'