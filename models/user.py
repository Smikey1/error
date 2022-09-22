from typing import Optional,List
from pydantic import BaseModel
from .blog import *
# Assuming this is the module where you declare your data model...


"""
? this is pydantic schema, but i make this with name --> pydantic model
"""

class UserBaseModel(BaseModel):
    name:str
    email:str
    phone:int
    

class UserModelOut(UserBaseModel):
    pass
    class Config():
        orm_mode = True

# defining it for response model --> but not working
class UserModelIn(UserBaseModel):
    password:str
    # user_blog:List[BlogModel]=[]