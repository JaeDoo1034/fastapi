from pydantic import BaseModel
from typing import List,Optional
from fastapi import Form

class Todo(BaseModel):
    id : Optional[int]
    item : str # pydantic은 중첩해서 사용할 수 있음.

    class Config:
        schema_extra = {
            "example" : {
                "id" : 1,
                "item" : "Example Schema!"
            }
        }
    @classmethod
    def as_form(
        cls,
        item:str = Form(...)
        ):
        return cls(item=item)



# UPDATE 라우트의 요청용 바디 모델
class TodoItem(BaseModel):
    item : str

    class Config:
        schema_extra = {
            "example" : {
                "item" : "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos : List[TodoItem]

    class Config:
        schema_extra = {
            "example" : {
                "todos" : [
                    {
                        "item" : "Example Schema 1!"
                    },
                    {
                        "item" : "Example Schema 2!"
                    }
                ]
            }
        }