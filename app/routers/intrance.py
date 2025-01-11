# intrance.py

from fastapi import APIRouter, Form, HTTPException, Request
from utils.templates import templates

IntranceRouter = APIRouter(prefix = '/intrance')

@IntranceRouter.get("/", tags=['intrance'])
async def read_intrance(request: Request):
    return templates.TemplateResponse("intrance.html", {"request": request})
