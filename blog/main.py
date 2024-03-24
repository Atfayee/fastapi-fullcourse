from fastapi import FastAPI
from pydantic import BaseModel

# uvicorn blog.main:app --reload
app = FastAPI()



class Blog(BaseModel):
    title:str
    body:str


@app.post('/blog')
def create(request: Blog):
    return request