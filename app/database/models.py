from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Projet(Base):
    __tablename__ = 'projets'
    
    id = Column(Integer, primary_key=True)
    nom = Column(String(255), nullable=False)
    description = Column(Text)
    budget_alloue = Column(Float) # Planification financière globale
    date_debut = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relations (Redevabilité & Dissémination)
    indicateurs = relationship("Indicateur", back_populates="projet")
    finances = relationship("Finance", back_populates="projet")
    capitalisations = relationship("Capitalisation", back_populates="projet")

class Indicateur(Base):
    __tablename__ = 'indicateurs'
    
    id = Column(Integer, primary_key=True)
    nom = Column(String(255))
    cible = Column(Float)      # Objectif (Planification)
    realise = Column(Float)    # Valeur consolidée via Veille Stratégique
    unite = Column(String(50)) # ex: "Datasets", "Bénéficiaires"
    projet_id = Column(Integer, ForeignKey('projets.id'))
    
    projet = relationship("Projet", back_populates="indicateurs")

class Finance(Base):
    __tablename__ = 'finances'
    
    id = Column(Integer, primary_key=True)
    montant_depense = Column(Float)
    annee = Column(Integer)         # Ajout pour le graphique d'évolution (ex: 2024)
    categorie = Column(String(100)) # ex: "Infrastructure", "Formation"
    date_transaction = Column(DateTime, default=datetime.datetime.utcnow)
    projet_id = Column(Integer, ForeignKey('projets.id'))
    
    projet = relationship("Projet", back_populates="finances")

class Capitalisation(Base):
    __tablename__ = 'capitalisation'
    
    id = Column(Integer, primary_key=True)
    lecon_apprise = Column(Text) # Pour le renforcement de l'impact
    succes = Column(Text)
    defis = Column(Text)
    projet_id = Column(Integer, ForeignKey('projets.id'))
    
    projet = relationship("Projet", back_populates="capitalisations")