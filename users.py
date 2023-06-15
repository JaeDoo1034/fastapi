from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 모델 생성
class User(BaseModel):
    email : EmailStr
    password : str
    events : Optional[List[Event]] # Event : events.py에서 정의한 Event 클래스(객체)

    # 샘플데이터 보여주기용 서브 클래스 생성
    class Config:
        schema_extra = {
            "example" : {
                "email" : "fastapi@packt.com",
                "username" : "strong!!",
                "events" : [],
            } 
        }


# 사용자 로그인 모댈 생성
class UserSignIn(BaseModel):
    email: EmailStr
    password : str

    class Config:
        schema_extra = {
            "example" : {
                "email" : "fastapi@packt.com",
                "password" : "strong!!",
                "events" : [],
            }
        }