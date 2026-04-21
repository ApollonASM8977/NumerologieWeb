# Â© 2026 Aboubacar Sidick Meite (ApollonASM8977) â€” All Rights Reserved
"""Core numerology calculation engine â€” ported from console script."""

import unicodedata

# â”€â”€ Letter table â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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

# â”€â”€ Helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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

# â”€â”€ Core calculations â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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
        return "Parfaite harmonie entre votre mission, votre nature et vos dÃ©sirs."
    elif chemin == expression or chemin == motivation or expression == motivation:
        return "Bonne cohÃ©rence entre vos Ã©nergies principales."
    return "Contrastes entre vos aspirations â€” tension crÃ©atrice Ã  apprivoiser."


def compatibilite(c1: int, c2: int) -> dict:
    diff = abs(c1 - c2)
    if c1 == c2:
        score, label, desc = 95, "Ã‚mes sÅ“urs", "Vous partagez les mÃªmes vibrations fondamentales."
    elif diff == 1:
        score, label, desc = 80, "TrÃ¨s compatible", "PersonnalitÃ©s complÃ©mentaires et naturellement attirÃ©es."
    elif diff in (2, 3):
        score, label, desc = 65, "Compatible", "Bonne entente possible avec respect mutuel."
    elif diff in (4, 5):
        score, label, desc = 45, "DiffÃ©rences notables", "Des efforts d'adaptation seront nÃ©cessaires."
    else:
        score, label, desc = 30, "Contrastes forts", "Ã‰nergies trÃ¨s diffÃ©rentes â€” comprÃ©hension profonde requise."
    return {"score": score, "label": label, "description": desc}

# â”€â”€ Interpretations â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

_CHEMIN = {
    1:  ("Leader", "Leader nÃ©, indÃ©pendant et ambitieux. Votre mission est d'ouvrir la voie et d'innover."),
    2:  ("Diplomate", "Diplomate, sensible et coopÃ©ratif. Vous excellez dans les relations humaines."),
    3:  ("CrÃ©ateur", "CrÃ©atif, joyeux et communicatif. Vous Ãªtes fait pour l'expression artistique."),
    4:  ("BÃ¢tisseur", "OrganisÃ©, rigoureux et stable. Votre force est la structure et la discipline."),
    5:  ("Explorateur", "Libre, curieux et aventureux. Vous Ãªtes fait pour le changement et l'exploration."),
    6:  ("Protecteur", "Responsable, attentionnÃ©. Vous incarnez l'harmonie familiale et communautaire."),
    7:  ("Chercheur", "Introspectif, spirituel et analytique. Vous cherchez la vÃ©ritÃ© et la profondeur."),
    8:  ("StratÃ¨ge", "Ambitieux, stratÃ¨ge et orientÃ© vers la rÃ©ussite matÃ©rielle et le leadership."),
    9:  ("Humaniste", "Altruiste, gÃ©nÃ©reux et universel. Votre mission est de servir l'humanitÃ©."),
    11: ("Visionnaire", "MaÃ®tre visionnaire â€” messager intuitif et inspirant d'une rare Ã©lÃ©vation spirituelle."),
    22: ("Grand BÃ¢tisseur", "MaÃ®tre bÃ¢tisseur â€” vous avez le potentiel de concrÃ©tiser de grandes visions collectives."),
    33: ("MaÃ®tre Enseignant", "MaÃ®tre enseignant â€” vous incarnez l'amour inconditionnel et la guÃ©rison universelle."),
}

_EXPRESSION = {
    1: ("AffirmÃ©", "Expression directe et affirmÃ©e. Vous imposez votre volontÃ© naturellement."),
    2: ("Doux", "Expression douce et diplomatique. Vous cherchez l'Ã©quilibre et la paix."),
    3: ("Joyeux", "Expression joyeuse et artistique. Vous aimez captiver et sÃ©duire par les mots."),
    4: ("StructurÃ©", "Expression structurÃ©e et fiable. Vous rassurez par votre sÃ©rieux."),
    5: ("Libre", "Expression libre et sÃ©duisante, parfois imprÃ©visible mais toujours vivante."),
    6: ("Chaleureux", "Expression chaleureuse et familiale. Vous portez les autres naturellement."),
    7: ("Profond", "Expression profonde et analytique. Vous inspirez par votre rÃ©flexion."),
    8: ("Puissant", "Expression puissante et dirigeante. Vous inspirez respect et autoritÃ©."),
    9: ("Universel", "Expression universelle et humanitaire. Vous parlez Ã  l'Ã¢me de tous."),
    11: ("Lumineux", "Expression lumineuse et inspirante. Vous touchez les autres en profondeur."),
    22: ("Constructif", "Expression ambitieuse et constructive. Vous bÃ¢tissez par vos paroles."),
    33: ("Nourrissant", "Expression nourriciÃ¨re et enseignante. Vous guÃ©rissez par votre prÃ©sence."),
}

