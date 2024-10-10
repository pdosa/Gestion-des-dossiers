from datetime import datetime

from pydantic import BaseModel


class DossierSchema(BaseModel):
    id_dossier:str
    type:str
    etat:str
    date_creation:datetime
    date_modification:datetime
    id_client:str
    
