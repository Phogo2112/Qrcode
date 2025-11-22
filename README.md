# Générateur de QR Code - Qrcode.py

Ce projet permet de générer un **QR Code** à partir d’une URL et de créer automatiquement :  
- une **image PNG** du QR Code  
- un **fichier PDF** format A4 contenant le QR Code  

Il est développé en **Python** et utilise les bibliothèques `qrcode` et `reportlab`.

---

## 🔹 Prérequis

- Python 3.x installé
- Un environnement virtuel (recommandé)

---

## 🔹 Installation

1. **Cloner le projet** :

```bash
git clone https://github.com/Phogo2
cd Qrcode
```
2. ##Créer un environnement virtuel (optionnel mais recommandé) :##

python -m venv env


3. ##Activer l’environnement virtuel :##

Windows PowerShell :

.\env\Scripts\Activate.ps1


4. ##Windows CMD :##

.\env\Scripts\activate.bat


5. ##Linux / Mac :##

source env/bin/activate


6. ##Installer les dépendances :##

pip install -r requirements.txt


7. ##Créer un fichier .env si nécessaire pour stocker des variables d’environnement (si ton projet en nécessite).##

Dans ce projet de base, il n’y a pas de variables sensibles, donc .env est optionnel.

🔹 Utilisation

##Pour générer un QR Code :##

python Qrcode.py

Cela crée automatiquement :

qrcode.png → l’image du QR Code

qrcode.pdf → le PDF A4 contenant le QR Code
