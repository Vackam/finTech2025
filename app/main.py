# main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

from routers.UserInput import InputRouter, InputData
from routers.auth import AuthRouter
from routers.intrance import IntranceRouter
from routers.result import ResultRouter
from routers.mainPage import MainRouter
from utils.templates import templates

import uvicorn

app = FastAPI()

app.include_router(InputRouter)
app.include_router(AuthRouter)
app.include_router(MainRouter)
app.include_router(IntranceRouter)
app.include_router(ResultRouter)
# 정적 파일(예: CSS, JS) 제공 설정 (필요 시)
# css 파일 건드릴 때 개방
app.mount("/style", StaticFiles(directory="style"), name="style")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return RedirectResponse(url="/intrance")
if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
