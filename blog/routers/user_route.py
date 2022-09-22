from fastapi import APIRouter
from fastapi import Depends,status,HTTPException
from utils.messages import *
from utils.db_connection import get_db
from sqlalchemy.orm import Session
from models.blog import *
from models.user import *
from .. import db_schemas
from utils.password_hashing import PasswordHashing



router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

db_instance:Session=Depends(get_db)

@router.get("/",status_code=status.HTTP_200_OK,response_model=UserModelOut)
def all_user(db=db_instance):
    all_users=db.query(db_schemas.UserSchema).all()
    return success(all_users)

@router.post("/",response_model=UserModelOut)
async def create_user(request:UserModelIn,db:Session=db_instance):
    # new_user = db_schemas.UserSchema(name=request.name,email=request.email,phone=request.phone,password=PasswordHashing.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # added_user=db.query(db_schemas.UserSchema).filter(db_schemas.UserSchema.id==new_user.id).first()
    # return success(added_user,"User Created Successfully")
    return success(request,"User Created Successfully")


@router.get("/{id}")
def create_user(id:int,db:Session=db_instance):
    single_user = db.query(db_schemas.UserSchema).filter(db_schemas.UserSchema.id==id).first()
    if not single_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=failure("Blog not found"))
    return success(single_user,"Fetched User Successfully")