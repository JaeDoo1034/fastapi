from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # FASTAPI에 CORS 예외 URL 등록.

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/hello")
def hello():
    return {"message" : "Hello"}