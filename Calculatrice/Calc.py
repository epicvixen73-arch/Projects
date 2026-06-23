"""
Calculatrice scientifique (Maths / Physique / Formules)
=========================================================

Architecture
------------
Toutes les opérations sont organisées en un arbre de menus :
  - un `Menu` regroupe plusieurs `Action` et/ou sous-`Menu` ;
  - une `Action` représente un calcul exécutable (une fonction `calc_xxx`).

Le moteur de navigation (`choisir`, `executer_noeud`) est entièrement
générique : il ne connaît ni les libellés ni le nombre d'options, il se
contente de parcourir la structure `Menu`/`Action` qu'on lui donne.

La liste "Formules" est elle aussi générée automatiquement à partir de ce
même arbre (fonction `collecter_formules`) : il n'y a qu'UN SEUL endroit où
chaque calcul est décrit, donc aucune duplication possible entre le menu de
navigation et la liste de référence.

Pour ajouter un nouveau calcul
------------------------------
1. Écrire une fonction `calc_xxx()` qui lit les entrées au clavier, fait le
   calcul, affiche le résultat et l'ajoute à `historique`.
2. L'ajouter avec `Action("Mon calcul", calc_xxx, "formule (optionnel)")`
   dans la liste `items` du `Menu` concerné (section "ARBRE DES MENUS").

C'est tout : pas de liste de validation à mettre à jour, pas de nouvel
`elif`, pas de numérotation à synchroniser ailleurs dans le fichier.
"""

from dataclasses import dataclass, field
from math import sqrt, factorial, e, cos, sin, tan, acos, asin, atan, radians, degrees
from time import sleep
from typing import Callable, Optional, Union

# ---------------------------------------------------------------------------
# Constantes physiques
# ---------------------------------------------------------------------------
G_UNIVERSELLE = 6.674e-11   # constante de gravitation universelle
G_TERRESTRE = 9.81          # accélération de pesanteur à la surface de la Terre
NA = 6.02e23                # nombre d'Avogadro
C_LUMIERE = 3e8              # vitesse de la lumière dans le vide (m/s)
MASSE_PROTON = 1.673e-27
MASSE_NEUTRON = 1.675e-27
MASSE_ELECTRON = 9.110e-31

# ---------------------------------------------------------------------------
# État global : historique des calculs effectués durant la session
# ---------------------------------------------------------------------------
historique: list[str] = []


# ---------------------------------------------------------------------------
# Utilitaires de saisie
# ---------------------------------------------------------------------------
def arrondi(valeur, precision: int = 4):
    return round(valeur, precision)


def saisir_entier(message: str, valeurs_valides: Optional[list[int]] = None) -> int:
    """Demande un entier, en boucle jusqu'à obtenir une valeur valide."""
    while True:
        try:
            choix = int(input(message))
            if valeurs_valides is None or choix in valeurs_valides:
                return choix
            print(f"Invalide. Nombre nécessaire parmi {valeurs_valides}")
        except ValueError:
            print("Merci d'entrer un nombre entier valide.")


def saisir_nombre(message: str) -> float:
    """Demande un nombre décimal, en boucle jusqu'à obtenir une valeur valide."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Merci d'entrer un nombre valide.")


# ---------------------------------------------------------------------------
# Modèle de données : Action / Menu
# ---------------------------------------------------------------------------
@dataclass
class Action:
    """Un calcul exécutable, feuille de l'arbre."""
    label: str
    fonction: Callable[[], None]
    formule: Optional[str] = None  # texte affiché dans la liste "Formules"


@dataclass
class Menu:
    """Un regroupement d'Action et/ou de sous-Menu."""
    label: str
    items: list = field(default_factory=list)        # list[Union[Action, "Menu"]]
    formule: Optional[str] = None                      # si renseigné : le menu
                                                         # entier représente UNE
                                                         # formule (ex: Thalès)
    recapitulatif: bool = False                        # marque le menu "Formules"


Noeud = Union[Action, Menu]


