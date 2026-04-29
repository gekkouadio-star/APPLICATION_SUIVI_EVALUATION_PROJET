def analyser_efficience_financement(budget_prevu, depense_reelle, resultats_atteints):
    """
    Calcule si le financement a eu l'impact escompté.
    """
    # 1. Calcul du taux de consommation (Redevabilité)
    taux_consommation = (depense_reelle / budget_prevu) * 100
    
    # 2. Calcul du coût unitaire de l'impact
    # ex: Coût par bénéficiaire
    if resultats_atteints > 0:
        cout_unitaire = depense_reelle / resultats_atteints
    else:
        cout_unitaire = 0

    # 3. Recommandation pour le renforcement
    recommandation = ""
    if taux_consommation > 100:
        recommandation = "Alerte : Surconsommation. Réviser la planification."
    elif cout_unitaire < (budget_prevu / resultats_atteints * 0.8):
        recommandation = "Excellente efficience : Capitaliser sur cette méthode."
        
    return {
        "taux_consommation": round(taux_consommation, 2),
        "cout_unitaire": round(cout_unitaire, 2),
        "recommandation": recommandation
    }