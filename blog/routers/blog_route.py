from fastapi import APIRouter
from fastapi import Depends,status,Response,HTTPException
from utils.messages import *
from utils.db_connection import get_db
from sqlalchemy.orm import Session
from models.blog import *
from .. import db_schemas


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

db_instance:Session=Depends(get_db)

# @router.get("/",status_code=status.HTTP_200_OK,response_model=List[ShowResponseBlogModel])
@router.get("/",status_code=status.HTTP_200_OK)
def all_blogs(db=db_instance):
    all_blogs=db.query(db_schemas.BlogSchema).all()
    return success(all_blogs)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_blog(request:BlogModel,db:Session=db_instance):
    new_blog=db_schemas.BlogSchema(title=request.title,body=request.body,is_published=request.is_published,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return success(new_blog)

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=ShowResponseBlogModel)
# @router.get("/{id}",status_code=status.HTTP_200_OK)
def get_blog_by_Id(id:int,db:Session=db_instance):
    single_blog=db.query(db_schemas.BlogSchema).filter(db_schemas.BlogSchema.id==id).first()
    if not single_blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=failure("Blog not found"))
    return success(single_blog,"Fetched Blog Successfully")

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_Id(id:int,request:BlogModel, db:Session=db_instance):
    blog= db.query(db_schemas.BlogSchema).filter(db_schemas.BlogSchema.id==request.title)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,failure("Blog Not Found"))
    blog_data = request.dict(exclude_unset=True)
    for key,value in blog_data.items():
        setattr(blog,key,value)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return success("Blog Updated")

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_Id(id:int,response:Response,db:Session=db_instance,):
    blog=db.query(db_schemas.BlogSchema).filter(db_schemas.BlogSchema.id==id)
    print(f"The blog is:-->{blog}")
    print(f"The blog.first is:-->{blog.first()}")
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND,failure("Blog Not Found"))
    blog.delete(synchronize_session=False)
    db.commit()
    return success("Blog Deleted")
