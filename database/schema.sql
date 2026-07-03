
-- IFRI_MentorLink - Rattrapage 


DROP TABLE IF EXISTS mentors;

CREATE TABLE mentors (
    id               SERIAL PRIMARY KEY,
    nom              VARCHAR(100) NOT NULL,
    matieres         TEXT[] NOT NULL,       -- ex: {'Python','Algorithmique'}
    disponibilites   TEXT[] NOT NULL,       -- ex: {'Lundi 14:00','Mercredi 10:00'}
    filiere          VARCHAR(50),           -- IA, IM, GL, SE_IoT, SI
    format_mentorat  VARCHAR(20) CHECK (format_mentorat IN ('presentiel','en ligne','les deux'))
);

-- Jeu de donnees 
INSERT INTO mentors (nom, matieres, disponibilites, filiere, format_mentorat) VALUES
('MENSAH Kokou',
 ARRAY['Algorithmique','Python','Langage SQL'],
 ARRAY['Lundi 14:00','Mercredi 10:00','Vendredi 16:00'],
 'GL', 'les deux'),

('ADJOVI Rachelle',
 ARRAY['Analyse','Recherche Operationnelle'],
 ARRAY['Mardi 09:00','Jeudi 15:00'],
 'IA', 'en ligne'),

('GBAGUIDI Eric',
 ARRAY['SQL','Langage C','Algebre relationnelle'],
 ARRAY['Lundi 08:00','Samedi 10:00'],
 'SE_IoT', 'presentiel');
