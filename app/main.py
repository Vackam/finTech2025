# main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from routers.UserInput import InputRouter, InputData
from routers.auth import AuthRouter
from utils.templates import templates

import uvicorn

app = FastAPI()

app.include_router(InputRouter)
app.include_router(AuthRouter)

# 정적 파일(예: CSS, JS) 제공 설정 (필요 시)
# css 파일 건드릴 때 개방
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
