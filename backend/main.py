
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Découpeur de scènes YouTube",
    description="Backend pour analyser et découper les vidéos",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur le backend du Découpeur de scènes YouTube !",
        "status": "operationnel"
    }

@app.get("/health")
def verifier_etat():
    return {"status": "ok"}
