from sqlalchemy import create_engine
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
app = FastAPI()
engine = create_engine('sqlite:///db') #Creation du moteur
SessionLocale = sessionmaker(engine) #Creation de gestionaire de session
Base = declarative_base() #Creation de BD
# Fonction qui sert pour generer une session locale
def creerSession():
    db_session = SessionLocale()
    try:
        yield db_session
    finally:
        db_session.close() #Fermeture de session
from GestionStock.models import Produit
Base.metadata.create_all(bind= engine)
from GestionStock import urls