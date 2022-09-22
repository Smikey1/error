from typing import Optional,List
from pydantic import BaseModel
from .user import *
# Assuming this is the module where you declare your data model...


"""
? this is pydantic schema, but i make this with name --> pydantic model
"""

class BlogBaseModel(BaseModel):
    title:str
    body:str
    is_published:Optional[bool]

class BlogModel(BlogBaseModel):
    class Config():
        orm_mode=True


# defining it for response model --> but not working
class ShowResponseBlogModel(BaseModel):
    title:str
    body:str
    blog_creator:UserModelOut
    is_published:Optional[bool]
    class Config():
        orm_mode=True