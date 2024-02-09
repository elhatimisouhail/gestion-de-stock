from fastapi import FastAPI, Depends
app = FastAPI()
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session
from datetime import datetime
from pydantic import BaseModel

engine = create_engine('sqlite:///db')  #Creation de moteur de liaison
SessionLocal = sessionmaker(engine)   #Creation de gestionnaire de session
Base = declarative_base()   #Creation de BD


# Fonction qui sert pour generer une session locale
def creerSession():
    db_session = SessionLocal()
    try:
        yield db_session  # yield un generateur
    finally:
        db_session.close()   #fermeture de session

class User (Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    create_date = Column(DateTime, default=datetime.utcnow)

class SchemaUser(BaseModel):
    email:str
    password:str

class SchemaUser_get(BaseModel):
    create_date : datetime


Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return {'message':'Hello'}
@app.post('/user')
def add_user(schemauser:SchemaUser, db_session:session = Depends(creerSession)):
    user = User(email = schemauser.email, password = schemauser.password)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return {'user':user}


import uvicorn
uvicorn.run(app)

