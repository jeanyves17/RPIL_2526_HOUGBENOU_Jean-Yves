# IFRI_MentorLink — Rattrapage

Version simplifiée : une seule page, recherche de mentor compatible (matière + créneau ± 1h), sans authentification.

## Étapes pour lancer le projet

### 1. Créer la base de données
```bash
createdb ifri_mentorlink
psql -d ifri_mentorlink -f database/schema.sql
```
(Adapte `DB_CONFIG` dans `app.py` si ton user/mot de passe PostgreSQL diffère.)

### 2. Installer les dépendances Python
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Lancer le serveur
```bash
python app.py
```
Puis ouvre : http://127.0.0.1:5000

## Comment les fichiers s'articulent

| Fichier | Rôle |
|---|---|
| `database/schema.sql` | Crée la table `mentors` (colonnes en tableaux PostgreSQL) + 3 mentors de test |
| `app.py` | Backend Flask : route `/` sert la page, route `/api/match` fait le matching en Python et interroge PostgreSQL |
| `templates/index.html` | La page unique avec le formulaire (matières, jour, heure, filière optionnelle) |
| `static/css/style.css` | Mise en forme |
| `static/js/script.js` | Récupère les valeurs du formulaire, envoie une requête POST à `/api/match`, affiche les résultats renvoyés en JSON |

## Logique du matching (dans `app.py`)
1. On charge tous les mentors depuis PostgreSQL.
2. Pour chaque mentor : on vérifie qu'il y a au moins une matière en commun.
3. On vérifie qu'il a un créneau le même jour, à ± 1h de l'heure demandée.
4. Score = 10 points par matière commune + 5 points si la filière correspond.
5. On trie les résultats par score décroissant et on renvoie le JSON au frontend.

## Note sur "travail individuel"
Le code est prêt à l'emploi mais reste simple : relis chaque fichier avant de le soumettre pour être capable de l'expliquer à l'oral (présentation du 06 juillet), le rattrapage évalue ta compréhension autant que le résultat.
