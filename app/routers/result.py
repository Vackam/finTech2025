# result.py

from fastapi import APIRouter, Form, HTTPException, Request
from utils.templates import templates

ResultRouter = APIRouter(prefix = '/result')

@ResultRouter.get("/", tags=['result'])
async def read_output(request: Request):
    return templates.TemplateResponse("result.html", {"request": request})

@ResultRouter.get("/test", tags=['result'])
async def test_output(request: Request):
    return {"Test": 1}
