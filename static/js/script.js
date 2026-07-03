document.getElementById('search-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const matieres = document.getElementById('matieres').value
    .split(',')
    .map(m => m.trim())
    .filter(Boolean);

  const jour = document.getElementById('jour').value;
  const heure = document.getElementById('heure').value;
  const filiere = document.getElementById('filiere').value;

  const resultatsDiv = document.getElementById('resultats');
  resultatsDiv.innerHTML = '<p class="empty">Recherche en cours...</p>';

  try {
    const response = await fetch('/api/match', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ matieres, jour, heure, filiere })
    });

    const data = await response.json();

    if (!response.ok) {
      resultatsDiv.innerHTML = `<p class="empty">Erreur : ${data.error}</p>`;
      return;
    }

    if (data.length === 0) {
      resultatsDiv.innerHTML = '<p class="empty">Aucun mentor compatible trouvé.</p>';
      return;
    }

    resultatsDiv.innerHTML = data.map(mentor => `
      <div class="mentor-card">
        <h3>${mentor.nom} <span class="score">(${mentor.score} pts)</span></h3>
        <p><strong>Matières en commun :</strong> ${mentor.matieres_communes.join(', ')}</p>
        <p><strong>Créneau correspondant :</strong> ${mentor.creneau_correspondant}</p>
        <p><strong>Toutes disponibilités :</strong> ${mentor.disponibilites.join(', ')}</p>
        <p><strong>Format :</strong> ${mentor.format_mentorat}</p>
        <p><strong>Filière :</strong> ${mentor.filiere || 'Non précisée'}</p>
      </div>
    `).join('');

  } catch (err) {
    resultatsDiv.innerHTML = '<p class="empty">Erreur de connexion au serveur.</p>';
  }
});
