# UserInput.py

from fastapi import APIRouter, Form
from typing import Annotated
from pydantic import BaseModel

class InputData(BaseModel):
    sleepingTime: str
    eatingHabits: str
    # Add some parameter for input

InputRouter = APIRouter(prefix = '/input')

@InputRouter.get("/", tags=['input'])
async def start_input():
    return {"message": "Hello World in userInput"}

@InputRouter.post("/data", tags=['input'])
async def input(
        sleepingTime: str = Form(...),
        eatingHabits: str = Form(...)
        ):
    data = InputData(
            sleepingTime = sleepingTime,
            eatingHabits = eatingHabits
            )
    return data
