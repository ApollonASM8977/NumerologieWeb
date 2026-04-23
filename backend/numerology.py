# © 2026 Aboubacar Sidick Meite (ApollonASM8977) — All Rights Reserved
"""Core numerology calculation engine — ported from console script."""

import unicodedata

# ── Letter table ──────────────────────────────────────────────────────────────

TABLE_LETTRES: dict[str, int] = {
    'A':1,'J':1,'S':1,
    'B':2,'K':2,'T':2,
    'C':3,'L':3,'U':3,
    'D':4,'M':4,'V':4,
    'E':5,'N':5,'W':5,
    'F':6,'O':6,'X':6,
    'G':7,'P':7,'Y':7,
    'H':8,'Q':8,'Z':8,
    'I':9,'R':9,
}

VOYELLES = set('AEIOUY')

# ── Helpers ───────────────────────────────────────────────────────────────────

def nettoyer_nom(nom: str) -> str:
    nom = nom.upper()
    nom = unicodedata.normalize('NFD', nom)
    nom = ''.join(c for c in nom if unicodedata.category(c) != 'Mn')
    return ''.join(c for c in nom if c.isalpha())


def reduire_nombre(n: int) -> int:
    """Reduce keeping master numbers 11, 22, 33."""
    while n not in (11, 22, 33) and n > 9:
        n = sum(int(c) for c in str(n))
    return n


def reduire_simple(n: int) -> int:
    while n > 9:
        n = sum(int(c) for c in str(n))
    return n

# ── Core calculations ──────────────────────────────────────────────────────────

def chemin_de_vie(jj: int, mm: int, aaaa: int) -> int:
    total = sum(int(c) for c in f"{jj:02d}{mm:02d}{aaaa}")
    return reduire_nombre(total)


def nombre_expression(nom: str) -> int:
    return reduire_nombre(sum(TABLE_LETTRES.get(c, 0) for c in nom))


def nombre_motivation(nom: str) -> int:
    return reduire_nombre(sum(TABLE_LETTRES.get(c, 0) for c in nom if c in VOYELLES))


def nombre_realisation(nom: str) -> int:
    return reduire_nombre(sum(TABLE_LETTRES.get(c, 0) for c in nom if c not in VOYELLES))


def cycles_majeurs(jj: int, mm: int, aaaa: int) -> tuple[int, int, int]:
    return reduire_simple(jj), reduire_simple(mm), reduire_simple(aaaa)


def lettres_manquantes(nom: str) -> list[str]:
    present = set(nom)
    return [l for l in TABLE_LETTRES if l not in present]


def analyse_equilibre(chemin: int, expression: int, motivation: int) -> str:
    if chemin == expression == motivation:
        return "Parfaite harmonie entre votre mission, votre nature et vos désirs."
    elif chemin == expression or chemin == motivation or expression == motivation:
        return "Bonne cohérence entre vos énergies principales."
    return "Contrastes entre vos aspirations — tension créatrice à apprivoiser."


def compatibilite(c1: int, c2: int) -> dict:
    diff = abs(c1 - c2)
    if c1 == c2:
        score, label, desc = 95, "Âmes sœurs", "Vous partagez les mêmes vibrations fondamentales."
    elif diff == 1:
        score, label, desc = 80, "Très compatible", "Personnalités complémentaires et naturellement attirées."
    elif diff in (2, 3):
        score, label, desc = 65, "Compatible", "Bonne entente possible avec respect mutuel."
    elif diff in (4, 5):
        score, label, desc = 45, "Différences notables", "Des efforts d'adaptation seront nécessaires."
    else:
        score, label, desc = 30, "Contrastes forts", "Énergies très différentes — compréhension profonde requise."
    return {"score": score, "label": label, "description": desc}

# ── Interpretations ───────────────────────────────────────────────────────────

_CHEMIN = {
    1:  ("Leader", "Leader né, indépendant et ambitieux. Votre mission est d'ouvrir la voie et d'innover."),
    2:  ("Diplomate", "Diplomate, sensible et coopératif. Vous excellez dans les relations humaines."),
    3:  ("Créateur", "Créatif, joyeux et communicatif. Vous êtes fait pour l'expression artistique."),
    4:  ("Bâtisseur", "Organisé, rigoureux et stable. Votre force est la structure et la discipline."),
    5:  ("Explorateur", "Libre, curieux et aventureux. Vous êtes fait pour le changement et l'exploration."),
    6:  ("Protecteur", "Responsable, attentionné. Vous incarnez l'harmonie familiale et communautaire."),
    7:  ("Chercheur", "Introspectif, spirituel et analytique. Vous cherchez la vérité et la profondeur."),
    8:  ("Stratège", "Ambitieux, stratège et orienté vers la réussite matérielle et le leadership."),
    9:  ("Humaniste", "Altruiste, généreux et universel. Votre mission est de servir l'humanité."),
    11: ("Visionnaire", "Maître visionnaire — messager intuitif et inspirant d'une rare élévation spirituelle."),
    22: ("Grand Bâtisseur", "Maître bâtisseur — vous avez le potentiel de concrétiser de grandes visions collectives."),
    33: ("Maître Enseignant", "Maître enseignant — vous incarnez l'amour inconditionnel et la guérison universelle."),
}

