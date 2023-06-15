
from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)

"""
tags 파라미터는 FastAPI의 APIRouter 클래스에서 사용되는 옵션입니다. 이 파라미터를 사용하여 API 경로에 태그를 지정할 수 있습니다.
태그는 API 문서 생성에 사용되며, API의 엔드포인트를 그룹화하거나 분류하는 데 도움이 됩니다. 
Swagger UI나 Redoc과 같은 API 문서 생성 도구에서는 이러한 태그를 사용하여 API를 쉽게 찾을 수 있습니다.
"""

users = {}

@user_router.post("/signup")
async def sign_new_user(data:User) -> dict:
# 사용자를 등록하기 전 데이터베이스에 비슷한 이메일이 존재하는 지 확인
    if data.email in users:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with supplied username exists"
        )
    users[data.email] = data
    return {
        "message" : "User successfully registered"
    }

@user_router.post('/signin')
async def sign_user_in(user:UserSignIn) -> dict:
# 로그인하려는 사용자가 데이터베이스에 있는 지 먼저 확인, 없으면 예외 발생
    if user.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User does not exist"
        )
# 사용자가 존재하면 패스워드가 일치하는 지 확인해서 성공 또는 실패 메세지 반환
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Wrong credentials passed"
        )
    return {
        "message" : "User signed in successfully"
    }
