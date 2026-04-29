from app.database.models import Indicateur

def analyser_evolution_impact(db_session, projet_id):
    print("🧠 Analyse de capitalisation en cours...")
    
    # On récupère les indicateurs du projet
    indicateurs = db_session.query(Indicateur).filter_by(projet_id=projet_id).all()
    
    notes = []
    for ind in indicateurs:
        taux = (ind.realise / ind.cible) * 100
        if taux >= 100:
            notes.append(f"Objectif atteint pour {ind.nom}. Envisager un passage à l'échelle.")
        elif taux >= 75:
            notes.append(f"Bonne progression sur {ind.nom}. Maintenir l'effort actuel.")
        else:
            notes.append(f"Alerte sur {ind.nom} : Progression inférieure à 75%. Réévaluer la stratégie.")
            
    return " | ".join(notes)