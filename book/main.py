from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()
app.include_router(user_router,prefix='/user')
app.include_router(event_router,prefix='/event')

if __name__ == "__main__":
    uvicorn.run("main:app",host='127.0.0.1',port = 8000, reload = True)

"""
1.
HTTP 통신에서 Accept와 Content-Type은 요청과 응답의 헤더 부분에 사용되는 필드입니다.

Accept: 클라이언트가 서버에게 받아들일 수 있는 콘텐츠 유형(미디어 타입)을 지정합니다.
이 필드는 클라이언트가 선호하는 응답 유형을 서버에 알려주는 역할을 합니다. 
예를 들어, 클라이언트가 JSON 형식의 응답을 선호한다면, Accept: application/json과 같이 설정할 수 있습니다. 
서버는 이 정보를 활용하여 클라이언트에게 가장 적합한 응답을 제공할 수 있습니다.

Content-Type: 클라이언트가 서버에게 전송하는 요청의 콘텐츠 유형을 지정합니다. 
이 필드는 요청 본문(body)의 유형을 명시합니다. 예를 들어, 클라이언트가 JSON 형식의 데이터를 서버로 전송하려고 한다면, 
Content-Type: application/json과 같이 설정해야 합니다. 
서버는 이 정보를 활용하여 요청 본문을 올바르게 해석할 수 있습니다.

FastAPI는 웹 애플리케이션 개발을 위한 Python 프레임워크로, 클라이언트와 서버 간의 통신을 처리하는 데 사용될 수 있습니다. 
따라서 Accept와 Content-Type 헤더 필드를 사용하여 클라이언트가 요청하는 콘텐츠 유형과 서버가 응답하는 콘텐츠 유형을 지정할 수 있습니다. 
이를 통해 클라이언트와 서버 간의 통신이 원활하게 이루어질 수 있습니다.


2.
첫 번째 cURL 명령어는 http://127.0.0.1:8000/event/와 같이 슬래시로 끝나는 URL을 사용하고 있습니다.

두 번째 cURL 명령어는 http://127.0.0.1:8000/event와 같이 슬래시로 끝나지 않는 URL을 사용하고 있습니다.


이 두 가지 차이는 서버 측에서 URL 경로를 해석하는 방식에 영향을 줄 수 있습니다. 
일반적으로, 슬래시로 끝나는 URL (/event/)은 해당 엔드포인트의 정확한 경로를 가리키는 것으로 간주됩니다. 
반면 슬래시 없는 URL (/event)은 해당 경로에 대한 일반적인 요청을 의미할 수 있습니다.

"""