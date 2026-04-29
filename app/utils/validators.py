def valider_donnee_humanitaire(valeur):
    """
    Vérifie si la donnée extraite est réaliste pour le S&E.
    """
    print(f"🔍 Validation de la donnée : {valeur}")
    
    # 1. Vérification du type
    if not isinstance(valeur, (int, float)):
        print("⚠️ Erreur : La donnée n'est pas un nombre.")
        return False, 0.0
    
    # 2. Vérification de cohérence (ex: pas de valeurs négatives pour des datasets)
    if valeur < 0:
        print("⚠️ Erreur : Valeur négative détectée.")
        return False, 0.0
    
    # 3. Plafond de sécurité (ex: pas plus de 100 000 datasets sur HDX pour éviter les bugs)
    if valeur > 100000:
        print("⚠️ Erreur : Valeur hors norme, possible erreur de scraping.")
        return False, 0.0
        
    return True, float(valeur)