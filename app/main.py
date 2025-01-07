# main.py

from fastapi import FastAPI
from routers.UserInput import InputRouter, InputData
from routers.Login import LoginRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

import uvicorn

app = FastAPI()

app.include_router(InputRouter)
app.include_router(LoginRouter)

# 정적 파일(예: CSS, JS) 제공 설정 (필요 시)
# css 파일 건드릴 때 개방
# app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 설정
views = Jinja2Templates(directory="views")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return views.TemplateResponse("main.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
