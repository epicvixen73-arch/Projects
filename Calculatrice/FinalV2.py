from math import sqrt, pow, factorial, e, pi, cos, sin, tan, acos, asin, atan, radians, degrees
from time import*
matières=[0,"Maths","Physique","Formules"]
maths_H1=[0,"Fonctions","Coordonnées","Théorèmes","Vecteurs","Triangles","Taux"]
math_fn=[0,"Carrée","Cube","Inverse","Racine carrée","Valeur absolue","Factorielle","Exponentielle"]
math_fn_H1=[0,"De bases","Spécialées"]
math_co=[0,"Milieu","Distance"]
math_theo=[0,"Pythagore","Thalès"]
math_vc=[0,"Relation de Chasles","Déterminant"]
math_trgl=[0,"Somme angulaire","Trigonométrie"]
math_trigoH1=[0,"Trigo","Arc_Trigo"]
math_trigo=[0,"Cosinus","Sinus","Tangente"]
math_arc_trigo=[0,"ArcCosinus","ArcSinus","ArcTangente"]
math_taux=[0,"Taux d'évolution","Taux normal"]
pc_H1=[0,"Matière","Electricité","Optique","Vitesse moyenne","Forces"]
pc_mat=[0,"Masse Volumique","Masse atome","Mol",'Dilution']
pc_elec=[0,"Loi d'Ohm","Puissance électrique","Energie électrique"]
pc_opt=[0,"Loi de Snell Descartes","Indice de réfraction"]
pc_v=[0,"Calculer v","Calculer d","Calculer t"]
pc_forces=[0,"Force de gravitation","Poids"]
formules=[0,
    "Carrée         : x**2",                                                # 1
    "Cube           : x**3",                                                # 2
    "Inverse        : 1/x",                                                 # 3
    "Racine carrée  : sqrt(x)",                                             # 4
    "Valeur absolue : |x|",                                                 # 5
    "Factorielle    : n!",                                                  # 6
    "Exponentielle  : e**x",                                                # 7
    "Milieu         : ((x1+x2)/2 , (y1+y2)/2)",                             # 8
    "Distance       : sqrt((x2-x1)**2 + (y2-y1)**2)",                       # 9
    "Pythagore      : a**2 + b**2 = c**2",                                  # 10
    "Pytha Récip.   : c**2 = a**2 + b**2",                                  # 11
    "Thalès         : AD/AB = AE/AC",                                       # 12
    "Chasles        : AB + BC = AC",                                        # 13
    "Déterminant    : det(u;v) = x1*y2 - y1*x2",                            # 14
    "Somme angulaire: 180 - (angle1 + angle2)",                             # 15
    "Cosinus        : cos(angle)",                                          # 16
    "Sinus          : sin(angle)",                                          # 17
    "Tangente       : tan(angle)",                                          # 18
    "ArcCosinus     : arccos(x)",                                           # 19
    "ArcSinus       : arcsin(x)",                                           # 20
    "ArcTangente    : arctan(x)",                                           # 21
    "Masse Volumique: p = m/V",                                             # 22
    "Masse atome    : m = (x*mp) + (y*mn) + (z*me)",                        # 23
    "Mol            : n = N / NA",                                          # 24
    "Dilution       : C1*V1 = C2*V2",                                       # 25
    "Loi d'Ohm      : U=RxI  R=U/I  I=U/R",                                 # 26
    "Puissance élec.: P=UxI  P=RxI**2  P=U**2/R",                           # 27
    "Energie élec.  : E = P x t",                                           # 28
    "Snell-Descartes: n1*sin(i1) = n2*sin(i2)",                             # 29
    "Indice réfract.: n = c/v  ou  v = c/n",                                # 30
    "Vitesse moyenne: v=d/t  d=v*t  t=d/v",                                 # 31
    "Force gravit.  : F = G*m1*m2 / d**2",                                  # 32
    "Poids          : P = m x g",                                           # 33
    "Taux évol.    : (b-a)/a*100",                                          # 34
    "Taux normal    : (1+var1)*(1+var2)-1"                                  # 35
]
historique=[]
G=6.674e-11
NA=6.02e23
c=3e8
MP=1.673e-27
MN=1.675e-27
ME=9.110e-31
mproton=1.673e-27
mneutron=1.675e-27
melectron=9.110e-31
g=9.81
def arrondi(valeur):
    return round(valeur,4)
def saisir(message, valeurs_valide=None):
    while True:
        try:
            choix=int(input(message))
            if valeurs_valide is None or choix in valeurs_valide:
                return choix
            else:
                print(f"Invalide. \nnombre nécessaire entre {valeurs_valide}")
        except ValueError:
            print("Merci d'entrer un Nb valide. ")
