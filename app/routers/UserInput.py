from fastapi import APIRouter, Form, HTTPException, Request
from typing import Annotated
from pydantic import BaseModel
from utils.templates import templates
from utils.ai_toolkit import get_insurance_model
import models
import json

class InputData(BaseModel):
    sleepingTime: str
    eatingHabits: str
    # Add additional parameters for input if needed

InputRouter = APIRouter(prefix="/input")

@InputRouter.get("/", tags=['input'])
async def start_input():
    return {"message": "Hello World in userInput"}

@InputRouter.post("/data", tags=['input'])
async def process_input(
    request: Request,
    sex: int = Form(...),
    age: int = Form(...),
    allownc: int = Form(...),
    npins: int = Form(...),
    ec_occp: int = Form(...),
    he_obe: int = Form(...),
    bd1_11: int = Form(...),
    bd2_14: int = Form(...),
    bp16_1: int = Form(...),
    bp16_2: int = Form(...),
    bs3_1: int = Form(...),
    be5_1: int = Form(...),
    he_fh: int = Form(...),
    he_hpfh1: int = Form(...),
    he_hpfh2: int = Form(...),
    he_hpfh3: int = Form(...),
    he_hlfh1: int = Form(...),
    he_hlfh2: int = Form(...),
    he_hlfh3: int = Form(...),
    he_ihdfh1: int = Form(...),
    he_ihdfh2: int = Form(...),
    he_ihdfh3: int = Form(...),
    he_strfh1: int = Form(...),
    he_strfh2: int = Form(...),
    he_strfh3: int = Form(...),
    he_dmfh1: int = Form(...),
    he_dmfh2: int = Form(...),
    he_dmfh3: int = Form(...),
):
    input_data = [
        age, sex, allownc, npins, ec_occp, he_obe, bd1_11, bd2_14,
        bp16_1, bp16_2, bs3_1, be5_1, he_fh,
        he_hpfh1, he_hpfh2, he_hpfh3, he_hlfh1, he_hlfh2, he_hlfh3,
        he_ihdfh1, he_ihdfh2, he_ihdfh3, he_strfh1, he_strfh2, he_strfh3,
        he_dmfh1, he_dmfh2, he_dmfh3,
    ]

    try:
        model = models.IntegratedInsuranceModel()
        result = model.predict([input_data])

        ai_recommend = get_insurance_model(result)
        ai_recommend = json.loads(ai_recommend)
        
        return templates.TemplateResponse(
            name="result.html", 
            context={"request": request, "result": result, "recommend_insurance": ai_recommend}  # Replace None with ai_recommend after testing
        )
    except ImportError as e:
        raise HTTPException(status_code=500, detail=f"ImportError: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@InputRouter.post("/test", tags=['input'])
async def test_input(
    sleepingTime: str = Form(...), 
    eatingHabits: str = Form(...)
):
    return {"sleepingTime": sleepingTime, "eatingHabits": eatingHabits}

