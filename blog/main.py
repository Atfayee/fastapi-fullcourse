from fastapi import FastAPI
from . import schemas

# uvicorn blog.main:app --reload
app = FastAPI()


@app.post('/blog')
def create(request: schemas.Blog):
    return request