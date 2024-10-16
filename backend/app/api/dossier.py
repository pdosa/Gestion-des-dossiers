from fastapi import APIRouter,Depends
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.dossier_model import Dossier
from app.models.user_model import User
from app.schemas.responseModel.dossier_response import DossierCreate, DossierResponse
from app.core.token_validation import get_current_active

from db.db_connection import bd_connection_v1

Dossier=APIRouter(prefix="/Dossier",tags=["Dossier"])

# Créer un dossier
@Dossier.post("/dossiers/", response_model=DossierResponse)
def create_dossier(dossier: DossierCreate, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    new_dossier = Dossier(
        titre=dossier.titre, description=dossier.description,
        user_id=current_user.id
    )
    db.add(new_dossier)
    db.commit()
    db.refresh(new_dossier)
    return new_dossier

# Obtenir tous les dossiers de l'utilisateur connecté
@Dossier.get("/dossiers/", response_model=list[DossierResponse])
def get_dossiers(db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    dossiers = db.query(Dossier).filter(Dossier.user_id == current_user.id).all()
    return dossiers

# Obtenir un dossier spécifique
@Dossier.get("/dossiers/{dossier_id}", response_model=DossierResponse)
def get_dossier(dossier_id: int, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    dossier = db.query(Dossier).filter(Dossier.id == dossier_id, Dossier.user_id == current_user.id).first()
    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    return dossier

# Mettre à jour un dossier
@Dossier.put("/dossiers/{dossier_id}", response_model=DossierResponse)
def update_dossier(dossier_id: int, dossier: DossierCreate, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    db_dossier = db.query(Dossier).filter(Dossier.id == dossier_id, Dossier.user_id == current_user.id).first()
    if not db_dossier:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    db_dossier.titre = dossier.titre
    db_dossier.description = dossier.description
    db.commit()
    db.refresh(db_dossier)
    return db_dossier

# Supprimer un dossier
@Dossier.delete("/dossiers/{dossier_id}")
def delete_dossier(dossier_id: int, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    dossier = db.query(Dossier).filter(Dossier.id == dossier_id, Dossier.user_id == current_user.id).first()
    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")
    db.delete(dossier)
    db.commit()
    return {"message": "Dossier supprimé avec succès"}

# Archiver un dossier
@Dossier.put("/dossiers/{dossier_id}/archiver")
def archiver_dossier(dossier_id: int, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    dossier = db.query(Dossier).filter(Dossier.id == dossier_id, Dossier.user_id == current_user.id).first()
    if not dossier:
        raise HTTPException(status_code=404, detail="Dossier non trouvé")

    if dossier.statut != "Finalisé":
        raise HTTPException(status_code=400, detail="Le dossier doit être finalisé avant archivage")

    dossier.statut = "Archivé"
    db.commit()
    return {"message": "Dossier archivé avec succès", "dossier": dossier}