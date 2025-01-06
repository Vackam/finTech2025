# main.py

from fastapi import FastAPI
from routers.UserInput import InputRouter, InputData
import uvicorn

app = FastAPI()

app.include_router(InputRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
