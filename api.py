from fastapi import FastAPI
from todo import todo_router

# 단일 경로만 고려하는 애플리케이션
app = FastAPI()

@app.get('/')
async def welcome() -> dict :
    return {
        "message" : "Hello world"
    }

app.include_router(todo_router)
