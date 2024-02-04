import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 접속 주소.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./myapi.db' # sqlite3 데이터베이스의 파일. 프로젝트 루트 디렉터리에 저장한다는 뜻.


# connection pool 생성.
# 커넷션 풀 : 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것.
# 용도 : 데이터베이스에 접속하는 세션수를 제어하고, 또 세션 접속에 소요되는 시간을 줄이고자 하는 용도
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" : False}
)

# 데이터베이스에 접속하기 위해 필요한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)
# autocommit : False > commit 이라는 사인을 주어야만 실제 저장. 데이터를 잘못 저장했을 경우 rollback 가능.

# Base : 데이터베이스 모델을 구성할 때 사용되는 클래스
Base = declarative_base()

@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()