def executer_formule(choix):
    """Exécute le calcul correspondant à la formule choisie par son index."""
    if choix == 1:  # Carrée
        x = float(input("x: "))
        res = arrondi(pow(x, 2))
        print(f"L'image de {x} est {res} par la fonction carrée.")
        historique.append(f"Carrée: {x}**2 = {res}")
    elif choix == 2:  # Cube
        x = float(input("x: "))
        res = arrondi(pow(x, 3))
        print(f"L'image de {x} est {res} par la fonction cube.")
        historique.append(f"Cube: {x}**3 = {res}")
    elif choix == 3:  # Inverse
        x = float(input("x: "))
        res = arrondi(1/x)
        print(f"L'image de {x} est {res} par la fonction inverse.")
        historique.append(f"Inverse: 1/{x} = {res}")
    elif choix == 4:  # Racine carrée
        x = float(input("x: "))
        res = arrondi(sqrt(x))
        print(f"L'image de {x} est {res} par la fonction racine carrée.")
        historique.append(f"Racine carrée: sqrt({x}) = {res}")
    elif choix == 5:  # Valeur absolue
        x = float(input("x: "))
        res = arrondi(sqrt(pow(x, 2)))
        print(f"L'image de {x} est {res} par la fonction valeur absolue.")
        historique.append(f"Valeur Absolue: |{x}| = {res}")
    elif choix == 6:  # Factorielle
        n = int(input("n: "))
        res = factorial(n)
        print(f"{n}! = {res}")
        historique.append(f"Factorielle: {n}! = {res}")
    elif choix == 7:  # Exponentielle
        x = float(input("x: "))
        res = arrondi(e**x)
        print(f"e**{x} = {res}")
        historique.append(f"Exponentielle: e**{x} = {res}")
    elif choix == 8:  # Milieu
        x1 = float(input("x1: "))
        x2 = float(input("x2: "))
        y1 = float(input("y1: "))
        y2 = float(input("y2: "))
        mx = arrondi((x1+x2)/2)
        my = arrondi((y1+y2)/2)
        print(f"Coordonnées du milieu: ({mx}, {my})")
        historique.append(f"Milieu: ({mx}, {my})")
    elif choix == 9:  # Distance
        x1 = float(input("x1: "))
        x2 = float(input("x2: "))
        y1 = float(input("y1: "))
        y2 = float(input("y2: "))
        res = arrondi(sqrt((x2-x1)**2 + (y2-y1)**2))
        print(f"Distance entre A et B: {res}")
        historique.append(f"Distance AB: {res}")
    elif choix == 10:  # Pythagore
        print("Le Théorème est: a²+b²=c²  (c est l'hypoténuse inconnu)")
        a = float(input("a: "))
        b = float(input("b: "))
        res = arrondi(sqrt(a**2 + b**2))
        print(f"c = {res}")
        historique.append(f"Pythagore: c = {res}")
    elif choix == 11:  # Réciproque/Contraposée Pythagore
        print("c²=a²+b²  (c = plus grand côté)")
        c = float(input("c: "))
        a = float(input("a: "))
        b = float(input("b: "))
        if round(c**2, 6) == round(a**2 + b**2, 6):
            print(f"Triangle rectangle (réciproque de Pythagore): {c}² = {a}² + {b}²")
            historique.append("Pytha récip: triangle rectangle")
        else:
            print(f"Triangle NON rectangle (contraposée de Pythagore): {c}² ≠ {a}² + {b}²")
            historique.append("Pytha contra: triangle non rectangle")
    elif choix == 12:  # Thalès
        print("AD/AB = AE/AC\n1: Chercher AE  2: Chercher AC\n3: Chercher AD  4: Chercher AB")
        c = saisir("Choix: ", [1,2,3,4])
        if c == 1:
            AB = float(input("AB: ")); AD = float(input("AD: ")); AC = float(input("AC: "))
            AE = arrondi((AD * AC) / AB)
            print(f"AE = {AE}")
            historique.append(f"Thalès: AE = {AE}")
        elif c == 2:
            AB = float(input("AB: ")); AD = float(input("AD: ")); AE = float(input("AE: "))
            AC = arrondi((AB * AE) / AD)
            print(f"AC = {AC}")
            historique.append(f"Thalès: AC = {AC}")
        elif c == 3:
            AB = float(input("AB: ")); AE = float(input("AE: ")); AC = float(input("AC: "))
            AD = arrondi((AB * AE) / AC)
            print(f"AD = {AD}")
            historique.append(f"Thalès: AD = {AD}")
        elif c == 4:
            AE = float(input("AE: ")); AD = float(input("AD: ")); AC = float(input("AC: "))
            AB = arrondi((AD * AC) / AE)
            print(f"AB = {AB}")
            historique.append(f"Thalès: AB = {AB}")
    elif choix == 13:  # Relation de Chasles
        print("1: Calculer AC\n2: Calculer AB\n3: Calculer BC")
        c = saisir("Choix: ", [1,2,3])
        if c == 1:
            AB = float(input("AB: ")); BC = float(input("BC: "))
            AC = arrondi(AB + BC)
            print(f"AC = {AC}")
            historique.append(f"Chasles: AC = {AC}")
        elif c == 2:
            AC = float(input("AC: ")); BC = float(input("BC: "))
            AB = arrondi(AC - BC)
            print(f"AB = {AB}")
            historique.append(f"Chasles: AB = {AB}")
        else:
            AC = float(input("AC: ")); AB = float(input("AB: "))
            BC = arrondi(AC - AB)
            print(f"BC = {BC}")
            historique.append(f"Chasles: BC = {BC}")
    elif choix == 14:  # Déterminant
        print("det(u;v) = x1*y2 - y1*x2")
        x1 = float(input("Abscisse de u: ")); y1 = float(input("Ordonnée de u: "))
        x2 = float(input("Abscisse de v: ")); y2 = float(input("Ordonnée de v: "))
        det = arrondi(x1*y2 - y1*x2)
        print(f"det(u;v) = ({x1}*{y2}) - ({y1}*{x2}) = {det}")
        historique.append(f"Déterminant: det(u;v) = {det}")
    elif choix == 15:  # Somme angulaire
        angle1 = float(input("angle 1 (°): "))
        angle2 = float(input("angle 2 (°): "))
        angle3 = arrondi(180 - (angle1 + angle2))
        print(f"Le 3ème angle est de: {angle3}°")
        historique.append(f"Somme angulaire: angle3 = {angle3}°")
    elif choix == 16:  # Cosinus
        x = float(input("angle (°): "))
        res = arrondi(cos(radians(x)))
        print(f"cos({x}°) = {res}")
        historique.append(f"Cosinus: cos({x}°) = {res}")
    elif choix == 17:  # Sinus
        x = float(input("angle (°): "))
        res = arrondi(sin(radians(x)))
        print(f"sin({x}°) = {res}")
        historique.append(f"Sinus: sin({x}°) = {res}")
    elif choix == 18:  # Tangente
        x = float(input("angle (°): "))
        res = arrondi(tan(radians(x)))
        print(f"tan({x}°) = {res}")
        historique.append(f"Tangente: tan({x}°) = {res}")
    elif choix == 19:  # ArcCosinus
        x = float(input("x (entre -1 et 1): "))
        res = arrondi(degrees(acos(x)))
        print(f"arccos({x}) = {res}°")
        historique.append(f"ArcCosinus: arccos({x}) = {res}°")
    elif choix == 20:  # ArcSinus
        x = float(input("x (entre -1 et 1): "))
        res = arrondi(degrees(asin(x)))
        print(f"arcsin({x}) = {res}°")
        historique.append(f"ArcSinus: arcsin({x}) = {res}°")
    elif choix == 21:  # ArcTangente
        x = float(input("x: "))
        res = arrondi(degrees(atan(x)))
        print(f"arctan({x}) = {res}°")
        historique.append(f"ArcTangente: arctan({x}) = {res}°")
    elif choix == 22:  # Masse Volumique
        print("1: Calculer p\n2: Calculer m\n3: Calculer V")
        c = saisir("Choix: ", [1,2,3])
        if c == 1:
            m = float(input("m (kg): ")); V = float(input("V (m³): "))
            rho = arrondi(m/V)
            print(f"p = {rho} kg/m³")
            historique.append(f"Masse Volumique: p = {rho} kg/m³")
        elif c == 2:
            rho = float(input("p (kg/m³): ")); V = float(input("V (m³): "))
            m = arrondi(rho*V)
            print(f"m = {m} kg")
            historique.append(f"Masse Volumique: m = {m} kg")
        else:
            m = float(input("m (kg): ")); rho = float(input("p (kg/m³): "))
            V = arrondi(m/rho)
            print(f"V = {V} m³")
            historique.append(f"Masse Volumique: V = {V} m³")
    elif choix == 23:  # Masse atome
        x = int(input("Nb de protons: "))
        y = int(input("Nb de neutrons: "))
        z = int(input("Nb d'électrons: "))
        mproton = 1.673e-27; mneutron = 1.675e-27; melectron = 9.110e-31
        m = (x*mproton) + (y*mneutron) + (z*melectron)
        print(f"Masse de l'atome: {m:.3e} kg")
        historique.append(f"Masse atome: {m:.3e} kg")
    elif choix == 24:  # Mol
        NA = 6.02e23
        n_entites = float(input("Nombre d'entités: "))
        n_moles = n_entites / NA
        print(f"Nombre de moles: {n_moles:.4e} mol")
        historique.append(f"Mol: {n_moles:.4e} mol")
    elif choix == 25:  # Dilution
        print("1: Calculer C2\n2: Calculer V2")
        c = saisir("Choix: ", [1,2])
        C1 = float(input("C1 (mol/L): ")); V1 = float(input("V1 (L): "))
        if c == 1:
            V2 = float(input("V2 (L): "))
            C2 = arrondi((C1*V1)/V2)
            print(f"C2 = {C2} mol/L")
            historique.append(f"Dilution: C2 = {C2} mol/L")
        else:
            C2 = float(input("C2 (mol/L): "))
            V2 = arrondi((C1*V1)/C2)
            print(f"V2 = {V2} L")
            historique.append(f"Dilution: V2 = {V2} L")
    elif choix == 26:  # Loi d'Ohm
        print("Calculer: 1=U  2=R  3=I")
        c = saisir("Choix: ", [1,2,3])
        if c == 1:
            R = float(input("R (Ω): ")); I = float(input("I (A): "))
            U = arrondi(R*I)
            print(f"U = {U} V")
            historique.append(f"Ohm: U = {U} V")
        elif c == 2:
            U = float(input("U (V): ")); I = float(input("I (A): "))
            R = arrondi(U/I)
            print(f"R = {R} Ω")
            historique.append(f"Ohm: R = {R} Ω")
        else:
            U = float(input("U (V): ")); R = float(input("R (Ω): "))
            I = arrondi(U/R)
            print(f"I = {I} A")
            historique.append(f"Ohm: I = {I} A")
    elif choix == 27:  # Puissance électrique
        print("1: P = UxI\n2: P = RxI²\n3: P = U²/R")
        c = saisir("Choix: ", [1,2,3])
        if c == 1:
            U = float(input("U (V): ")); I = float(input("I (A): "))
            P = arrondi(U*I)
        elif c == 2:
            R = float(input("R (Ω): ")); I = float(input("I (A): "))
            P = arrondi(R*I**2)
        else:
            U = float(input("U (V): ")); R = float(input("R (Ω): "))
            P = arrondi(U**2/R)
        print(f"P = {P} W")
        historique.append(f"Puissance: P = {P} W")
    elif choix == 28:  # Energie électrique
        P = float(input("P (W): ")); t = float(input("t (s): "))
        E = arrondi(P*t)
        print(f"E = {E} J  |  E = {E/3600:.2f} Wh")
        historique.append(f"Energie: E = {E} J ({E/3600:.2f} Wh)")
    elif choix == 29:  # Snell-Descartes
        n1 = float(input("n1: ")); n2 = float(input("n2: ")); i1 = float(input("i1 (°): "))
        sin_i2 = n1 * sin(radians(i1)) / n2
        if sin_i2 > 1:
            print("Réflexion totale")
            historique.append("Snell-Descartes: réflexion totale")
        else:
            i2 = arrondi(degrees(asin(sin_i2)))
            print(f"i2 = {i2}°")
            historique.append(f"Snell-Descartes: i2 = {i2}°")
    elif choix == 30:  # Indice de réfraction
        print("Calculer: 1=n  2=v")
        c_choix = saisir("Choix: ", [1,2])
        c = 3e8
        if c_choix == 1:
            v = float(input("v (m/s): "))
            n = arrondi(c/v)
            print(f"n = {n}")
            historique.append(f"Indice réfraction: n = {n}")
        else:
            n = float(input("n: "))
            v = c/n
            print(f"v = {v:.2e} m/s")
            historique.append(f"Indice réfraction: v = {v:.2e} m/s")
    elif choix == 31:  # Vitesse moyenne
        print("Calculer: 1=v  2=d  3=t")
        c = saisir("Choix: ", [1,2,3])
        if c == 1:
            d = float(input("d (m): ")); t = float(input("t (s): "))
            v = arrondi(d/t)
            print(f"v = {v} m/s")
            historique.append(f"Vitesse moyenne: v = {v} m/s")
        elif c == 2:
            v = float(input("v (m/s): ")); t = float(input("t (s): "))
            d = arrondi(v*t)
            print(f"d = {d} m")
            historique.append(f"Vitesse moyenne: d = {d} m")
        else:
            d = float(input("d (m): ")); v = float(input("v (m/s): "))
            t = arrondi(d/v)
            print(f"t = {t} s")
            historique.append(f"Vitesse moyenne: t = {t} s")
    elif choix == 32:  # Force de gravitation
        G = 6.674e-11
        m1 = float(input("m1 (kg): ")); m2 = float(input("m2 (kg): ")); d = float(input("d (m): "))
        F = arrondi(G*m1*m2/d**2)
        print(f"F = {F:.2e} N")
        historique.append(f"Force de gravitation: F = {F:.2e} N")
    elif choix == 33:  # Poids
        m = float(input("m (kg): "))
        g = 9.81
        P = arrondi(m*g)
        print(f"P = {P} N")
        historique.append(f"Poids: P = {P} N")
    elif choix == 34:  # Taux d'évolution
        a = float(input("Valeur de départ: "))
        b = float(input("Valeur d'arrivée: "))
        if a == 0:
            print("Erreur: valeur de départ ne peut pas être 0.")
        else:
            taux = arrondi((b - a) / a * 100)
            print(f"Taux d'évolution: {taux:.2f} %")
            historique.append(f"Taux évol.: {taux:.2f} %")
    elif choix == 35:  # Taux normal
        a = float(input("Variation 1(%): "))
        b = float(input("Variation 2(%): "))
        var1, var2 = a / 100, b / 100
        taux = arrondi(((1 + var1) * (1 + var2) - 1) * 100)
        print(f"Taux global: {taux:.2f} %")
        historique.append(f"Taux global: {taux:.2f} %")
