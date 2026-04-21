# âœ¨ NumerologieWeb

> Analyse numÃ©rologique complÃ¨te â€” dÃ©couvrez vos nombres, cycles de vie et compatibilitÃ©.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![React](https://img.shields.io/badge/Frontend-React%2018-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)
![License](https://img.shields.io/badge/License-Proprietary-red)

---

## Qu'est-ce que NumerologieWeb ?

NumerologieWeb est une application web full-stack qui calcule et interprÃ¨te vos **nombres numÃ©rÐ¾Ð»Ð¾Ð³iques** Ã  partir de votre prÃ©nom, nom et date de naissance.  
Interface mystique violet/or â€” entiÃ¨rement locale, aucune donnÃ©e envoyÃ©e Ã  l'extÃ©rieur.

---

## FonctionnalitÃ©s

| FonctionnalitÃ© | DÃ©tails |
|---|---|
| ðŸŒ  Chemin de vie | CalculÃ© depuis la date de naissance, rÃ©duit aux nombres maÃ®tres |
| ðŸŽ­ Nombre d'expression | BasÃ© sur toutes les lettres du nom complet |
| ðŸ’– Nombre de motivation | CalculÃ© depuis les voyelles du nom |
| ðŸ§± Nombre de rÃ©alisation | CalculÃ© depuis les consonnes du nom |
| ðŸŒ€ Cycles de vie | 3 cycles majeurs (0â€“27, 28â€“56, 57+) avec interprÃ©tations |
| âš–ï¸ Analyse d'Ã©quilibre | CohÃ©rence entre chemin, expression et motivation |
| ðŸ’€ Lettres karmiques | DÃ©tection des vibrations manquantes dans le nom |
| â¤ï¸ CompatibilitÃ© | Comparaison de deux profils avec score et verdict |
| â­ Nombres maÃ®tres | DÃ©tection et mise en valeur des nombres 11, 22, 33 |

---

## MÃ©thode de calcul

```
PrÃ©nom + Nom  â”€â”€â–º nettoyage (accents, casse) â”€â”€â–º table pythagoricienne
                                                         â”‚
                               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
                               â”‚                         â”‚
                          Consonnes                  Voyelles
                               â”‚                         â”‚
                          RÃ©alisation               Motivation
                               â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                        â”‚
                                   Expression (toutes lettres)

Date de naissance â”€â”€â–º somme des chiffres â”€â”€â–º rÃ©duction â”€â”€â–º Chemin de vie
                                           (conserve 11, 22, 33)
```

---

## Installation

```bash
git clone https://github.com/ApollonASM8977/NumerologieWeb.git
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
â”œâ”€â”€ backend/
â”‚   â”œâ”€â”€ main.py           # API FastAPI â€” routes /analyze et /compatibility
â”‚   â”œâ”€â”€ numerology.py     # Moteur de calcul numÃ©rologique complet
â”‚   â””â”€â”€ requirements.txt
â”‚
â””â”€â”€ frontend/
    â”œâ”€â”€ src/
    â”‚   â”œâ”€â”€ App.tsx                      # Shell principal â€” 2 onglets
    â”‚   â””â”€â”€ components/
    â”‚       â”œâ”€â”€ ProfileTab.tsx           # Onglet profil complet
    â”‚       â”œâ”€â”€ CompatibilityTab.tsx     # Onglet compatibilitÃ©
    â”‚       â”œâ”€â”€ ProfileResult.tsx        # Affichage des rÃ©sultats
    â”‚       â”œâ”€â”€ NumberCard.tsx           # Carte par nombre
    â”‚       â””â”€â”€ PersonForm.tsx           # Formulaire de saisie
    â”œâ”€â”€ tailwind.config.js               # ThÃ¨me mystique violet/or
    â””â”€â”€ vite.config.ts
```

---

## API Endpoints

| MÃ©thode | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/analyze` | Profil numÃ©rologique complet |
| `POST` | `/compatibility` | CompatibilitÃ© entre deux personnes |

---

## Tech Stack

- **Backend** â€” FastAPI, Python 3.11, Uvicorn
- **Calculs** â€” Python natif (unicodedata, arithmÃ©tique)
- **Frontend** â€” React 18, TypeScript, Vite
- **Styling** â€” Tailwind CSS (thÃ¨me mystique personnalisÃ©)
- **HTTP** â€” Axios

---

## Auteur

**Aboubacar Sidick Meite** â€” Cybersecurity Student  
[GitHub](https://github.com/ApollonASM8977)

---

## Licence

Â© 2026 Aboubacar Sidick Meite â€” Tous droits rÃ©servÃ©s.  
Toute reproduction ou distribution non autorisÃ©e est strictement interdite.

