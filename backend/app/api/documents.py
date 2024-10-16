from fastapi import APIRouter


documents=APIRouter(prefix="/Documents",tags=["Documents"])

from fastapi import APIRouter,Depends
from fastapi import File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.models.file_model import Document
from app.models.dossier_model import Dossier
from app.models.user_model import User
from app.schemas.responseModel.file_response import FileCreate, FileResponse
from app.core.token_validation import get_current_active
import shutil
import os

from db.db_connection import bd_connection_v1




# Configuration du dossier de stockage
UPLOAD_DIRECTORY = "/path/to/upload/directory/"

# Téléverser un document
@documents.post("/dossiers/{dossier_id}/documents/")
def upload_document(dossier_id: int, file: UploadFile = File(...), db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    dossier = db.query(Dossier).filter(Dossier.id == dossier_id, Dossier.user_id == current_user.id).first()
    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")

    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    # Sauvegarde du fichier
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Enregistrement du document dans la base de données
    new_document = Document(
        file_name=file.filename, file_path=file_path, dossier_id=dossier.id
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return {"message": "Document téléversé avec succès", "document": new_document}

# Obtenir la liste des documents d'un dossier
@documents.get("/dossiers/{dossier_id}/documents/")
def get_documents(dossier_id: int, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    documents = db.query(Document).filter(Document.dossier_id == dossier_id).all()
    return documents

# Supprimer un document
@documents.delete("/documents/{document_id}")
def delete_document(document_id: int, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document non trouvé")

    os.remove(document.file_path)
    db.delete(document)
    db.commit()
    return {"message": "Document supprimé avec succès"}
