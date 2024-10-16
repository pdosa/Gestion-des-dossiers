from datetime import datetime

from pydantic import BaseModel


class DossierSchema(BaseModel):
    id_dossier:str
    document_id:str
    file_path:str
    file_name:str
    date_update:datetime
    
    
