# IFRI_MentorLink

Application web de mise en relation entre étudiants et mentors au sein de l'IFRI (Institut de Formation et de Recherche en Informatique), Université d'Abomey-Calavi.

Projet réalisé dans le cadre du rattrapage de PIL (Projet Intégré de Licence) — Licence 1.

## 🎯 Objectif

Permettre aux étudiants de trouver facilement un mentor selon leurs besoins (matière, disponibilités, filière) et de faciliter la prise de contact pour des séances de tutorat.

## 🛠️ Technologies utilisées

- **Backend** : Python (Flask)
- **Base de données** : PostgreSQL
- **Frontend** : HTML, CSS, JavaScript (vanilla)

## 📁 Structure du projet

```
IFRI_MentorLink/
├── app.py                  # Point d'entrée de l'application Flask
├── database/
│   └── schema.sql           # Script de création de la base de données
├── static/
│   ├── css/
│   │   └── style.css        # Feuille de style
│   ├── js/
│   │   └── script.js        # Scripts JavaScript
│   └── images/
│       └── logo.png
├── templates/
│   └── index.html            # Page(s) HTML (Jinja2)
└── README.md
```

## ⚙️ Installation

### Prérequis

- Python 3.12+
- PostgreSQL installé et configuré
- pip

### Étapes

1. **Cloner le dépôt**
```bash
git clone https://github.com/jeanyves17/RPIL_2526_HOUGBENOU_Jean-Yves.git
cd RPIL_2526_HOUGBENOU_Jean-Yves
```

2. **Installer les dépendances Python**
```bash
pip install -r requirements.txt
```

3. **Configurer la base de données**

Créer une base PostgreSQL, puis exécuter le script de schéma :
```bash
psql -U votre_utilisateur -d nom_de_la_base -f database/schema.sql
```

4. **Configurer la connexion à la base de données**

Adapter les identifiants de connexion (utilisateur, mot de passe, nom de la base) dans `app.py` ou dans un fichier de configuration/variables d'environnement.

5. **Lancer l'application**
```bash
python app.py
```

L'application est ensuite accessible sur `http://127.0.0.1:5000`.

## 🗄️ Base de données

La table principale `mentors` contient :
- `id` — identifiant unique
- `nom` — nom du mentor
- `matieres` — liste des matières enseignées
- `disponibilites` — créneaux horaires disponibles
- `filiere` — filière concernée (IA, IM, GL, etc.)
- `format_mentorat` — format proposé (présentiel, distanciel, les deux)

## ✨ Fonctionnalités

- Consultation de la liste des mentors disponibles
- Filtrage par matière, disponibilité et filière
- Interface simple et responsive