def run():
    global historique
    print(f"1: {matières[1]}, 2: {matières[2]}, 3: {matières[3]}")
    choix=saisir("Choix: ", [1,2,3])
    # Maths
    if matières[choix]=="Maths":
        print(f"1: {maths_H1[1]}, 2: {maths_H1[2]} \n3: {maths_H1[3]}, 4: {maths_H1[4]} \n5: {maths_H1[5]}, 6: {maths_H1[6]}")
        choix=saisir("Choix: ", [1,2,3,4,5,6])
        if maths_H1[choix]=="Fonctions": #Fonctions
            print(f"1: {math_fn_H1[1]}, 2: {math_fn_H1[2]}")
            choix=saisir("Choix: ", [1,2])
            if math_fn_H1[choix]=="De bases":
                print(f"1: {math_fn[1]}, 2: {math_fn[2]} \n3: {math_fn[3]}, 4: {math_fn[4]} \n5: {math_fn[5]}")
                choix=saisir("Choix: ", [1,2,3,4,5])
                if math_fn[choix]=="Carrée":
                    # carrée
                    x=float(input("x: "))
                    calcul2=arrondi(pow(x, 2))
                    print(f"L'image de {x} est {calcul2} par la fonction carrée.")
                    historique.append(f"Carrée: {x}**2 = {calcul2}")
                elif math_fn[choix]=="Cube":
                    # cube
                    x=float(input("x: "))
                    calcul3=arrondi(pow(x, 3))
                    print(f"L'image de {x} est {calcul3} par la fonction cube.")
                    historique.append(f"Cube: {x}**3 = {calcul3}")
                elif math_fn[choix]=="Inverse":
                    # inverse
                    x=float(input("x: "))
                    calcul4=arrondi(1/x)
                    print(f"L'image de {x}, est {calcul4} par la fonction inverse.")
                    historique.append(f"Inverse: 1/{x} = {calcul4}")
                elif math_fn[choix]=="Racine carrée":
                    # racine carrée
                    x=float(input("x: "))
                    calcul5=arrondi(sqrt(x))
                    print(f"L'image de {x} est {calcul5} par la fonction racine carrée.")
                    historique.append(f"Racine carrée: {x} = {calcul5}")
                elif math_fn[choix]=="Valeur absolue":
                    # valeur absolue
                    x=float(input("x: "))
                    calcul6=arrondi(sqrt(pow(x, 2)))
                    print(f"L'image de {x} est {calcul6} par la fonction valeur absolue.")
                    historique.append(f"Valeur Absolue: {x} = {calcul6}")
            elif math_fn_H1[choix]=="Spécialées":
                print(f"6: {math_fn[6]} \n7: {math_fn[7]}")
                choix=saisir("Choix: ", [6,7])
                if math_fn[choix]=="Factorielle":
                    # factorielle
                    n=int(input("n: "))
                    result_facto=factorial(n)
                    print(f"{n}! = {result_facto}")
                    historique.append(f"Factorielle: {n}! = {result_facto}")
                elif math_fn[choix]=="Exponentielle":
                    x=float(input("x: "))
                    expo=arrondi(e**x)
                    print(f"e**{x} = {expo}")
                    historique.append(f"Exponentielle: e**{x} = {expo}")
        elif maths_H1[choix]=="Coordonnées": #Coordonnées
            print(f"1: {math_co[1]}, 2: {math_co[2]}")
            choix, x1, y1, x2, y2=saisir("Operation: ", [1,2]), float(input("x1: ")), float(input("y1: ")), float(input("x2: ")), float(input("y2: "))
            if math_co[choix]=="Milieu":
                # Milieu
                calculx, calculy=arrondi((x1+x2)/2), arrondi((y1+y2)/2)
                print("Coordonnées du milieu:", calculx, calculy)
                historique.append(f"Milieu: ({calculx}, {calculy})")
            else:
                # Distance
                calculd=arrondi(sqrt(((x2-x1)**2)+((y2-y1)**2)))
                print(f"Distance entre A et B:, {calculd}")
                historique.append(f"Distance AB: {calculd}")
        elif maths_H1[choix]=="Théorèmes": #Théorèmes
            print(f"1: {math_theo[1]}, 2: {math_theo[2]}")
            choix=saisir("Choix: ", [1,2])
            if math_theo[choix]=="Pythagore":
                print("1: Théorème \n2: Réciproque/Contraposée")
                choix=saisir("Choix: ", [1,2])
                if choix==1:
                    print("Le Théorème est: a^2+b^2=c^2 \nAvec c qui est inconnu")
                    a, b=float(input("a: ")), float(input("b: "))
                    P_théo=arrondi(sqrt(a**2+b**2))
                    print(f"La longueur de c par {a} et {b} est de {P_théo}")
                    historique.append(f"Pythagore: c = {P_théo}")
                elif choix==2:
                    print("La Réciproque du théo de P est: \nc^2=a^2+b^2 \nAvec c le plus grand coté: ")
                    c, a, b=float(input("c: ")), float(input("a: ")), float(input("b: "))
                    P_réci1, P_réci2=c**2, a**2+b**2
                    if round(c**2, 6)==round(a**2+b**2, 6):
                        print(f"Le triangle est bien rectangle car: \nd'après la réciproque de Pythagore; \n{c}^2 est bien égal à {a}^2 + {b}^2")
                        historique.append(f"Pytha récip: triangle rectangle")
                    else:
                        print(f"Le triangle n'est pas rectangle car \nd'après la contraposée de Pythagore; \n{c}^2 n'est pas égal à {a}^2 + {b}^2")
                        historique.append(f"Pytha contra: triangle non rectangle")
            elif math_theo[choix]=="Thalès":
                print("Dans un triangle AD/AB = AE/AC; \nChercher AE \n1: Chercher AE, 2: Chercher AC \n3: Chercher AD, 4: Chercher AB")
                choix=saisir("Choix: ", [1,2,3,4])
                if choix==1:
                    AB, AD, AC=float(input("AB: ")), float(input("AD: ")), float(input("AC: "))
                    AE = arrondi((AD * AC) / AB)
                    print(f"AE={AE}")
                    historique.append(f"Thalès: AE = {AE}")
                elif choix==2:
                    AB, AD, AE=float(input("AB: ")), float(input("AD: ")), float(input("AE: "))
                    AC = arrondi((AB * AE) / AD)
                    print(f"AC={AC}")
                    historique.append(f"Thalès: AC = {AC}")
                elif choix==3:
                    AB, AE, AC=float(input("AB: ")), float(input("AE: ")), float(input("AC: "))
                    AD = arrondi((AB * AE) / AC)
                    print(f"AD={AD}")
                    historique.append(f"Thalès: AD = {AD}")
                elif choix==4:
                    AE, AD, AC=float(input("AE: ")), float(input("AD: ")), float(input("AC: "))
                    AB = arrondi((AD * AC) / AE)
                    print(f"AB={AB}")
                    historique.append(f"Thalès: AB = {AB}")
        elif maths_H1[choix]=="Vecteurs": #Vecteurs
            print(f"1: {math_vc[1]} \n2: {math_vc[2]}")
            choix=saisir("Choix: ", [1,2])
            if math_vc[choix]=="Relation de Chasles":
                print("1: Calculer AC")
                print("2: Calculer AB")
                print("3: Calculer BC")
                choix=saisir("Choix: ", [1,2,3])
                if choix==1:
                    AB, BC=float(input("AB: ")), float(input("BC: "))
                    AC=arrondi(AB + BC)
                    print(f"AC = {AC}")
                    historique.append(f"Chasles: AC = {AC}")
                elif choix==2:
                    AC, BC=float(input("AC: ")), float(input("BC: "))
                    AB=arrondi(AC - BC)
                    print(f"AB = {AB}")
                    historique.append(f"Chasles: AB = {AB}")
                else:
                    AC, AB=float(input("AC: ")), float(input("AB: "))
                    BC=arrondi(AC - AB)
                    print(f"BC = {BC}")
                    historique.append(f"Chasles: BC = {BC}")
            elif math_vc[choix]=="Déterminant":
                print("Le det(u;v)")
                x1, y1, x2, y2 = float(input("Abscisse de u: ")), float(input("Ordonnée de u: ")), float(input("Abscisse de v: ")), float(input("Ordonnée de v: "))
                calc1, calc2=x1*y2, y1*x2
                determinant=arrondi(calc1-calc2)
                print(f"det(u;v)= \n({x1}*{y2})-({y1}*{x2}) \n=({calc1})-({calc2}) \n={determinant}")
                historique.append(f"Déterminant: det(u;v) = {determinant}")
        elif maths_H1[choix]=="Triangles": #Triangles
            print(f"1: {math_trgl[1]}, 2: {math_trgl[2]}")
            choix=saisir("Choix: ", [1,2])
            if math_trgl[choix]=="Somme angulaire":
                angle1, angle2=float(input("angle 1: ")), float(input("angle 2: "))
                angle3=arrondi(180-(angle1+angle2))
                print(f"Le 3eme angle est de: {angle3}")
                historique.append(f"Somme angulaire: angle3 = {angle3} degré")
            elif math_trgl[choix]=="Trigonométrie":
                print(f"1: {math_trigoH1[1]}, 2: {math_trigoH1[2]}")
                choix=saisir("Choix: ", [1,2])
                if math_trigoH1[choix]=="Trigo":
                    print(f"1: {math_trigo[1]}, 2: {math_trigo[2]} \n3: {math_trigo[3]}")
                    choix=saisir("Choix: ", [1,2,3])
                    if math_trigo[choix]=="Cosinus":
                        x=float(input("x: "))
                        cos_x=arrondi(cos(radians(x)))
                        print(f"cos({x}) = {cos_x}")
                        historique.append(f"Cosinus: cos({x}) = {cos_x}")
                    elif math_trigo[choix]=="Sinus":
                        x=float(input("x: "))
                        sin_x=arrondi(sin(radians(x)))
                        print(f"sin({x}) = {sin_x}")
                        historique.append(f"Sinus: sin({x}) = {sin_x}")
                    elif math_trigo[choix]=="Tangente":
                        x=float(input("x: "))
                        tan_x=arrondi(tan(radians(x)))
                        print(f"tan({x}) = {tan_x}")
                        historique.append(f"Tangente: tan({x}) = {tan_x}")
                elif math_trigoH1[choix]=="Arc_Trigo":
                    print(f"1: {math_arc_trigo[1]}, 2: {math_arc_trigo[2]} \n3: {math_arc_trigo[3]}")
                    choix=saisir("Choix: ", [1,2,3])
                    if math_arc_trigo[choix]=="ArcCosinus":
                        x=float(input("x: "))
                        arccos_x=arrondi(degrees(acos(x)))
                        print(f"arccos({x}) = {arccos_x}")
                        historique.append(f"ArcCosinus: arccos({x}) = {arccos_x}")
                    elif math_arc_trigo[choix]=="ArcSinus":
                        x=float(input("x: "))
                        arcsin_x=arrondi(degrees(asin(x)))
                        print(f"arcsin({x}) = {arcsin_x}")
                        historique.append(f"ArcSinus: arcsin({x}) = {arcsin_x}")
                    elif math_arc_trigo[choix]=="ArcTangente":
                        x=float(input("x: "))
                        arctan_x=arrondi(degrees(atan(x)))
                        print(f"arctan({x}) = {arctan_x}")
                        historique.append(f"ArcTangente: arctan({x}) = {arctan_x}")
        elif maths_H1[choix]=="Taux":
                    print(f"1: {math_taux[1]} \n2: {math_taux[2]}")
                    choix=saisir("Choix: ", [1,2])
                    if math_taux[choix]=="Taux d'évolution":
                        a=float(input("Valeur de départ: "))
                        b=float(input("Valeur d'arrivée: "))
                        if a==0:
                            print("Erreur: valeur de départ ne peut pas être 0.")
                        else:
                            taux=arrondi((b-a)/a*100)
                            print(f"Taux d'évolution: {taux:.2f} %")
                            historique.append(f"Taux évol.: {taux:.2f} %")
                    elif math_taux[choix]=="Taux normal":
                        a=float(input("Variation 1(%): "))
                        b=float(input("Variation 2(%): "))
                        var1, var2=a/100, b/100
                        taux=arrondi(((1+var1)*(1+var2)-1)*100)
                        print(f"Taux global: {taux:.2f} %")
                        historique.append(f"Taux global: {taux:.2f} %")
    elif matières[choix]=="Physique":
        print(f"1: {pc_H1[1]}, 3: {pc_H1[3]} \n2: {pc_H1[2]}, 4: {pc_H1[4]} \n5: {pc_H1[5]}")
        choix=saisir("Choix: ", [1,2,3,4,5])
        if pc_H1[choix]=="Matière": #Matière
            print(f"1: {pc_mat[1]}, 3: {pc_mat[3]} \n2: {pc_mat[2]}, 4: {pc_mat[4]}")
            choix=saisir("Choix: ", [1,2,3,4])
            if pc_mat[choix]=="Masse Volumique":
                print("1: Calculer p \n2: Calculer m \n3: Calculer V")
                choix_calc=saisir("Choix: ", [1,2,3])
                if choix_calc==1:
                    m, V=float(input("m (kg): ")), float(input("V (m³): "))
                    rho=arrondi(m/V)
                    print(f"p= {rho} kg/m³")
                    historique.append(f"Masse Volumique: p = {rho} kg/m**3")
                elif choix_calc==2:
                    rho, V=float(input("p (kg/m³): ")), float(input("V (m³): "))
                    m=arrondi(rho*V)
                    print(f"m= {m} kg")
                    historique.append(f"Masse Volumique: m = {m} kg")
                else:
                    m, rho=float(input("m (kg): ")), float(input("p (kg/m³): "))
                    V=arrondi(m/rho)
                    print(f"V = {V} m³")
                    historique.append(f"Masse Volumique: V = {V} m**3")
            elif pc_mat[choix]=="Masse atome":
                x, y, z=int(input("Nb de protons: ")), int(input("Nb de neutrons: ")), int(input("Nb d'électrons: "))
                m = (x * mproton) + (y * mneutron) + (z * melectron)
                print(f"Masse de l'atome : {m:.3e} kg")
                historique.append(f"Masse atome: {m:.3e} kg")
            elif pc_mat[choix]=="Mol":
                n_entites=float(input("Nombre d'entités: "))
                n_moles=arrondi(n_entites/NA)
                print(f"Nombre de moles: {n_moles:.4e} mol")
                historique.append(f"Mol: {n_moles:.4e} mol")
            elif pc_mat[choix]=="Dilution":
                print("1: Calculer C2  \n2: Calculer V2 ")
                choix=saisir("Choix: ", [1,2])  
                C1=float(input("C1 (mol/L): "))
                V1=float(input("V1 (L): "))
                if choix==1:
                    V2=float(input("V2 (L): "))
                    C2=arrondi((C1*V1)/V2)
                    print(f"C2= {C2} mol/L")
                    historique.append(f"Dilution: C2 = {C2} mol/L")
                else:
                    C2=float(input("C2 (mol/L): "))
                    V2=arrondi((C1*V1)/C2)
                    print(f"V2 = {V2} L")
                    historique.append(f"Dilution: V2 = {V2} L")
        elif pc_H1[choix]=="Electricité": #Electricité
            print(f"1: {pc_elec[1]}, 2: {pc_elec[2]} \n3: {pc_elec[3]}")
            choix=saisir("Choix: ", [1,2,3])
            if pc_elec[choix]=="Loi d'Ohm":
                print("Calculer: 1=U, 2=R, 3=I")
                choix=saisir("Choix: ", [1,2,3])
                if choix==1:
                    R, I=float(input("R (Ω): ")), float(input("I (A): "))
                    U=arrondi(R*I)
                    print(f"U= {U} V")
                    historique.append(f"Ohm: U = {U} V")
                elif choix==2:
                    U, I=float(input("U (V): ")), float(input("I (A): "))
                    R=arrondi(U/I)
                    print(f"R= {R} Ω")
                    historique.append(f"Ohm: R = {R} Ω")
                else:
                    U, R=float(input("U (V): ")), float(input("R (Ω): "))
                    I=arrondi(U/R)
                    print(f"I= {I} A")
                    historique.append(f"Ohm: I = {I} A")
            elif pc_elec[choix]=="Puissance électrique":
                print("1: P= UxI \n2: P= RxI**2 \n3: P= U**2/R")
                choix=saisir("Choix: ", [1,2,3])
                if choix==1:
                    U, I=float(input("U (V): ")), float(input("I (A): "))
                    P=arrondi(U*I)
                    print(f"P= {P} W")
                    historique.append(f"Puissance: P = {P} W")
                elif choix==2:
                    R, I = float(input("R (Ω): ")), float(input("I (A): "))
                    P=arrondi(R*I**2)
                    print(f"P= {P} W")
                    historique.append(f"Puissance: P = {P} W")
                else:
                    U, R=float(input("U (V): ")), float(input("R (Ω): "))
                    P=arrondi(U**2/R)
                    print(f"P= {P} W")
                    historique.append(f"Puissance: P = {P} W")
            elif pc_elec[choix]=="Energie électrique":
                P, t=float(input("P (W): ")), float(input("t (s): "))
                E=arrondi(P*t)
                print(f"E= {E} J \nE= {E/3600:.2f} Wh")
                historique.append(f"Energie: E = {E} J ({E/3600:.2f} Wh)")
        elif pc_H1[choix]=="Optique": #Optique
            print(f"1: {pc_opt[1]} \n2: {pc_opt[2]}")
            choix=saisir("Choix: ", [1,2])
            if pc_opt[choix]=="Loi de Snell Descartes":
                n1, n2, i1=float(input("n1: ")), float(input("n2: ")), float(input("i1 (°): "))
                sin_i2=n1*sin(radians(i1))/n2
                if sin_i2>1:
                    print("Réflexion totale")
                    historique.append("Snell_Descartes: réflexion totale")
                else:
                    i2=degrees(asin(sin_i2))
                    print(f"i2 = {i2:.2f}°")
                    historique.append(f"Snell-Descartes: i2 = {i2:.2f}°")
            elif pc_opt[choix]=="Indice de réfraction":
                print(" Calculer: 1=n, 2=v")
                choix=saisir("Choix: ", [1,2])
                if choix==1:
                    v=float(input("v (m/s): "))
                    n=c/v
                    print(f"n= {n:.2f}")
                    historique.append(f"Indice réfraction: n = {n:.2f}")
                else:
                    n=float(input("n: "))
                    v=c/n
                    print(f"v= {v:.2e} m/s")
                    historique.append(f"Indice réfraction: v = {v:.2e} m/s")
        elif pc_H1[choix]=="Vitesse moyenne": #Vitesse Moyenne
            print("Calculer: 1=v, 2=d, 3=t")
            choix=saisir("Choix: ", [1,2,3])
            if choix==1:
                d, t=float(input("d (m): ")), float(input("t (s): "))
                v=arrondi(d/t)
                print(f"v= {v} m/s")
                historique.append(f"Vitesse moyenne: v = {v} m/s")
            elif choix==2:
                v, t=float(input("v (m/s): ")), float(input("t (s): "))
                d=arrondi(v*t)
                print(f"d= {d} m")
                historique.append(f"Vitesse moyenne: d = {d} m")
            else:
                d, v=float(input("d (m): ")), float(input("v (m/s): "))
                t=arrondi(d/v)
                print(f"t= {t} s")
                historique.append(f"Vitesse moyenne: t = {t} s")
        elif pc_H1[choix]=="Forces":
            print(f"1: {pc_forces[1]} \n2: {pc_forces[2]}")
            choix=saisir("Choix: ", [1,2])
            if pc_forces[choix]=="Force de gravitation":
                m1, m2, d =float(input("m1 (kg): ")), float(input("m2 (kg): ")), float(input("d (m): "))
                F=arrondi(G*m1*m2/d**2)
                print(f"F= {F:.2e} N")
                historique.append(f"Force de gravitation: F = {F:.2e} N")
            elif pc_forces[choix]=="Poids":
                m=float(input("m (kg): "))
                P=arrondi(m*g)
                print(f"P= {P} N")
                historique.append(f"Poids: P= {P} N")
    elif matières[choix]=="Formules":
        print("\nFormules disponibles:")
        for i in range(1, len(formules)):
            print(f"  {i:2}: {formules[i]}")
        choix = saisir("Choix: ", list(range(1, len(formules))))
        print(f"\n>>> {formules[choix]}")
        executer_formule(choix)
while True:
    run()
    continuer=saisir("\nAvez vous terminé ? \n1(oui) / 0(non): ", [0,1])
    if continuer==1:
        if historique:
            print("\nHistorique des calculs: ")
            for entry in historique:
                print(entry)
        else:
            print("\nAucun calcul effectué.")
        print("Deconnexion...")
        sleep(2)
        print("Au revoir")
        break
    print()