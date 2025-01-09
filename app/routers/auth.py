# auth.py

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from typing import Annotated
from pydantic import BaseModel

from utils.templates import templates

import models

class LoginData(BaseModel):
    str_id: str
    str_password: str

AuthRouter = APIRouter(prefix = '/auth')

# For Prototype, Using fake db
fake_user_db = {
        "user1": "password1",
        "user2": "password2",
        }

# rendering to login page
@AuthRouter.get("/login", tags=['login'])
async def render_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request" : request})

@AuthRouter.post("/login", tags=['login'])
async def login(
            request: Request,
            username: str = Form(...),
            password: str = Form(...),
        ):
    if username in fake_user_db and fake_user_db[username] == password:
        # TODO: 일단 메인페이지로 보냄
        response = RedirectResponse(url="/", status_code=303)
        return response
    else:
        {"return": "존재하지 않는 유저"}
