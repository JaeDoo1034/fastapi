import sys
sys.path.append('/Users/yunjaedu/3_Resource/fastapi/projects/myapi')
from models import Question

from sqlalchemy.orm import Session


def get_question_list(db: Session):
    print(type(db))
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list