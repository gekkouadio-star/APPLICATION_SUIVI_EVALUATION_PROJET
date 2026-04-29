import streamlit as st
import pandas as pd
import os
from PIL import Image
import subprocess
from datetime import datetime
from app.database.db import SessionLocal
from app.database.models import Projet, Indicateur

# --- CONFIGURATION DE LA PAGE ---
icon_path = os.path.join("outputs", "Projet.png")
icon_image = Image.open(icon_path)

# Configuration de la page avec l'image personnalisée
st.set_page_config(
    page_title="PROJET S&E Pro", 
    page_icon=icon_image, 
    layout="wide"
)

# --- STYLE CSS PERSONNALISÉ (STYLE DÉVELOPPEUR AVANCÉ) ---
st.markdown("""
<style>
    /* IMPORT D'UNE POLICE MODERNE */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* 1. FOND DE NAVIGATION SIDEBAR DARK MODE */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e1117 0%, #162a4a 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Majuscules et espacement pour le menu */
    [data-testid="stSidebarNav"] ul li div a span {
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        color: #ffffff !important;
        font-size: 0.85rem;
    }

    /* Style de la bande passante animée */
    .info-banner {
        background-color: #102a43;
        color: #f0f4f8;
        padding: 14px;
        font-size: 0.85rem;
        font-weight: 600;
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        box-sizing: border-box;
        border-radius: 12px;
        margin-bottom: 25px;
        border: 1px solid #243b53;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .info-banner span {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 30s linear infinite;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }

    /* Style des cartes KPI (Statistiques) */
    .stats-container {
        background-color: #ffffff;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        border: 1px solid #d9e2ec;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    .stats-container:hover { 
        transform: translateY(-8px); 
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
        border-color: #627d98;
    }

    .stats-container h2 {
        font-weight: 800;
        letter-spacing: -1px;
        margin: 10px 0;
    }

    .stats-container p {
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* MODIFICATION ICI : FOND GRIS TRÈS CLAIR PROFESSIONNEL */
    .stApp { background-color: #f8fafc; }
    
    /* Titres principaux */
    h1 {
        color: #102a43;
        font-weight: 800 !important;
        letter-spacing: -1.5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.05);
    }

    h3 {
        color: #334e68;
        font-weight: 700 !important;
        border-left: 5px solid #1c335e;
        padding-left: 15px;
        margin-top: 30px !important;
    }

    /* Boutons personnalisés */
    .stButton>button {
        background: linear-gradient(90deg, #1c335e 0%, #334e68 100%);
        color: white;
        border-radius: 12px;
        padding: 0.7rem 1.5rem;
        width: 100%;
        border: none;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(28, 51, 94, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- 1. BANDE PASSANTE D'INFORMATION (DYNAMIQUE) ---
date_actuelle = datetime.now().strftime("%d %B %Y")
st.markdown(f'''
    <div class="info-banner">
        <span>BOUSSOLE S&E | STATUT : OPÉRATIONNEL | DERNIÈRE COLLECTE : {date_actuelle} | 
        MODULE DE VALIDATION : ACTIF | ALGORITHME : D'ÉVALUATION DES INDICATEURS SELON L'AVANCEMENT DU PROJET | 
        SYSTÈME AUTOMATISÉ</span>
    </div>
''', unsafe_allow_html=True)

# --- 2. LOGIQUE DE DONNÉES ---
db = SessionLocal()
projets = db.query(Projet).all()

# --- 3. BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    # MODIFICATION ICI : REMPLACEMENT DE L'URL PAR TON IMAGE LOCALE Projet.png
    st.image(icon_image, width=120) 
    
    st.markdown("### CONFIGURATION")
    
    # --- AJOUTS CHAMPS DYNAMIQUES POUR LANCEMENT AUTOMATIQUE ---
    nom_projet = st.text_input("NOM DU PROJET", value="Rapport Impact 2026")
    budget_projet = st.number_input("BUDGET ALLOUÉ (€)", min_value=0.0, value=85000.0)
    cible_projet = st.number_input("CIBLE À ATTEINDRE", min_value=1.0, value=2500.0)
    input_url = st.text_input("🔗 URL DU PROJET À SUIVRE", placeholder="Coller le lien HDX ici...")
    
    if st.button("LANCER LE SUIVI"):
        if input_url:
            with st.spinner("TRAITEMENT EN COURS..."):
                # LANCEMENT AUTOMATIQUE AVEC ARGUMENTS : Nom, Budget, Cible
                subprocess.run([
                    "python3", "-m", "app.main", 
                    nom_projet, 
                    str(budget_projet), 
                    str(cible_projet)
                ])
                st.rerun()
        else:
            st.error("Veuillez saisir une URL.")

# --- 4. CORPS PRINCIPAL ---
st.title("TABLEAU DE L'APPLICATION SUIVI-ÉVALUATION")

if projets:
    p = projets[-1]
    indic = db.query(Indicateur).filter_by(projet_id=p.id).first()
    
    # Affichage des KPIs dans le style "Stats-Container"
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""<div class="stats-container">
            <p style='color:#627d98; font-size:0.85rem;'>RÉALISÉ ACTUEL</p>
            <h2 style='color:#102a43;'>{indic.realise if indic else 0}</h2>
            <p style='font-size:0.75rem; color:#829ab1;'>UNITÉ : {indic.unite if indic else '-'}</p>
        </div>""", unsafe_allow_html=True)

    with col2:
        taux = round((indic.realise / indic.cible * 100), 1) if (indic and indic.cible > 0) else 0
        st.markdown(f"""<div class="stats-container">
            <p style='color:#627d98; font-size:0.85rem;'>TAUX D'ATTEINTE GLOBAL</p>
            <h2 style='color:#218838;'>{taux}%</h2>
            <p style='font-size:0.75rem; color:#829ab1;'>OBJECTIF CIBLE : {indic.cible if indic else 0}</p>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""<div class="stats-container">
            <p style='color:#627d98; font-size:0.85rem;'>ENVELOPPE BUDGÉTAIRE</p>
            <h2 style='color:#102a43;'>{p.budget_alloue:,.0f} €</h2>
            <p style='font-size:0.75rem; color:#829ab1;'>PROJET : {p.nom[:25]}...</p>
        </div>""", unsafe_allow_html=True)

    st.write("###")

    # --- AJOUT DU GRAPHIQUE D'ÉVOLUTION ---
    st.subheader("ANALYSE DE LA RÉALISATION ET INVESTISSEMENTS")
    
    data_evolution = pd.DataFrame({
        'Année': ['2022', '2023', '2024', '2025', '2026'],
        'Investissement (€)': [p.budget_alloue * 0.2, p.budget_alloue * 0.4, p.budget_alloue * 0.6, p.budget_alloue * 0.8, p.budget_alloue],
        'Taux Réalisation (%)': [15, 35, 55, 80, taux]
    })
    
    st.bar_chart(data=data_evolution, x='Année', y='Investissement (€)', color="#1c335e")
    st.line_chart(data=data_evolution, x='Année', y='Taux Réalisation (%)', color="#28a745")

    st.write("###")
    
    # Zone de détails
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("### DÉTAILS STRATÉGIQUES DU PROJET")
        st.info(f"**CONTEXTE ET DESCRIPTION :** {p.description}")
        
        all_indic = db.query(Indicateur).filter_by(projet_id=p.id).all()
        df = pd.DataFrame([{
            "NOM DE L'INDICATEUR": i.nom,
            "CIBLE PRÉVUE": i.cible,
            "VALEUR RÉELLE": i.realise,
            "PERFORMANCE (%)": f"{(i.realise/i.cible*100):.1f}%"
        } for i in all_indic])
        st.table(df)

    with c2:
        st.markdown("### ARCHIVES DE REDEVABILITÉ")
        
        path_archives = "outputs/archives"
        path_outputs = "outputs"
        
        # 1. RECHERCHE DES FICHIERS PDF
        tous_les_pdfs = []
        for dossier in [path_outputs, path_archives]:
            if os.path.exists(dossier):
                for f in os.listdir(dossier):
                    if f.endswith(".pdf"):
                        tous_les_pdfs.append(os.path.join(dossier, f))

        # 2. AFFICHAGE ÉPURÉ (Menu Déroulant)
        if tous_les_pdfs:
            # Trier pour avoir le plus récent en premier
            tous_les_pdfs.sort(key=os.path.getmtime, reverse=True)
            
            # Créer un dictionnaire pour afficher uniquement le nom du fichier dans la liste
            options_fichiers = {os.path.basename(p): p for p in tous_les_pdfs}
            
            # Menu déroulant pour choisir le rapport
            fichier_choisi_nom = st.selectbox(
                "CHOISIR UN RAPPORT À CONSULTER :", 
                options=options_fichiers.keys(),
                index=0
            )
            
            # Récupérer le chemin complet du fichier sélectionné
            chemin_complet = options_fichiers[fichier_choisi_nom]
            
            st.write("---")
            
            # Bouton unique de téléchargement pour le fichier sélectionné
            with open(chemin_complet, "rb") as f:
                st.download_button(
                    label=f"📥 TÉLÉCHARGER LE RAPPORT",
                    data=f,
                    file_name=fichier_choisi_nom,
                    mime="application/pdf",
                    key=f"dl_{fichier_choisi_nom}"
                )
        else:
            st.warning("Aucun rapport disponible.")
            st.info("Vérifiez que 'main.py' a bien fini de générer le fichier dans le dossier 'outputs'.")
else:
    st.warning("AUCUNE DONNÉE DISPONIBLE. VEUILLEZ CONFIGURER UNE SOURCE DANS LA SIDEBAR.")

db.close()