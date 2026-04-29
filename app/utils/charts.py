import matplotlib.pyplot as plt
import os

def generer_graphique_barres(nom_projet, cible, realise):
    # Setup du style
    plt.figure(figsize=(6, 4))
    categories = ['Cible', 'Réalisé']
    valeurs = [cible, realise]
    couleurs = ['#bdc3c7', '#3498db'] # Gris pour cible, Bleu pour réalisé

    plt.bar(categories, valeurs, color=couleurs)
    plt.title(f"Progression : {nom_projet}")
    plt.ylabel("Valeurs")

    # Création du dossier temporaire
    if not os.path.exists('app/static/temp'):
        os.makedirs('app/static/temp')

    path_chart = 'app/static/temp/last_chart.png'
    plt.savefig(path_chart)
    plt.close()
    return path_chart