_MOTIVATION = {
    1: ("IndÃ©pendance", "Vous dÃ©sirez mener, crÃ©er et affirmer votre identitÃ© unique."),
    2: ("Harmonie", "Vous cherchez l'amour, la paix et la collaboration sincÃ¨re."),
    3: ("Joie", "Vous avez soif de plaisir, d'expression crÃ©ative et de lÃ©gÃ¨retÃ©."),
    4: ("StabilitÃ©", "Vous dÃ©sirez la stabilitÃ©, l'ordre et un cadre solide."),
    5: ("LibertÃ©", "Vous aspirez Ã  la libertÃ© absolue, au mouvement et Ã  l'expÃ©rience."),
    6: ("Amour", "Vous voulez servir, aimer, prendre soin des Ãªtres qui vous entourent."),
    7: ("VÃ©ritÃ©", "Vous cherchez Ã  comprendre, mÃ©diter, analyser le sens profond."),
    8: ("RÃ©ussite", "Vous voulez rÃ©ussir, maÃ®triser et exercer une influence rÃ©elle."),
    9: ("Service", "Vous aspirez Ã  servir les autres avec compassion et universalitÃ©."),
    11: ("Ã‰veil", "Vous ressentez un appel intÃ©rieur fort Ã  Ã©veiller et inspirer."),
    22: ("Impact", "Vous Ãªtes motivÃ© par une vision concrÃ¨te Ã  impact collectif majeur."),
    33: ("GuÃ©rison", "Vous avez le dÃ©sir profond d'apporter l'amour et la guÃ©rison."),
}

_REALISATION = {
    1: ("Pionnier", "Vous Ãªtes perÃ§u comme affirmÃ©, indÃ©pendant et profondÃ©ment motivÃ©."),
    2: ("MÃ©diateur", "On vous voit comme diplomate, sociable et porteur de paix."),
    3: ("Artiste", "Vous Ãªtes perÃ§u comme joyeux, expressif et plein de vie."),
    4: ("Pilier", "Vous montrez une image sÃ©rieuse, stable et rassurante."),
    5: ("Dynamique", "Votre image publique est dynamique, vive et toujours adaptable."),
    6: ("Bienveillant", "Vous Ãªtes vu comme bienveillant, serviable et ancrÃ© dans le cÅ“ur."),
    7: ("MystÃ©rieux", "On vous perÃ§oit comme rÃ©flÃ©chi, mystÃ©rieux et profond."),
    8: ("AutoritÃ©", "Vous inspirez le respect, la maÃ®trise et la rÃ©ussite."),
    9: ("Sage", "Vous Ãªtes perÃ§u comme gÃ©nÃ©reux, humaniste et sage."),
    11: ("Inspirant", "Vous Ãªtes perÃ§u comme une prÃ©sence unique, intense et inspirante."),
    22: ("Responsable", "On vous voit comme quelqu'un de responsable, bÃ¢tisseur et crÃ©dible."),
    33: ("LumiÃ¨re", "Vous dÃ©gagez une prÃ©sence chaleureuse, protectrice et lumineuse."),
}


def interpret(table: dict, n: int) -> dict:
    title, text = table.get(n, ("â€”", "InterprÃ©tation non disponible."))
    return {"title": title, "text": text}


# â”€â”€ Main analysis â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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
            {"label": "Cycle 1 (0â€“27 ans)",  "valeur": c1, "desc": f"Enfance et formation sous l'Ã©nergie du {c1}."},
            {"label": "Cycle 2 (28â€“56 ans)", "valeur": c2, "desc": f"Vie adulte orientÃ©e par les qualitÃ©s du {c2}."},
            {"label": "Cycle 3 (57+ ans)",   "valeur": c3, "desc": f"Accomplissement marquÃ© par la vibration du {c3}."},
        ],
        "equilibre": analyse_equilibre(chemin, expr, motiv),
        "lettres_manquantes": manquantes,
        "master_number": chemin in (11, 22, 33),
    }

