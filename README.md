# ✨ NumerologieWeb

> Analyse numérologique complète — découvrez vos nombres, cycles de vie et compatibilité.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![React](https://img.shields.io/badge/Frontend-React%2018-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)
![License](https://img.shields.io/badge/License-Proprietary-red)

---

## Qu'est-ce que NumerologieWeb ?

NumerologieWeb est une application web full-stack qui calcule et interprète vos **nombres numérологiques** à partir de votre prénom, nom et date de naissance.  
Interface mystique violet/or — entièrement locale, aucune donnée envoyée à l'extérieur.

---

## Fonctionnalités

| Fonctionnalité | Détails |
|---|---|
| 🌠 Chemin de vie | Calculé depuis la date de naissance, réduit aux nombres maîtres |
| 🎭 Nombre d'expression | Basé sur toutes les lettres du nom complet |
| 💖 Nombre de motivation | Calculé depuis les voyelles du nom |
| 🧱 Nombre de réalisation | Calculé depuis les consonnes du nom |
| 🌀 Cycles de vie | 3 cycles majeurs (0–27, 28–56, 57+) avec interprétations |
| ⚖️ Analyse d'équilibre | Cohérence entre chemin, expression et motivation |
| 💀 Lettres karmiques | Détection des vibrations manquantes dans le nom |
| ❤️ Compatibilité | Comparaison de deux profils avec score et verdict |
| ⭐ Nombres maîtres | Détection et mise en valeur des nombres 11, 22, 33 |

---

## Méthode de calcul

```
Prénom + Nom  ──► nettoyage (accents, casse) ──► table pythagoricienne
                                                         │
                               ┌─────────────────────────┤
                               │                         │
                          Consonnes                  Voyelles
                               │                         │
                          Réalisation               Motivation
                               └────────┬────────────────┘
                                        │
                                   Expression (toutes lettres)

Date de naissance ──► somme des chiffres ──► réduction ──► Chemin de vie
                                           (conserve 11, 22, 33)
```

---

## Installation

```bash
git clone https://github.com/ApollonIUGB77/NumerologieWeb.git
cd NumerologieWeb
```

### Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
# API disponible sur http://localhost:8001
```

### Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
# App disponible sur http://localhost:5173
```

---

## Structure du projet

```
NumerologieWeb/
├── backend/
│   ├── main.py           # API FastAPI — routes /analyze et /compatibility
│   ├── numerology.py     # Moteur de calcul numérologique complet
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.tsx                      # Shell principal — 2 onglets
    │   └── components/
    │       ├── ProfileTab.tsx           # Onglet profil complet
    │       ├── CompatibilityTab.tsx     # Onglet compatibilité
    │       ├── ProfileResult.tsx        # Affichage des résultats
    │       ├── NumberCard.tsx           # Carte par nombre
    │       └── PersonForm.tsx           # Formulaire de saisie
    ├── tailwind.config.js               # Thème mystique violet/or
    └── vite.config.ts
```

---

## API Endpoints

| Méthode | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/analyze` | Profil numérologique complet |
| `POST` | `/compatibility` | Compatibilité entre deux personnes |

---

## Tech Stack

- **Backend** — FastAPI, Python 3.11, Uvicorn
- **Calculs** — Python natif (unicodedata, arithmétique)
- **Frontend** — React 18, TypeScript, Vite
- **Styling** — Tailwind CSS (thème mystique personnalisé)
- **HTTP** — Axios

---

## Auteur

**Aboubacar Sidick Meite** — Cybersecurity Student  
[GitHub](https://github.com/ApollonIUGB77)

---

## Licence

© 2026 Aboubacar Sidick Meite — Tous droits réservés.  
Toute reproduction ou distribution non autorisée est strictement interdite.
