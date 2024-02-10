import datetime

from pydantic import BaseModel

# Question schema  생성.
class Question(BaseModel):
    id : int
    subject : str | None = None # 선택항목으로 설정. default 는 None
    content : str
    create_date : datetime.datetime

# 구버전 ORM 모드 호환 목적 
# 구버전(Pydantic V1) 사용할 경우, Question 모델은 Question 스키마로 자동변환되지 않는다.
# (_question_list의 함수의 리턴값이 딕셔너라기 아닌 Question 모델임)
class Config:
    orm_mode = True 