# ---------------------------------------------------------------------------
# Moteur de navigation générique
# ---------------------------------------------------------------------------
def choisir(menu: Menu) -> Noeud:
    """Affiche les options d'un menu et renvoie l'item choisi."""
    print(f"\n{menu.label}")
    for i, item in enumerate(menu.items, start=1):
        print(f"  {i}: {item.label}")
    n = saisir_entier("Choix : ", list(range(1, len(menu.items) + 1)))
    return menu.items[n - 1]


def executer_noeud(noeud: Noeud) -> None:
    """Descend dans l'arbre jusqu'à une Action exécutable, puis la lance.
    Cas particulier : le menu "Formules" déclenche l'affichage récapitulatif."""
    while isinstance(noeud, Menu) and not noeud.recapitulatif:
        noeud = choisir(noeud)
    if isinstance(noeud, Menu):
        afficher_formules()
    else:
        noeud.fonction()


def collecter_formules(menu: Menu) -> list[Noeud]:
    """Parcourt l'arbre et renvoie tous les nœuds porteurs d'une formule.

    Si un Menu possède lui-même une formule (ex: Thalès, Loi d'Ohm), on
    l'ajoute tel quel SANS descendre dans ses enfants : ses enfants ne sont
    que des variantes du même calcul (chercher U, R ou I, par exemple)."""
    resultats: list[Noeud] = []
    for item in menu.items:
        if item.formule is not None:
            resultats.append(item)
        elif isinstance(item, Menu):
            resultats.extend(collecter_formules(item))
    return resultats


def afficher_formules() -> None:
    entrees = collecter_formules(ARBRE)
    print("\nFormules disponibles :")
    for i, noeud in enumerate(entrees, start=1):
        print(f"  {i:2}: {noeud.label:<26}: {noeud.formule}")
    choix = saisir_entier("Choix : ", list(range(1, len(entrees) + 1)))
    executer_noeud(entrees[choix - 1])


# ===========================================================================
# CALCULS - MATHÉMATIQUES
# ===========================================================================

# --- Fonctions de base ------------------------------------------------------
def calc_carre():
    x = saisir_nombre("x: ")
    res = arrondi(x ** 2)
    print(f"L'image de {x} est {res} par la fonction carrée.")
    historique.append(f"Carrée: {x}**2 = {res}")


def calc_cube():
    x = saisir_nombre("x: ")
    res = arrondi(x ** 3)
    print(f"L'image de {x} est {res} par la fonction cube.")
    historique.append(f"Cube: {x}**3 = {res}")


def calc_inverse():
    x = saisir_nombre("x: ")
    res = arrondi(1 / x)
    print(f"L'image de {x} est {res} par la fonction inverse.")
    historique.append(f"Inverse: 1/{x} = {res}")


def calc_racine_carree():
    x = saisir_nombre("x: ")
    res = arrondi(sqrt(x))
    print(f"L'image de {x} est {res} par la fonction racine carrée.")
    historique.append(f"Racine carrée: sqrt({x}) = {res}")


def calc_valeur_absolue():
    x = saisir_nombre("x: ")
    res = arrondi(abs(x))
    print(f"L'image de {x} est {res} par la fonction valeur absolue.")
    historique.append(f"Valeur absolue: |{x}| = {res}")


# --- Fonctions spéciales -----------------------------------------------------
def calc_factorielle():
    n = saisir_entier("n: ")
    res = factorial(n)
    print(f"{n}! = {res}")
    historique.append(f"Factorielle: {n}! = {res}")


def calc_exponentielle():
    x = saisir_nombre("x: ")
    res = arrondi(e ** x)
    print(f"e**{x} = {res}")
    historique.append(f"Exponentielle: e**{x} = {res}")


# --- Coordonnées -------------------------------------------------------------
def calc_milieu():
    x1 = saisir_nombre("x1: ")
    y1 = saisir_nombre("y1: ")
    x2 = saisir_nombre("x2: ")
    y2 = saisir_nombre("y2: ")
    mx, my = arrondi((x1 + x2) / 2), arrondi((y1 + y2) / 2)
    print(f"Coordonnées du milieu: ({mx}, {my})")
    historique.append(f"Milieu: ({mx}, {my})")


