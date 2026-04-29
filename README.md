# Boussole de Suivi-Évaluation (S&E) Automatisée

## Présentation du Projet
La **Boussole S&E** est une application Full-Stack Data conçue pour automatiser la collecte, l'analyse et la redevabilité des indicateurs de projets humanitaires. Développée sur MacBook Air dans le cadre du DU Big Data, elle permet de transformer des données brutes issues du web en rapports décisionnels (PDF) archivés.

L'architecture repose sur **6 piliers stratégiques** :
1. **Planification** : Définition des cibles en base de données.
2. **Crédibilité** : Collecte automatisée par Scraping sécurisé.
3. **Redevabilité** : Validation des données et stockage SQL.
4. **Impact/Efficience** : Calcul automatique des écarts.
5. **Capitalisation** : Génération de notes d'analyse stratégique.
6. **Dissémination** : Production et archivage de rapports PDF professionnels.

---

## Structure du Projet

```markdown
# 🧭 Boussole S&E Pro : Système Automatisé de Suivi-Évaluation

**Boussole S&E Pro** est une plateforme intelligente de monitoring humanitaire et de développement. Elle permet de collecter automatiquement des données via des sources externes (comme HDX), de valider la qualité des données, de générer des analyses d'impact financier et de produire des rapports PDF professionnels archivables.

---

## 🚀 Fonctionnalités Clés

* **Veille Stratégique Automatisée** : Collecte de données en temps réel via un scraper intégré pour garantir la crédibilité des sources.
* **Validation de Données** : Module de Data Quality (`validators.py`) pour filtrer les données aberrantes ou corrompues avant stockage.
* **Tableau de Bord Dynamique** : Interface Streamlit moderne avec indicateurs de performance (KPIs) et graphiques d'évolution.
* **Génération de Rapports PDF** : Création automatique de rapports détaillés incluant tableaux de bord et graphiques de performance via FPDF.
* **Gestion des Archives** : Système d'archivage chronologique avec menu de sélection épuré (selectbox) pour consulter l'historique sans encombrer l'interface.

---

## 📂 Structure du Projet

```text
SUIVI_EVALUATION_APP/
├── app/
│   ├── database/       # Gestion de la base de données SQL (Models, Session)
│   ├── pdf_reports/    # Moteur de génération des rapports PDF (generator.py)
│   ├── services/       # Logique métier et capitalisation (Analyse d'impact)
│   ├── utils/          # Outils : Scraper, Validateurs, Générateurs de graphiques
│   └── main.py         # Script principal de traitement (Backend)
├── outputs/            # Dossier de sortie des PDF et images temporaires
│   └── archives/       # Dossier de stockage des rapports historiques
├── dashboard.py        # Interface utilisateur Streamlit (Frontend)
├── requirements.txt    # Dépendances du projet
└── setup_mac.sh        # Script d'installation rapide
```

### Installation & Lancement

1. Installation automatique (Mac)
Ouvrez votre terminal dans le dossier du projet et lancez :

chmod +x setup_mac.sh
./setup_mac.sh

Ce script installe les dépendances système (Pango, Libffi), crée l'environnement virtuel (venv) et installe les bibliothèques Python.

2. Lancement du cycle de suivi

source venv/bin/activate
python3 -m app.main

Voici les 5 étapes clés à suivre avec ton application pour piloter un projet, de la source brute au rapport final :

1. Configuration de la Source (Input)

Tout commence dans la Sidebar (barre latérale) de ton Dashboard.Action : Tu identifies une source de données fiable (ex: une page de projet sur HDX ou le portail d'un bailleur).Opération : Tu colles l'URL dans le champ "🔗 URL DU PROJET À SUIVRE".Objectif : Dire à l'algorithme où chercher les informations sans modifier une seule ligne de code.

2. Collecte Automatisée 

Une fois que tu cliques sur "Lancer le Suivi" :Action : L'application déclenche Selenium et Undetected-Chromedriver.Opération : Le robot ouvre le navigateur en arrière-plan, contourne les protections, et extrait les données textuelles (nom du projet, budget, valeurs des indicateurs).Résultat : Les données "sales" du web sont transformées en données structurées.

3. Persistance et Stockage (Database)

Ton application ne se contente pas d'afficher, elle mémorise.Action : Utilisation de SQLAlchemy.Opération : Le script vérifie si le projet existe déjà. S'il est nouveau, il crée une entrée dans la table Projet. Il insère ensuite les chiffres dans la table Indicateur.Importance : Cela permet de garder un historique et de voir l'évolution des indicateurs au fil du temps (le "Suivi").

4. Analyse et Visualisation (Dashboard)

C'est la partie "Intelligence" de l'interface.Action : Streamlit interroge la base de données SQLite.Opération :Calcul du taux d'atteinte :$$(Réalisé / Cible) \times 100$$Génération des KPI Cards (les conteneurs blancs) pour une lecture immédiate.Affichage de la Performance dans le tableau central.

5. Reporting et Redevabilité (Output)

La dernière étape pour les décideurs.Action : Génération via Jinja2 et WeasyPrint.Opération : L'application prend les données fraîches, les injecte dans un template HTML élégant et génère un PDF officiel.Diffusion : Le rapport est archivé dans outputs/archives/ et devient disponible au téléchargement direct sur ton interface pour être envoyé aux partenaires.

Développé par Gérard KOUADIO - Projet S&E Big Data

---

### Pourquoi ce README est "Clair et Pro" ?

1.  **Hiérarchie** : On comprend tout de suite ce que fait l'outil, comment on l'installe et comment on le lance.
2.  **Transparence** : La partie sur la "Sentinelle" montre que tu maîtrises les risques liés au Big Data (données fausses).
3.  **Modularité** : La section sur l'adaptation prouve que ton code n'est pas "figé" mais évolutif.
4.  **Valorisation** : Tu cites tes piliers S&E, ce qui montre que ce n'est pas qu'un projet informatique, mais une solution métier.


**Félicitations !** Ton projet est maintenant complet, documenté et prêt pour une démonstration.