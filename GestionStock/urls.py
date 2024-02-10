from GestionStock import app, creerSession
from GestionStock.schema import SchemaProduit
from GestionStock.schema import SchemaFournisseur
from GestionStock.schema import SchemaClient
from sqlalchemy.orm import  Session #Importation de gestionaire de session et de donnee de type session
from GestionStock.models import Produit
from fastapi import Depends


@app.get('/')
def home():
    return {'message':'Hello'}

@app.post('/produit')
def add_produit(schemaproduit : SchemaProduit, db_session:Session = Depends(creerSession)):
    produit = Produit(nom = schemaproduit.nom, prix_unitaire = schemaproduit.prix_unitaire)
    db_session.add(produit)
    db_session.commit()
    db_session.refresh(produit)
    return {'produit':produit}

@app.post('/fournisseur')
def add_fournisseur(schemafournisseur : SchemaFournisseur, db_session:Session = Depends(creerSession)):
    fournisseur = Fournisseur(nom = schemafournisseur.nom, adress = schemafournisseur.adress, contact = schemafournisseur.contact)
    db_session.add(fournisseur)
    db_session.commit()
    db_session.refresh(fournisseur)
    return {'fournisseur':fournisseur}

@app.post('/client')
def add_client(schemaclient : SchemaClient, db_session:Session = Depends(creerSession)):
    client = Client(nom = schemaclient.nom, adress = schemaclient.adress, contact = schemaclient.contact)
    db_session.add(client)
    db_session.commit()
    db_session.refresh(client)
    return {'client':client}