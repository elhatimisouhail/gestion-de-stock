from pydantic import BaseModel


class SchemaProduit(BaseModel):
    nom: str
    prix_unitaire: float

class SchemaFournisseur(BaseModel):
    nom: str
    adress: str
    contact: str

class SchemaClient(BaseModel):
    nom: str
    adress: str
    contact: str