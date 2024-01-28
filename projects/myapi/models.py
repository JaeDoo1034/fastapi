# 모델 생성 : 질문모델 , 답변 모델

# 질문모델
'''
id : 질문 데이터의 고유 번호
subject : 질문 제목
content : 질문 내용
create_date : 질문 작성일시
'''

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Question(Base):
    __tablename__ = "question" # 모델에 의해 관리되는 테이블 이름

    id = Column(Integer, primary_key = True)
    subject = Column(String,primary_key = False,nullable = False)
    content = Column(Text,primary_key = False, nullable = False)
    create_date = Column(DateTime, primary_key = False,nullable = False)


# 답변모델
'''
id : 답변 데이터의 고유 번호
question_id : 질문 데이터의 고유 번호(어떤 질문에 달린 답변인지 알아야 하므로 질문 데이터의 고유번호가 필요)
content : 답변 내용
create_date : 답변 작성일시
'''


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer,primary_key = True)
    content = Column(Text, nullable = False)
    create_date = Column(DateTime, nullable = False)
    # 답변을 질문과 연결하기 위해 추가한 속성
    question_id = Column(Integer, ForeignKey("question_id"))
    # >> question 테이블의 id 컬럼과 연결된다는 뜻.


    question = relationship("Question",backref = "answers")