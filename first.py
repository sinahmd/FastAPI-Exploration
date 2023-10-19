from fastapi import FastAPI


app = FastAPI()

@app.get('/home/{name}/{age}')
def index(name:str, age:int=0):
    return {'message':f'{name} is {age} years old.'}
