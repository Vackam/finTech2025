# UserInput.py

from fastapi import APIRouter, Form, HTTPException, Request
from typing import Annotated
from pydantic import BaseModel
from utils.templates import templates
from utils.ai_toolkit import get_insurance_model

import json
import joblib
import models

class InputData(BaseModel):
    sleepingTime: str
    eatingHabits: str
    # Add some parameter for input

InputRouter = APIRouter(prefix = '/input')

@InputRouter.get("/", tags=['input'])
async def start_input():
    return {"message": "Hello World in userInput"}

@InputRouter.post("/data", tags=['input'])
async def process_input(
        request: Request,
        sleepingTime: str = Form(...),
        eatingHabits: str = Form(...)
        ):

    # For docs, set like this
    input_data = {
            "sleepingTime" : sleepingTime,
            "eatingHabits" : eatingHabits
            }

    try: 
        model = models.InsuranceModel()
        result = model.predict(input_data)

        ai_recommend = get_insurance_model(result)
        ai_recommend = json.loads(ai_recommend)
        return templates.TemplateResponse(
                name="result.html", context={"request": request, "result": result, "recommend_insurance": ai_recommend}
                ) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ImportError as e:
        print(f"ImportError 발생: {e}")
        raise HTTPException(status_code=500, detail=f"ImportError: {e}")

@InputRouter.post("/test", tags=['input'])
async def test_input(sleepingTime: str=Form(...), eatingHabits: str=Form(...)):
    print(sleepingTime, eatingHabits)
    return {"sleepingTime": sleepingTime, "eatingHabits": eatingHabits}
     
