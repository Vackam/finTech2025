# ml_test/main.py


from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import joblib
import os
import numpy as np
import xgboost as xgb

app = FastAPI()

'''
origins = [ "*" ] # 허용할 url 주소, *이면 모든 url에 대해 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware
'''
model_path = "C:/Users/uesr/Documents/GitHub/finTech2025/app/ml/insurance_model.joblib"

model = joblib.load(model_path)

test_input = [1, 2]


@app.get("/", response_class=HTMLResponse)
async def test_data(request: Request):
    prediction = model.predict([test_input]) 

    a = {"ML_TEST/MAIN" : prediction}

    print(prediction)
    return prediction[0]
if __name__ == "__main__":
    print(xgb.__version__)
