from GestionStock import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Produit(Base):
    __tablename__ = 'produits'
    id = Column(Integer, primary_key = True)
    nom = Column (String(50), nullable = False, unique = True)
    prix_unitaire = Column(String(50), nullable = False)
    quantite_en_stock = Column(Integer, default=0)
    create_date = Column(DateTime, default = datetime.utcnow)

class Fournisseur(Base):
    __tablename__ = 'fournisseur'
    id = Column(Integer, primary_key = True)
    nom = Column (String(50), nullable = False, unique = True)
    adress = Column(String(50), nullable = False)
    contact = Column(String(50), nullable = False)
    create_date = Column(DateTime, default = datetime.utcnow)

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key = True)
    nom = Column (String(50), nullable = False, unique = True)
    adress = Column(String(50), nullable = False)
    contact = Column(String(50), nullable = False)
    create_date = Column(DateTime, default = datetime.utcnow)