from fastapi import APIRouter

from database import get_db
from models import Question

#  --- 라우터 파일에 반드시 필요한 것은 APIRouter클래스로 생성한 router객체.
#  --- router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작.
# * 라우팅 : FASTAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위. *

# prefix : 요청 URL 에 항상 포함되어야 하는 것.
# 이 라우터는 /api/question 이라는 Path가 포함된 URL이 실행되어야 동작.
router = APIRouter(
    prefix="/api/question",
)

# db세션을 생성하고 해당 세션을 이용하여 질문 목록을 조회하여 리턴하는 함수
# db 세션 객체를 생성한 후에 db.close()를 수행하지 않으면 SQLAlchemy가 사숑하는 커넥션 풀에 db세션이 반환되지 않는다.
@router.get("/list")
def question_list():
    
    # contextlib의 contextmanager 사용
    with get_db() as db:
      _question_list = db.query(Question).order_by(Question.create_date.desc()).all()  
    
    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # db.close() # 사용한 세션을 커넥션 풀에 반환하는 함수. (세션 종료가 아니다!)
    return _question_list