_EXPRESSION = {
    1: ("Affirmé", "Expression directe et affirmée. Vous imposez votre volonté naturellement."),
    2: ("Doux", "Expression douce et diplomatique. Vous cherchez l'équilibre et la paix."),
    3: ("Joyeux", "Expression joyeuse et artistique. Vous aimez captiver et séduire par les mots."),
    4: ("Structuré", "Expression structurée et fiable. Vous rassurez par votre sérieux."),
    5: ("Libre", "Expression libre et séduisante, parfois imprévisible mais toujours vivante."),
    6: ("Chaleureux", "Expression chaleureuse et familiale. Vous portez les autres naturellement."),
    7: ("Profond", "Expression profonde et analytique. Vous inspirez par votre réflexion."),
    8: ("Puissant", "Expression puissante et dirigeante. Vous inspirez respect et autorité."),
    9: ("Universel", "Expression universelle et humanitaire. Vous parlez à l'âme de tous."),
    11: ("Lumineux", "Expression lumineuse et inspirante. Vous touchez les autres en profondeur."),
    22: ("Constructif", "Expression ambitieuse et constructive. Vous bâtissez par vos paroles."),
    33: ("Nourrissant", "Expression nourricière et enseignante. Vous guérissez par votre présence."),
}

_MOTIVATION = {
    1: ("Indépendance", "Vous désirez mener, créer et affirmer votre identité unique."),
    2: ("Harmonie", "Vous cherchez l'amour, la paix et la collaboration sincère."),
    3: ("Joie", "Vous avez soif de plaisir, d'expression créative et de légèreté."),
    4: ("Stabilité", "Vous désirez la stabilité, l'ordre et un cadre solide."),
    5: ("Liberté", "Vous aspirez à la liberté absolue, au mouvement et à l'expérience."),
    6: ("Amour", "Vous voulez servir, aimer, prendre soin des êtres qui vous entourent."),
    7: ("Vérité", "Vous cherchez à comprendre, méditer, analyser le sens profond."),
    8: ("Réussite", "Vous voulez réussir, maîtriser et exercer une influence réelle."),
    9: ("Service", "Vous aspirez à servir les autres avec compassion et universalité."),
    11: ("Éveil", "Vous ressentez un appel intérieur fort à éveiller et inspirer."),
    22: ("Impact", "Vous êtes motivé par une vision concrète à impact collectif majeur."),
    33: ("Guérison", "Vous avez le désir profond d'apporter l'amour et la guérison."),
}

_REALISATION = {
    1: ("Pionnier", "Vous êtes perçu comme affirmé, indépendant et profondément motivé."),
    2: ("Médiateur", "On vous voit comme diplomate, sociable et porteur de paix."),
    3: ("Artiste", "Vous êtes perçu comme joyeux, expressif et plein de vie."),
    4: ("Pilier", "Vous montrez une image sérieuse, stable et rassurante."),
    5: ("Dynamique", "Votre image publique est dynamique, vive et toujours adaptable."),
    6: ("Bienveillant", "Vous êtes vu comme bienveillant, serviable et ancré dans le cœur."),
    7: ("Mystérieux", "On vous perçoit comme réfléchi, mystérieux et profond."),
    8: ("Autorité", "Vous inspirez le respect, la maîtrise et la réussite."),
    9: ("Sage", "Vous êtes perçu comme généreux, humaniste et sage."),
    11: ("Inspirant", "Vous êtes perçu comme une présence unique, intense et inspirante."),
    22: ("Responsable", "On vous voit comme quelqu'un de responsable, bâtisseur et crédible."),
    33: ("Lumière", "Vous dégagez une présence chaleureuse, protectrice et lumineuse."),
}


def interpret(table: dict, n: int) -> dict:
    title, text = table.get(n, ("—", "Interprétation non disponible."))
    return {"title": title, "text": text}


# ── Main analysis ──────────────────────────────────────────────────────────────

def analyser(prenom: str, nom: str, jour: int, mois: int, annee: int) -> dict:
    nom_net = nettoyer_nom(prenom + " " + nom)
    chemin  = chemin_de_vie(jour, mois, annee)
    expr    = nombre_expression(nom_net)
    motiv   = nombre_motivation(nom_net)
    real    = nombre_realisation(nom_net)
    c1, c2, c3 = cycles_majeurs(jour, mois, annee)
    manquantes = lettres_manquantes(nom_net)

    return {
        "prenom": prenom,
        "nom": nom,
        "date": f"{jour:02d}/{mois:02d}/{annee}",
        "chemin_de_vie": {
            "valeur": chemin,
            **interpret(_CHEMIN, chemin),
        },
        "expression": {
            "valeur": expr,
            **interpret(_EXPRESSION, expr),
        },
        "motivation": {
            "valeur": motiv,
            **interpret(_MOTIVATION, motiv),
        },
        "realisation": {
            "valeur": real,
            **interpret(_REALISATION, real),
        },
        "cycles": [
            {"label": "Cycle 1 (0–27 ans)",  "valeur": c1, "desc": f"Enfance et formation sous l'énergie du {c1}."},
            {"label": "Cycle 2 (28–56 ans)", "valeur": c2, "desc": f"Vie adulte orientée par les qualités du {c2}."},
            {"label": "Cycle 3 (57+ ans)",   "valeur": c3, "desc": f"Accomplissement marqué par la vibration du {c3}."},
        ],
        "equilibre": analyse_equilibre(chemin, expr, motiv),
        "lettres_manquantes": manquantes,
        "master_number": chemin in (11, 22, 33),
    }

