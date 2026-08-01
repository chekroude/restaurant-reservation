# 🌐 Restaurant Reservation

Une application web permettant de réserver une table dans un restaurant en quelques clics — de la recherche à la confirmation.

![Statut](https://img.shields.io/badge/statut-fonctionnel-brightgreen)
![Licence](https://img.shields.io/badge/licence-MIT-blue)

##  Aperçu

| Connexion | Restaurants | Réservation |
|---|---|---|
| ![login](images/login.png) | ![home](images/home.png) | ![reserve](images/reserve.png) |

##  À propos du projet

Cette application permet à un utilisateur de créer un compte, de parcourir une liste de restaurants filtrable par ville, de consulter les détails d'un établissement, puis de réserver une table à une date et heure précises. L'historique complet des réservations est disponible à tout moment.

Le projet a été conçu comme un exercice complet de développement Full-Stack : de la conception de la base de données à la sécurisation de l'API, en passant par une interface entièrement responsive.

##  Fonctionnalités

-  Authentification sécurisée (inscription / connexion)
-  Liste des restaurants avec recherche par ville en temps réel
-  Réservation avec choix de la date et de l'heure
-  Historique complet des réservations de l'utilisateur
-  Interface entièrement responsive (mobile / tablette / desktop)
-  Design original avec identité visuelle propre au projet

##  Compétences techniques démontrées

| Domaine | Compétences |
|---|---|
| **Frontend** | HTML sémantique, CSS moderne (variables, grid, flexbox), JavaScript (Fetch API, async/await, DOM) |
| **Backend** | API REST avec Flask, architecture en couches (routes / utils / database) |
| **Base de données** | Modélisation relationnelle MySQL, clés étrangères, requêtes paramétrées |
| **Sécurité** | Authentification JWT, hashage bcrypt, protection contre l'injection SQL |
| **Outils** | Git, structuration de projet, variables d'environnement |

##  Stack technique

| Couche | Technologie |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Backend | Python, Flask, API REST |
| Base de données | MySQL |
| Sécurité | JWT (PyJWT), bcrypt |

##  Structure du projet

```
restaurant-reservation/
├── README.md
├── LICENSE
├── .gitignore
├── images/                 
├── backend/
│   ├── app/
│   │   ├── routes/          
│   │   └── utils/           
│   ├── database.py          
│   ├── database.sql        
│   ├── run.py                
│   └── requirements.txt
└── frontend/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── api.js            
    └── pages/
        ├── login.html
        ├── restaurants.html
        ├── reserve.html
        └── history.html
```


## Installation locale

### Prérequis

- Python 3.10+
- MySQL (via WAMP, XAMPP, ou installation native)

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-pseudo/restaurant-reservation.git
cd restaurant-reservation/backend
```

### 2. Configurer l'environnement Python

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 3. Configurer la base de données

```bash
copy .env.example .env
```

Modifier le fichier `.env` avec tes identifiants MySQL, puis :

```bash
mysql -u root -p < database.sql
```

### 4. Lancer le serveur

```bash
python run.py
```

L'API est disponible sur `http://localhost:5000`.

### 5. Ouvrir le frontend

Ouvrir `frontend/pages/login.html` dans un navigateur (ou via l'extension "Live Server" de VS Code).

##  Sécurité implémentée

- Mots de passe hashés avec **bcrypt** (jamais stockés en clair)
- Authentification par **JWT** (token valable 24h)
- Requêtes SQL **paramétrées** (protection contre l'injection SQL)
- Variables sensibles isolées dans `.env` (non versionné, exclu via `.gitignore`)

##  Roadmap

- [ ] Tests automatisés (unitaires + intégration)
- [ ] Annulation de réservation
- [ ] Vérification de la capacité disponible en temps réel
- [ ] Déploiement (Render / Railway pour le backend, Vercel pour le frontend)

##  Licence

Ce projet est sous licence MIT — voir le fichier [LICENSE](LICENSE).

##  Auteur

Projet réalisé dans le cadre d'un portfolio de développeur Full-Stack.

---



