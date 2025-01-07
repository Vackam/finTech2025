# Login.py

from fastapi import APIRouter, Form, HTTPException
from typing import Annotated
from pydantic import BaseModel
import models

class LoginData(BaseModel):
    str_id: str
    str_password: str

LoginRouter = APIRouter(prefix = '/auth/login')

@LoginRouter.get("/", tags=['login'])
async def login_render():
    return views.TemplateResponse("login.html", {"request" : request})
