# mainPage.py

from fastapi import APIRouter, Form, HTTPException, Request
from utils.templates import templates

MainRouter = APIRouter(prefix = '/main')

@MainRouter.get("/", tags=['main'])
async def read_main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
