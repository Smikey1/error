from utils.db_connection import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship

# For SQL Class and ORM
"""
? this is sql model, but i make this with name --> sql schema
"""

class BlogSchema(Base):
    __tablename__="blog_table"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    is_published=Column(Boolean)
    user_id=Column(Integer,ForeignKey("user_table.id"))
    blog_creator= relationship("UserSchema",back_populates="user_blog")

class UserSchema(Base):
    __tablename__="user_table"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    phone=Column(Integer)
    password=Column(String)
    user_blog= relationship("BlogSchema",back_populates="blog_creator")
