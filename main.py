from fastapi import FastAPI
from blog import db_schemas

from utils.db_connection import engine
from blog.routers import blog_route,user_route

#creating app for fastapi
app=FastAPI()

#creating new engine with sql schema/table 
db_schemas.Base.metadata.create_all(engine)

#include all router here
app.include_router(blog_route.router)
app.include_router(user_route.router)