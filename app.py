"""
IFRI_MentorLink - Rattrapage
Backend Flask : une seule route API qui fait le matching cote serveur.
"""

from flask import Flask, render_template, request, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# --- Connexion a la base de donnees ---
DB_CONFIG = dict(
    host="localhost",
    dbname="ifri_mentorlink",
    user="postgres",
    password="1234",
    port=5432,
    options='-c client_encoding=UTF8'
)


def get_conn():
    return psycopg2.connect(**DB_CONFIG, client_encoding='UTF8')


def parse_slot(slot: str):
    """'Lundi 14:00' -> ('Lundi', 840)  (840 minutes depuis minuit)"""
    jour, heure = slot.split(" ")
    h, m = map(int, heure.split(":"))
    return jour, h * 60 + m


def within_tolerance(minutes_a: int, minutes_b: int, tolerance: int = 60) -> bool:
    return abs(minutes_a - minutes_b) <= tolerance


# --- Route page unique ---
@app.route("/")
def index():
    return render_template("index.html")


# --- Route API : matching ---
@app.route("/api/match", methods=["POST"])
def match():
    data = request.get_json(force=True)

    matieres_recherchees = [
        m.strip().lower() for m in data.get("matieres", []) if m.strip()
    ]
    jour = (data.get("jour") or "").strip()
    heure = (data.get("heure") or "").strip()   # format "HH:MM"
    filiere = (data.get("filiere") or "").strip()

    if not matieres_recherchees or not jour or not heure:
        return jsonify({"error": "matieres, jour et heure sont obligatoires"}), 400

    h, m = map(int, heure.split(":"))
    minutes_demande = h * 60 + m

    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM mentors;")
    mentors = cur.fetchall()
    cur.close()
    conn.close()

    resultats = []

    for mentor in mentors:
        matieres_mentor = [x.lower() for x in mentor["matieres"]]
        communes = [m for m in matieres_recherchees if m in matieres_mentor]

        # Au moins une matiere en commun
        if not communes:
            continue

        # Tolerance horaire de ± 1h le meme jour
        dispo_matchee = None
        for slot in mentor["disponibilites"]:
            jour_slot, minutes_slot = parse_slot(slot)
            if jour_slot.lower() == jour.lower() and within_tolerance(
                minutes_slot, minutes_demande
            ):
                dispo_matchee = slot
                break

        if dispo_matchee is None:
            continue

        # Score simple : +10 par matiere commune, +5 si filiere identique
        score = len(communes) * 10
        if filiere and mentor["filiere"] and filiere.lower() == mentor["filiere"].lower():
            score += 5

        resultats.append(
            {
                "nom": mentor["nom"],
                "matieres_communes": communes,
                "disponibilites": mentor["disponibilites"],
                "creneau_correspondant": dispo_matchee,
                "format_mentorat": mentor["format_mentorat"],
                "filiere": mentor["filiere"],
                "score": score,
            }
        )

    resultats.sort(key=lambda r: r["score"], reverse=True)
    return jsonify(resultats)


if __name__ == "__main__":
    app.run(debug=True)
