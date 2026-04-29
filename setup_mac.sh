#!/bin/bash

echo "🚀 Démarrage de l'installation de la Boussole S&E..."

# 1. Vérification de Homebrew
if ! command -v brew &> /dev/null
then
    echo "❌ Homebrew n'est pas installé. Veuillez l'installer sur https://brew.sh/"
    exit
fi

# 2. Installation des dépendances système pour le PDF et Python
echo "📦 Installation des dépendances système (Brew)..."
brew install pango libffi python@3.10

# 3. Création de l'environnement virtuel
echo "🐍 Configuration de l'environnement virtuel Python..."
python3 -m venv venv
source venv/bin/activate

# 4. Installation des bibliothèques Python
echo "📥 Installation des packages Python (Requirements)..."
pip install --upgrade pip
pip install -r requirements.txt

# 5. Création des dossiers manquants
echo "📂 Création de l'arborescence de sortie..."
mkdir -p outputs/archives
mkdir -p app/static/temp

echo "✅ Installation terminée !"
echo "👉 Pour lancer l'app : source venv/bin/activate && python3 -m app.main"
