from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# URL de la base de données (crée le fichier localement)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./suivi_impact.db")

# Création du moteur
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Nécessaire pour SQLite
)

# Configuration de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)