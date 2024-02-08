# --------------------- 질문 데이터  --------------------- #

############# 질문 저장하기 #############
from models import Question, Answer
from datetime import datetime
import os
print(os.getcwd())

q = Question(subject = "pybo가 무엇인가요?", content = "pybo에 대해서 알고 싶습니다.",create_date = datetime.now())

# db세션 객체를 이용하여 데이터베이스에 데이터를 저장.
from database import SessionLocal
db = SessionLocal()
db.add(q)
db.commit()
print(fr"방금 생성한 데이터의 id : {q.id}")

q = Question(subject = "FASTAPI 모델 질문입니다.", content='id는 자동으로 생성 되나요?', create_date = datetime.now())
db.add(q)
db.commit() # 커밋하면 취소할 수 없음. 수행한 작업을 취소하려면 커밋 이전에 진행해야 함(db.rollback()
print(fr"방금 생성한 데이터의 id : {q.id}")

############# 데이터 조회하기 #############
print(fr"데이터 전부 표현 : {db.query(Question).all()}")
print(fr"id가 1인 질문만 조회 filter 함수 이용 : {db.query(Question).filter(Question.id==1).all()}")
print(fr"id가 1인 질문만 조회 get 함수 이용 (곧 없어짐): {db.query(Question).get(1)}")
print(fr"like 검색으로 FASTAPI 문자열이 포함된 질문만 조회 : {Question.subject.like('FASTAPI%')}")

############# 데이터 수정하기 #############
q = db.query(Question).get(2)
print(fr"q 의 id 값은? : {q.id}")
q.subject = 'FastAPI Model Question'
print(fr"q의 subject ? : {q.subject}")
db.commit()

############# 데이터 삭제하기 #############
# q = db.query(Question).get(1)
# db.delete(q)
# print("삭제 완료!")
# db.commit() # 삭제 역시 commit 필요.


# --------------------- 답변 데이터 --------------------- #


############# 데이터 저장하기 #############
from datetime import datetime
from models import Question, Answer
from database import SessionLocal
db = SessionLocal()
q = db.query(Question).get(2)
a = Answer(question = q, content = '네 자동으로 생성됩니다.', create_date=datetime.now())
# Anwser 모델 관려 추가 설명
# - 어떤 질문에 해당하는 답변인지 연결할 목적으로 question_id 속성이 있다.
# - Answer 모델의 객체를 생성할 때 question에 q를 대입하면 question_id 에 값을 지정하지 않아도 자동으로 입력되어 저장된다.

db.add(a)
db.commit()

print(fr"질문 a의 id : {a.id}")
a = db.query(Answer).get(1)
print(fr"db로 조회한 Answer 모델 내 첫 번째 데이터의 id : {a.id}")

print(db.query(Question).order_by(Question.create_date.desc()))
print(db.query(Question).order_by(Question.create_date.desc()).all())
# Answer 모델과 Question 모델 간 question relationship 다시 확인하기! (1/29)