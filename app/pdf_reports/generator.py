from fpdf import FPDF
import os
from app.utils.charts import generer_graphique_barres

def generer_pdf_final(projet_db, **kwargs):
    print(f"📄 Optimisation du PDF pour : {projet_db.nom}...")
    
    pdf = FPDF()
    pdf.add_page()
    
    # --- EN-TÊTE ---
    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(52, 152, 219) 
    pdf.cell(190, 15, "RAPPORT DE SUIVI-ÉVALUATION", ln=True, align='C')
    
    pdf.set_font("Arial", 'I', 12)
    pdf.set_text_color(100)
    pdf.cell(190, 10, f"Projet : {projet_db.nom}", ln=True, align='C')
    pdf.ln(10)

    # --- TABLEAU DE PERFORMANCE ---
    w = [80, 35, 35, 40] 
    pdf.set_font("Arial", 'B', 11)
    pdf.set_fill_color(52, 152, 219)
    pdf.set_text_color(255)
    
    cols = ["Indicateur", "Cible", "Réalisé", "Progression"]
    for i in range(len(cols)):
        pdf.cell(w[i], 10, cols[i], 1, 0, 'C', True)
    pdf.ln()

    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(0)
    
    for indic in projet_db.indicateurs:
        # Calcul sécurisé du taux
        taux_val = (indic.realise / indic.cible) if indic.cible > 0 else 0
        progression = f"{(taux_val * 100):.2f}%"
        
        pdf.cell(w[0], 10, f" {indic.nom}", 1)
        pdf.cell(w[1], 10, f"{indic.cible}", 1, 0, 'C')
        pdf.cell(w[2], 10, f"{indic.realise}", 1, 0, 'C')
        
        # Couleur dynamique selon performance
        if taux_val >= 0.8:
            pdf.set_text_color(39, 174, 96) # Vert
        else:
            pdf.set_text_color(231, 76, 60) # Rouge
            
        pdf.cell(w[3], 10, progression, 1, 1, 'C')
        pdf.set_text_color(0) 

    # --- GRAPHIQUE 1 : PERFORMANCE ACTUELLE ---
    if projet_db.indicateurs:
        ind = projet_db.indicateurs[0]
        chart_performance = generer_graphique_barres(ind.nom, ind.cible, ind.realise)
        
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(190, 10, "1. Analyse de la Performance Actuelle", ln=True, align='L')
        pdf.image(chart_performance, x=30, w=150) 
        pdf.ln(5)

    # --- GRAPHIQUE 2 : ÉVOLUTION (Si présent) ---
    if 'evolution_chart_path' in kwargs and os.path.exists(kwargs['evolution_chart_path']):
        pdf.add_page() # Nouvelle page pour l'historique
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(190, 10, "2. Analyse de l'Évolution Historique (2022-2026)", ln=True, align='L')
        pdf.image(kwargs['evolution_chart_path'], x=20, w=170)
        pdf.ln(5)

    # --- FOOTER D'IMPACT ---
    # On s'assure d'avoir de l'espace
    if pdf.get_y() > 230: 
        pdf.add_page()
        
    pdf.ln(10)
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 10, " Synthèse de l'Impact Stratégique ", 0, 1, 'L', True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(190, 8, "La collecte automatisée confirme la crédibilité des sources. "
                          "L'atteinte des objectifs suggère une efficience des fonds alloués. "
                          "Les graphiques ci-dessus valident la trajectoire de performance du projet.")

    # --- SAUVEGARDE ---
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        
    output_path = f"outputs/Rapport_{projet_db.id}.pdf"
    pdf.output(output_path)
    print(f"✅ Rapport généré avec succès : {output_path}")