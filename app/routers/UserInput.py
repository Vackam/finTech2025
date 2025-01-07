# UserInput.py

from fastapi import APIRouter, Form, HTTPException
from typing import Annotated
from pydantic import BaseModel
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
        sleepingTime: str = Form(...),
        eatingHabits: str = Form(...)
        ):
    # For docs, set like this
    input_data = {
            "sleepingTime" : sleepingTime,
            "eatingHabits" : eatingHabits
            }
    # Test Code

    model = models.TestModel()
    
    try: 
        result = model.predict(input_data)
        return {"result" : result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@InputRouter.post("/test", tags=['input'])
async def test_input(sleepingTime: str=Form(...), eatingHabits: str=Form(...)):
    print(sleepingTime, eatingHabits)
    return {"sleepingTime": sleepingTime, "eatingHabits": eatingHabits}
     
