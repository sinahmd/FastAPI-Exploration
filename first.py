from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel
from typing import Union
class User(BaseModel):
    name: str
    age: int = Path(ge=0, le=120)
    height: Union[float, None] = None

class UserIn(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    username:str
    email:str

app = FastAPI()
@app.post('/users/')
def get_index(user:User, car:str=Query('nothing, min_length=2, max_lenght=20')):
    return user, car
@app.post('/home/', response_model=UserOut, status_code=201)
def index(usr:UserIn):
    if usr.username == 'admin':
        raise HTTPException(detail="user can't be admin", status_code=400, headers={"X-error":"there goes my error"})
    return usr

