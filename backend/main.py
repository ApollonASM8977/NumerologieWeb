# © 2026 Aboubacar Sidick Meite (ApollonIUGB77) — All Rights Reserved
"""NumerologieWeb API — FastAPI backend."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import datetime

from numerology import analyser, chemin_de_vie, compatibilite

# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="NumerologieWeb API",
    description="Analyse numérologique complète — calcul et interprétation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://127.0.0.1:5173", "http://127.0.0.1:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Models ────────────────────────────────────────────────────────────────────

class PersonRequest(BaseModel):
    prenom: str = Field(..., min_length=1)
    nom: str = Field(..., min_length=1)
    jour: int = Field(..., ge=1, le=31)
    mois: int = Field(..., ge=1, le=12)
    annee: int = Field(..., ge=1900, le=datetime.date.today().year)


class CompatibiliteRequest(BaseModel):
    personne1: PersonRequest
    personne2: PersonRequest


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"name": "NumerologieWeb API", "version": "1.0.0", "status": "running"}


@app.post("/analyze")
def analyze(req: PersonRequest):
    try:
        result = analyser(req.prenom, req.nom, req.jour, req.mois, req.annee)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/compatibility")
def compatibility(req: CompatibiliteRequest):
    try:
        p1 = req.personne1
        p2 = req.personne2
        profil1 = analyser(p1.prenom, p1.nom, p1.jour, p1.mois, p1.annee)
        profil2 = analyser(p2.prenom, p2.nom, p2.jour, p2.mois, p2.annee)
        compat = compatibilite(profil1["chemin_de_vie"]["valeur"], profil2["chemin_de_vie"]["valeur"])
        return {
            "personne1": profil1,
            "personne2": profil2,
            "compatibilite": compat,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