def calc_distance():
    x1 = saisir_nombre("x1: ")
    y1 = saisir_nombre("y1: ")
    x2 = saisir_nombre("x2: ")
    y2 = saisir_nombre("y2: ")
    res = arrondi(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    print(f"Distance entre A et B: {res}")
    historique.append(f"Distance AB: {res}")


# --- Théorèmes : Pythagore ----------------------------------------------------
def calc_pythagore_theoreme():
    print("a² + b² = c²  (c est l'hypoténuse, inconnue)")
    a = saisir_nombre("a: ")
    b = saisir_nombre("b: ")
    res = arrondi(sqrt(a ** 2 + b ** 2))
    print(f"c = {res}")
    historique.append(f"Pythagore: c = {res}")


def calc_pythagore_reciproque():
    print("c² = a² + b²  (c désigne le plus grand côté)")
    cote_c = saisir_nombre("c: ")
    a = saisir_nombre("a: ")
    b = saisir_nombre("b: ")
    if round(cote_c ** 2, 6) == round(a ** 2 + b ** 2, 6):
        print(f"Triangle rectangle (réciproque de Pythagore) : {cote_c}² = {a}² + {b}²")
        historique.append("Pythagore (réciproque): triangle rectangle")
    else:
        print(f"Triangle NON rectangle (contraposée de Pythagore) : {cote_c}² ≠ {a}² + {b}²")
        historique.append("Pythagore (contraposée): triangle non rectangle")


# --- Théorèmes : Thalès -------------------------------------------------------
def calc_thales_ae():
    AB = saisir_nombre("AB: ")
    AD = saisir_nombre("AD: ")
    AC = saisir_nombre("AC: ")
    AE = arrondi((AD * AC) / AB)
    print(f"AE = {AE}")
    historique.append(f"Thalès: AE = {AE}")


def calc_thales_ac():
    AB = saisir_nombre("AB: ")
    AD = saisir_nombre("AD: ")
    AE = saisir_nombre("AE: ")
    AC = arrondi((AB * AE) / AD)
    print(f"AC = {AC}")
    historique.append(f"Thalès: AC = {AC}")


def calc_thales_ad():
    AB = saisir_nombre("AB: ")
    AE = saisir_nombre("AE: ")
    AC = saisir_nombre("AC: ")
    AD = arrondi((AB * AE) / AC)
    print(f"AD = {AD}")
    historique.append(f"Thalès: AD = {AD}")


def calc_thales_ab():
    AE = saisir_nombre("AE: ")
    AD = saisir_nombre("AD: ")
    AC = saisir_nombre("AC: ")
    AB = arrondi((AD * AC) / AE)
    print(f"AB = {AB}")
    historique.append(f"Thalès: AB = {AB}")


# --- Vecteurs : relation de Chasles -------------------------------------------
def calc_chasles_ac():
    AB = saisir_nombre("AB: ")
    BC = saisir_nombre("BC: ")
    AC = arrondi(AB + BC)
    print(f"AC = {AC}")
    historique.append(f"Chasles: AC = {AC}")


def calc_chasles_ab():
    AC = saisir_nombre("AC: ")
    BC = saisir_nombre("BC: ")
    AB = arrondi(AC - BC)
    print(f"AB = {AB}")
    historique.append(f"Chasles: AB = {AB}")


def calc_chasles_bc():
    AC = saisir_nombre("AC: ")
    AB = saisir_nombre("AB: ")
    BC = arrondi(AC - AB)
    print(f"BC = {BC}")
    historique.append(f"Chasles: BC = {BC}")


# --- Vecteurs : déterminant ---------------------------------------------------
def calc_determinant():
    x1 = saisir_nombre("Abscisse de u: ")
    y1 = saisir_nombre("Ordonnée de u: ")
    x2 = saisir_nombre("Abscisse de v: ")
    y2 = saisir_nombre("Ordonnée de v: ")
    det = arrondi(x1 * y2 - y1 * x2)
    print(f"det(u;v) = ({x1}*{y2}) - ({y1}*{x2}) = {det}")
    historique.append(f"Déterminant: det(u;v) = {det}")


# --- Triangles -----------------------------------------------------------------
def calc_somme_angulaire():
    angle1 = saisir_nombre("angle 1 (°): ")
    angle2 = saisir_nombre("angle 2 (°): ")
    angle3 = arrondi(180 - (angle1 + angle2))
    print(f"Le 3ème angle est de {angle3}°")
    historique.append(f"Somme angulaire: angle3 = {angle3}°")


def calc_cosinus():
    x = saisir_nombre("angle (°): ")
    res = arrondi(cos(radians(x)))
    print(f"cos({x}°) = {res}")
    historique.append(f"Cosinus: cos({x}°) = {res}")


def calc_sinus():
    x = saisir_nombre("angle (°): ")
    res = arrondi(sin(radians(x)))
    print(f"sin({x}°) = {res}")
    historique.append(f"Sinus: sin({x}°) = {res}")


def calc_tangente():
    x = saisir_nombre("angle (°): ")
    res = arrondi(tan(radians(x)))
    print(f"tan({x}°) = {res}")
    historique.append(f"Tangente: tan({x}°) = {res}")


def calc_arccosinus():
    x = saisir_nombre("x (entre -1 et 1): ")
    res = arrondi(degrees(acos(x)))
    print(f"arccos({x}) = {res}°")
    historique.append(f"ArcCosinus: arccos({x}) = {res}°")


def calc_arcsinus():
    x = saisir_nombre("x (entre -1 et 1): ")
    res = arrondi(degrees(asin(x)))
    print(f"arcsin({x}) = {res}°")
    historique.append(f"ArcSinus: arcsin({x}) = {res}°")


def calc_arctangente():
    x = saisir_nombre("x: ")
    res = arrondi(degrees(atan(x)))
    print(f"arctan({x}) = {res}°")
    historique.append(f"ArcTangente: arctan({x}) = {res}°")


# --- Taux ------------------------------------------------------------------
def calc_taux_evolution():
    a = saisir_nombre("Valeur de départ: ")
    b = saisir_nombre("Valeur d'arrivée: ")
    if a == 0:
        print("Erreur: la valeur de départ ne peut pas être 0.")
        return
    taux = arrondi((b - a) / a * 100)
    print(f"Taux d'évolution: {taux:.2f} %")
    historique.append(f"Taux évolution: {taux:.2f} %")


def calc_taux_global():
    a = saisir_nombre("Variation 1 (%): ")
    b = saisir_nombre("Variation 2 (%): ")
    var1, var2 = a / 100, b / 100
    taux = arrondi(((1 + var1) * (1 + var2) - 1) * 100)
    print(f"Taux global: {taux:.2f} %")
    historique.append(f"Taux global: {taux:.2f} %")


# ===========================================================================
# CALCULS - PHYSIQUE
# ===========================================================================

# --- Matière : masse volumique ------------------------------------------------
def calc_masse_volumique_rho():
    m = saisir_nombre("m (kg): ")
    V = saisir_nombre("V (m³): ")
    rho = arrondi(m / V)
    print(f"p = {rho} kg/m³")
    historique.append(f"Masse volumique: p = {rho} kg/m³")


def calc_masse_volumique_m():
    rho = saisir_nombre("p (kg/m³): ")
    V = saisir_nombre("V (m³): ")
    m = arrondi(rho * V)
    print(f"m = {m} kg")
    historique.append(f"Masse volumique: m = {m} kg")


def calc_masse_volumique_v():
    m = saisir_nombre("m (kg): ")
    rho = saisir_nombre("p (kg/m³): ")
    V = arrondi(m / rho)
    print(f"V = {V} m³")
    historique.append(f"Masse volumique: V = {V} m³")


def calc_masse_atome():
    x = saisir_entier("Nb de protons: ")
    y = saisir_entier("Nb de neutrons: ")
    z = saisir_entier("Nb d'électrons: ")
    m = x * MASSE_PROTON + y * MASSE_NEUTRON + z * MASSE_ELECTRON
    print(f"Masse de l'atome: {m:.3e} kg")
    historique.append(f"Masse atome: {m:.3e} kg")


def calc_mol():
    n_entites = saisir_nombre("Nombre d'entités: ")
    n_moles = arrondi(n_entites / NA)
    print(f"Nombre de moles: {n_moles:.4e} mol")
    historique.append(f"Mol: {n_moles:.4e} mol")


def calc_dilution_c2():
    C1 = saisir_nombre("C1 (mol/L): ")
    V1 = saisir_nombre("V1 (L): ")
    V2 = saisir_nombre("V2 (L): ")
    C2 = arrondi((C1 * V1) / V2)
    print(f"C2 = {C2} mol/L")
    historique.append(f"Dilution: C2 = {C2} mol/L")


def calc_dilution_v2():
    C1 = saisir_nombre("C1 (mol/L): ")
    V1 = saisir_nombre("V1 (L): ")
    C2 = saisir_nombre("C2 (mol/L): ")
    V2 = arrondi((C1 * V1) / C2)
    print(f"V2 = {V2} L")
    historique.append(f"Dilution: V2 = {V2} L")


# --- Électricité ---------------------------------------------------------------
def calc_ohm_u():
    R = saisir_nombre("R (Ω): ")
    I = saisir_nombre("I (A): ")
    U = arrondi(R * I)
    print(f"U = {U} V")
    historique.append(f"Ohm: U = {U} V")


def calc_ohm_r():
    U = saisir_nombre("U (V): ")
    I = saisir_nombre("I (A): ")
    R = arrondi(U / I)
    print(f"R = {R} Ω")
    historique.append(f"Ohm: R = {R} Ω")


def calc_ohm_i():
    U = saisir_nombre("U (V): ")
    R = saisir_nombre("R (Ω): ")
    I = arrondi(U / R)
    print(f"I = {I} A")
    historique.append(f"Ohm: I = {I} A")


def calc_puissance_ui():
    U = saisir_nombre("U (V): ")
    I = saisir_nombre("I (A): ")
    P = arrondi(U * I)
    print(f"P = {P} W")
    historique.append(f"Puissance: P = {P} W")


def calc_puissance_ri2():
    R = saisir_nombre("R (Ω): ")
    I = saisir_nombre("I (A): ")
    P = arrondi(R * I ** 2)
    print(f"P = {P} W")
    historique.append(f"Puissance: P = {P} W")


def calc_puissance_u2r():
    U = saisir_nombre("U (V): ")
    R = saisir_nombre("R (Ω): ")
    P = arrondi(U ** 2 / R)
    print(f"P = {P} W")
    historique.append(f"Puissance: P = {P} W")


def calc_energie_electrique():
    P = saisir_nombre("P (W): ")
    t = saisir_nombre("t (s): ")
    E = arrondi(P * t)
    print(f"E = {E} J  |  E = {E / 3600:.2f} Wh")
    historique.append(f"Energie: E = {E} J ({E / 3600:.2f} Wh)")


# --- Optique ---------------------------------------------------------------------
def calc_snell_descartes():
    n1 = saisir_nombre("n1: ")
    n2 = saisir_nombre("n2: ")
    i1 = saisir_nombre("i1 (°): ")
    sin_i2 = n1 * sin(radians(i1)) / n2
    if sin_i2 > 1:
        print("Réflexion totale")
        historique.append("Snell-Descartes: réflexion totale")
    else:
        i2 = arrondi(degrees(asin(sin_i2)))
        print(f"i2 = {i2}°")
        historique.append(f"Snell-Descartes: i2 = {i2}°")


def calc_indice_refraction_n():
    v = saisir_nombre("v (m/s): ")
    n = arrondi(C_LUMIERE / v)
    print(f"n = {n}")
    historique.append(f"Indice de réfraction: n = {n}")


def calc_indice_refraction_v():
    n = saisir_nombre("n: ")
    v = C_LUMIERE / n
    print(f"v = {v:.2e} m/s")
    historique.append(f"Indice de réfraction: v = {v:.2e} m/s")


# --- Vitesse moyenne ---------------------------------------------------------------
def calc_vitesse():
    d = saisir_nombre("d (m): ")
    t = saisir_nombre("t (s): ")
    v = arrondi(d / t)
    print(f"v = {v} m/s")
    historique.append(f"Vitesse moyenne: v = {v} m/s")


def calc_distance_temps():
    v = saisir_nombre("v (m/s): ")
    t = saisir_nombre("t (s): ")
    d = arrondi(v * t)
    print(f"d = {d} m")
    historique.append(f"Vitesse moyenne: d = {d} m")


def calc_temps():
    d = saisir_nombre("d (m): ")
    v = saisir_nombre("v (m/s): ")
    t = arrondi(d / v)
    print(f"t = {t} s")
    historique.append(f"Vitesse moyenne: t = {t} s")


# --- Forces ---------------------------------------------------------------------
def calc_force_gravitation():
    m1 = saisir_nombre("m1 (kg): ")
    m2 = saisir_nombre("m2 (kg): ")
    d = saisir_nombre("d (m): ")
    F = arrondi(G_UNIVERSELLE * m1 * m2 / d ** 2)
    print(f"F = {F:.2e} N")
    historique.append(f"Force de gravitation: F = {F:.2e} N")


def calc_poids():
    m = saisir_nombre("m (kg): ")
    P = arrondi(m * G_TERRESTRE)
    print(f"P = {P} N")
    historique.append(f"Poids: P = {P} N")


# ===========================================================================
# ARBRE DES MENUS
# ===========================================================================
# Tout ajout (nouveau calcul, nouvelle catégorie) se fait UNIQUEMENT ici.

# --- Maths -------------------------------------------------------------------
menu_fonctions_base = Menu("De base", [
    Action("Carrée", calc_carre, "x**2"),
    Action("Cube", calc_cube, "x**3"),
    Action("Inverse", calc_inverse, "1/x"),
    Action("Racine carrée", calc_racine_carree, "sqrt(x)"),
    Action("Valeur absolue", calc_valeur_absolue, "|x|"),
])

menu_fonctions_speciales = Menu("Spéciales", [
    Action("Factorielle", calc_factorielle, "n!"),
    Action("Exponentielle", calc_exponentielle, "e**x"),
])

menu_fonctions = Menu("Fonctions", [menu_fonctions_base, menu_fonctions_speciales])

menu_coordonnees = Menu("Coordonnées", [
    Action("Milieu", calc_milieu, "((x1+x2)/2 , (y1+y2)/2)"),
    Action("Distance", calc_distance, "sqrt((x2-x1)**2 + (y2-y1)**2)"),
])

menu_pythagore = Menu("Pythagore", [
    Action("Théorème", calc_pythagore_theoreme, "a**2 + b**2 = c**2"),
    Action("Réciproque / Contraposée", calc_pythagore_reciproque, "c**2 = a**2 + b**2"),
])

menu_thales = Menu("Thalès", [
    Action("Chercher AE", calc_thales_ae),
    Action("Chercher AC", calc_thales_ac),
    Action("Chercher AD", calc_thales_ad),
    Action("Chercher AB", calc_thales_ab),
], formule="AD/AB = AE/AC")

menu_theoremes = Menu("Théorèmes", [menu_pythagore, menu_thales])

menu_chasles = Menu("Relation de Chasles", [
    Action("Calculer AC", calc_chasles_ac),
    Action("Calculer AB", calc_chasles_ab),
    Action("Calculer BC", calc_chasles_bc),
], formule="AB + BC = AC")

menu_vecteurs = Menu("Vecteurs", [
    menu_chasles,
    Action("Déterminant", calc_determinant, "det(u;v) = x1*y2 - y1*x2"),
])

menu_trigo = Menu("Trigo", [
    Action("Cosinus", calc_cosinus, "cos(angle)"),
    Action("Sinus", calc_sinus, "sin(angle)"),
    Action("Tangente", calc_tangente, "tan(angle)"),
])

menu_arc_trigo = Menu("Arc trigo", [
    Action("ArcCosinus", calc_arccosinus, "arccos(x)"),
    Action("ArcSinus", calc_arcsinus, "arcsin(x)"),
    Action("ArcTangente", calc_arctangente, "arctan(x)"),
])

menu_trigonometrie = Menu("Trigonométrie", [menu_trigo, menu_arc_trigo])

menu_triangles = Menu("Triangles", [
    Action("Somme angulaire", calc_somme_angulaire, "180 - (angle1 + angle2)"),
    menu_trigonometrie,
])

menu_taux = Menu("Taux", [
    Action("Taux d'évolution", calc_taux_evolution, "(b-a)/a*100"),
    Action("Taux normal (composé)", calc_taux_global, "(1+var1)*(1+var2)-1"),
])

menu_maths = Menu("Maths", [
    menu_fonctions,
    menu_coordonnees,
    menu_theoremes,
    menu_vecteurs,
    menu_triangles,
    menu_taux,
])

# --- Physique ------------------------------------------------------------------
menu_masse_volumique = Menu("Masse volumique", [
    Action("Calculer p", calc_masse_volumique_rho),
    Action("Calculer m", calc_masse_volumique_m),
    Action("Calculer V", calc_masse_volumique_v),
], formule="p = m/V")

menu_dilution = Menu("Dilution", [
    Action("Calculer C2", calc_dilution_c2),
    Action("Calculer V2", calc_dilution_v2),
], formule="C1*V1 = C2*V2")

menu_matiere = Menu("Matière", [
    menu_masse_volumique,
    Action("Masse atome", calc_masse_atome, "m = (x*mp) + (y*mn) + (z*me)"),
    Action("Mol", calc_mol, "n = N / NA"),
    menu_dilution,
])

menu_ohm = Menu("Loi d'Ohm", [
    Action("Calculer U", calc_ohm_u),
    Action("Calculer R", calc_ohm_r),
    Action("Calculer I", calc_ohm_i),
], formule="U=RxI  R=U/I  I=U/R")

menu_puissance = Menu("Puissance électrique", [
    Action("P = U x I", calc_puissance_ui),
    Action("P = R x I**2", calc_puissance_ri2),
    Action("P = U**2 / R", calc_puissance_u2r),
], formule="P=UxI  P=RxI**2  P=U**2/R")

menu_electricite = Menu("Electricité", [
    menu_ohm,
    menu_puissance,
    Action("Energie électrique", calc_energie_electrique, "E = P x t"),
])

menu_indice_refraction = Menu("Indice de réfraction", [
    Action("Calculer n", calc_indice_refraction_n),
    Action("Calculer v", calc_indice_refraction_v),
], formule="n = c/v  ou  v = c/n")

menu_optique = Menu("Optique", [
    Action("Loi de Snell-Descartes", calc_snell_descartes, "n1*sin(i1) = n2*sin(i2)"),
    menu_indice_refraction,
])

menu_vitesse_moyenne = Menu("Vitesse moyenne", [
    Action("Calculer v", calc_vitesse),
    Action("Calculer d", calc_distance_temps),
    Action("Calculer t", calc_temps),
], formule="v=d/t  d=v*t  t=d/v")

menu_forces = Menu("Forces", [
    Action("Force de gravitation", calc_force_gravitation, "F = G*m1*m2 / d**2"),
    Action("Poids", calc_poids, "P = m x g"),
])

menu_physique = Menu("Physique", [
    menu_matiere,
    menu_electricite,
    menu_optique,
    menu_vitesse_moyenne,
    menu_forces,
])

# --- Racine ---------------------------------------------------------------------
menu_formules = Menu("Formules", recapitulatif=True)

ARBRE = Menu("Calculatrice", [menu_maths, menu_physique, menu_formules])


# ===========================================================================
# BOUCLE PRINCIPALE
# ===========================================================================
def run() -> None:
    executer_noeud(ARBRE)


def boucle_principale() -> None:
    while True:
        run()
        fin = saisir_entier("\nAvez-vous terminé ? \n1 (oui) / 0 (non): ", [0, 1])
        if fin == 1:
            if historique:
                print("\nHistorique des calculs :")
                for entree in historique:
                    print(entree)
            else:
                print("\nAucun calcul effectué.")
            print("Deconnexion...")
            sleep(2)
            print("Au revoir")
            break
        print()


if __name__ == "__main__":
    boucle_principale()