from sqlalchemy import create_engine
# sqlalchemy.extension.declaraticve
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#creation of database engine
SQLALCHAMY_DATABASE_URL = "sqlite:///./fastapi.db"
engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})

#creation of sql orm session
SessionLocalMaker = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# And finally, creation and decleration of base
Base = declarative_base()

def get_db():
    db=SessionLocalMaker()
    try:
        yield db
    finally:
        db.close()