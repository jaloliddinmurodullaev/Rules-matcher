import asyncio
from fastapi import FastAPI

from matchers.rules import home

app = FastAPI(title="Rules Matecher API", version="1.0",
              description="Rules Matcher module that applies all rules to Content microservice")

@app.get('/')
async def root():
    return {"message": 'hello'}

@app.get("/main/")
async def main():
    await asyncio.sleep(3)
    return {"status": "success"}

@app.get("/home/")
async def main_home():
    response = await home()
    return response



