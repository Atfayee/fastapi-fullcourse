from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import schemas, models
from blog.database import get_db
from .. import token
from ..hashing import Hash


router = APIRouter(
    tags=['Authentication'],
)

@router.post('/login')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail=f"Incorrect password")
    
    access_token = token.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"} 