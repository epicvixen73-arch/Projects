from math import sqrt,factorial,e,cos,sin,tan,acos,asin,atan,radians,degrees
G=6.674e-11;NA=6.02e23;C=3e8;MP=1.673e-27;MN=1.675e-27;ME=9.110e-31;g=9.81
hist=[]
def r4(v):return round(v,4)
def fi(m):return float(input(m))
def ii(m):return int(input(m))
def saisir(msg,v):
    while True:
        try:
            n=int(input(msg))
            if n in v:return n
            print("Invalide")
        except:print("Entier SVP")
MAX_HIST=5
def histo(s):
    hist.append(s)
    if len(hist)>MAX_HIST:hist.pop(0)
    restant=MAX_HIST-len(hist)
    print("[Histo: "+str(len(hist))+"/"+str(MAX_HIST)+" | "+str(restant)+" libre(s)]")
def calc(c):
    if c==1:
        x=fi("x: ");r=r4(x**2);print(r);histo("x^2="+str(r))
    elif c==2:
        x=fi("x: ");r=r4(x**3);print(r);histo("x^3="+str(r))
    elif c==3:
        x=fi("x: ");r=r4(1/x);print(r);histo("1/x="+str(r))
    elif c==4:
        x=fi("x: ");r=r4(sqrt(x));print(r);histo("sqrt="+str(r))
    elif c==5:
        x=fi("x: ");r=r4(abs(x));print(r);histo("|x|="+str(r))
    elif c==6:
        n=ii("n: ");r=factorial(n);print(r);histo(str(n)+"!="+str(r))
    elif c==7:
        x=fi("x: ");r=r4(e**x);print(r);histo("e^x="+str(r))
    elif c==8:
        x1=fi("x1: ");x2=fi("x2: ");y1=fi("y1: ");y2=fi("y2: ")
        mx=r4((x1+x2)/2);my=r4((y1+y2)/2)
        print("("+str(mx)+","+str(my)+")")
        histo("M=("+str(mx)+","+str(my)+")")
    elif c==9:
        x1=fi("x1: ");x2=fi("x2: ");y1=fi("y1: ");y2=fi("y2: ")
        r=r4(sqrt((x2-x1)**2+(y2-y1)**2));print(r);histo("d="+str(r))
    elif c==10:
        a=fi("a: ");b=fi("b: ");r=r4(sqrt(a**2+b**2))
        print("c="+str(r));histo("Pytha c="+str(r))
    elif c==11:
        cv=fi("c: ");a=fi("a: ");b=fi("b: ")
        if round(cv**2,6)==round(a**2+b**2,6):
            print("Rectangle");histo("Rect: oui")
        else:
            print("Non rect.");histo("Rect: non")
    elif c==12:
        print("1:AE 2:AC 3:AD 4:AB")
        t=saisir("? ",(1,2,3,4))
        if t==1:
            AB=fi("AB: ");AD=fi("AD: ");AC=fi("AC: ")
            r=r4(AD*AC/AB);print("AE="+str(r));histo("Thales AE="+str(r))
        elif t==2:
            AB=fi("AB: ");AD=fi("AD: ");AE=fi("AE: ")
            r=r4(AB*AE/AD);print("AC="+str(r));histo("Thales AC="+str(r))
        elif t==3:
            AB=fi("AB: ");AE=fi("AE: ");AC=fi("AC: ")
            r=r4(AB*AE/AC);print("AD="+str(r));histo("Thales AD="+str(r))
        else:
            AE=fi("AE: ");AD=fi("AD: ");AC=fi("AC: ")
            r=r4(AD*AC/AE);print("AB="+str(r));histo("Thales AB="+str(r))
    elif c==13:
        print("1:AC 2:AB 3:BC")
        t=saisir("? ",(1,2,3))
        if t==1:
            r=r4(fi("AB: ")+fi("BC: "));print("AC="+str(r));histo("Chasles AC="+str(r))
        elif t==2:
            r=r4(fi("AC: ")-fi("BC: "));print("AB="+str(r));histo("Chasles AB="+str(r))
        else:
            r=r4(fi("AC: ")-fi("AB: "));print("BC="+str(r));histo("Chasles BC="+str(r))
    elif c==14:
        x1=fi("u_x: ");y1=fi("u_y: ");x2=fi("v_x: ");y2=fi("v_y: ")
        r=r4(x1*y2-y1*x2);print("det="+str(r));histo("det="+str(r))
    elif c==15:
        a1=fi("a1(deg): ");a2=fi("a2(deg): ")
        r=r4(180-(a1+a2));print("a3="+str(r)+"deg");histo("a3="+str(r))
    elif c==16:
        x=fi("angle(deg): ");r=r4(cos(radians(x)));print(r);histo("cos="+str(r))
    elif c==17:
        x=fi("angle(deg): ");r=r4(sin(radians(x)));print(r);histo("sin="+str(r))
    elif c==18:
        x=fi("angle(deg): ");r=r4(tan(radians(x)));print(r);histo("tan="+str(r))
    elif c==19:
        x=fi("x[-1;1]: ");r=r4(degrees(acos(x)));print(str(r)+"deg");histo("acos="+str(r))
    elif c==20:
        x=fi("x[-1;1]: ");r=r4(degrees(asin(x)));print(str(r)+"deg");histo("asin="+str(r))
    elif c==21:
        x=fi("x: ");r=r4(degrees(atan(x)));print(str(r)+"deg");histo("atan="+str(r))
    elif c==22:
        print("1:p 2:m 3:V")
        t=saisir("? ",(1,2,3))
        if t==1:
            r=r4(fi("m(kg): ")/fi("V(m3): "));print("p="+str(r)+"kg/m3");histo("p="+str(r))
        elif t==2:
            r=r4(fi("p(kg/m3): ")*fi("V(m3): "));print("m="+str(r)+"kg");histo("m="+str(r))
        else:
            r=r4(fi("m(kg): ")/fi("p(kg/m3): "));print("V="+str(r)+"m3");histo("V="+str(r))
    elif c==23:
        x=ii("protons: ");y=ii("neutrons: ");z=ii("electrons: ")
        m=x*MP+y*MN+z*ME;s="%.3e"%m;print("m="+s+"kg");histo("atome="+s)
    elif c==24:
        N=fi("entites: ");n=N/NA;s="%.4e"%n;print("n="+s+"mol");histo("mol="+s)
    elif c==25:
        print("1:C2 2:V2")
        t=saisir("? ",(1,2))
        C1=fi("C1(mol/L): ");V1=fi("V1(L): ")
        if t==1:
            r=r4(C1*V1/fi("V2(L): "));print("C2="+str(r));histo("C2="+str(r))
        else:
            r=r4(C1*V1/fi("C2(mol/L): "));print("V2="+str(r));histo("V2="+str(r))
    elif c==26:
        print("1:U 2:R 3:I")
        t=saisir("? ",(1,2,3))
        if t==1:
            r=r4(fi("R(ohm): ")*fi("I(A): "));print("U="+str(r)+"V");histo("U="+str(r))
        elif t==2:
            r=r4(fi("U(V): ")/fi("I(A): "));print("R="+str(r)+"ohm");histo("R="+str(r))
        else:
            r=r4(fi("U(V): ")/fi("R(ohm): "));print("I="+str(r)+"A");histo("I="+str(r))
    elif c==27:
        print("1:UxI 2:RxI2 3:U2/R")
        t=saisir("? ",(1,2,3))
        if t==1:P=r4(fi("U(V): ")*fi("I(A): "))
        elif t==2:P=r4(fi("R(ohm): ")*fi("I(A): ")**2)
        else:P=r4(fi("U(V): ")**2/fi("R(ohm): "))
        print("P="+str(P)+"W");histo("P="+str(P))
    elif c==28:
        P=fi("P(W): ");t=fi("t(s): ");E=r4(P*t)
        print("E="+str(E)+"J / "+str(round(E/3600,2))+"Wh");histo("E="+str(E))
    elif c==29:
        n1=fi("n1: ");n2=fi("n2: ");i1=fi("i1(deg): ")
        s=n1*sin(radians(i1))/n2
        if s>1:print("Refl. totale");histo("Snell:refl")
        else:r=r4(degrees(asin(s)));print("i2="+str(r)+"deg");histo("i2="+str(r))
    elif c==30:
        print("1:n 2:v")
        t=saisir("? ",(1,2))
        if t==1:
            r=r4(C/fi("v(m/s): "));print("n="+str(r));histo("n="+str(r))
        else:
            v=C/fi("n: ");s="%.2e"%v;print("v="+s+"m/s");histo("v="+s)
    elif c==31:
        print("1:v 2:d 3:t")
        t=saisir("? ",(1,2,3))
        if t==1:
            r=r4(fi("d(m): ")/fi("t(s): "));print("v="+str(r)+"m/s");histo("v="+str(r))
        elif t==2:
            r=r4(fi("v(m/s): ")*fi("t(s): "));print("d="+str(r)+"m");histo("d="+str(r))
        else:
            r=r4(fi("d(m): ")/fi("v(m/s): "));print("t="+str(r)+"s");histo("t="+str(r))
    elif c==32:
        m1=fi("m1(kg): ");m2=fi("m2(kg): ");d=fi("d(m): ")
        F=G*m1*m2/d**2;s="%.2e"%F;print("F="+s+"N");histo("F="+s)
    elif c==33:
        r=r4(fi("m(kg): ")*g);print("P="+str(r)+"N");histo("P="+str(r))
    elif c==34:
        a=fi("Depart: ");b=fi("Arrivee: ")
        if a==0:print("Err:depart=0")
        else:
            r=r4((b-a)/a*100);print(str(r)+"%");histo("TauxEvol="+str(r)+"%")
    elif c==35:
        a=fi("Var1(%): ");b=fi("Var2(%): ")
        r=r4(((1+a/100)*(1+b/100)-1)*100);print(str(r)+"%");histo("TauxNorm="+str(r)+"%")
def run():
    print("1:Maths\n2:Physique")
    m=saisir("? ",(1,2))
    if m==1:
        print("1:Fonctions\n2:Coords\n3:Theoremes\n4:Vecteurs\n5:Triangles\n6:Taux")
        s=saisir("? ",(1,2,3,4,5,6))
        if s==1:
            print("1:Carree 2:Cube\n3:Inverse 4:Racine\n5:ValAbs 6:Facto\n7:Expo")
            calc(saisir("? ",(1,2,3,4,5,6,7)))
        elif s==2:
            print("1:Milieu\n2:Distance")
            calc(saisir("? ",(1,2))+7)
        elif s==3:
            print("1:Pythagore\n2:Thales")
            t=saisir("? ",(1,2))
            if t==1:
                print("1:Theoreme\n2:Reciproque")
                calc(saisir("? ",(1,2))+9)
            else:calc(12)
        elif s==4:
            print("1:Chasles\n2:Determinant")
            calc(saisir("? ",(1,2))+12)
        elif s==5:
            print("1:Somme ang.\n2:Trigo")
            t=saisir("? ",(1,2))
            if t==1:calc(15)
            else:
                print("1:cos/sin/tan\n2:acos/asin/atan")
                t=saisir("? ",(1,2))
                if t==1:
                    print("1:cos 2:sin 3:tan")
                    calc(saisir("? ",(1,2,3))+15)
                else:
                    print("1:acos 2:asin 3:atan")
                    calc(saisir("? ",(1,2,3))+18)
        elif s==6:
            print("1:Taux evol\n2:Taux norm")
            calc(saisir("? ",(1,2))+33)
    else:
        print("1:Matiere\n2:Electricite\n3:Optique\n4:Vitesse\n5:Forces")
        s=saisir("? ",(1,2,3,4,5))
        if s==1:
            print("1:MasseVol\n2:Atome\n3:Mol\n4:Dilution")
            calc(saisir("? ",(1,2,3,4))+21)
        elif s==2:
            print("1:Ohm\n2:Puissance\n3:Energie")
            calc(saisir("? ",(1,2,3))+25)
        elif s==3:
            print("1:Snell\n2:Indice")
            calc(saisir("? ",(1,2))+28)
        elif s==4:calc(31)
        else:
            print("1:Gravitation\n2:Poids")
            calc(saisir("? ",(1,2))+31)
while True:
    run()
    if saisir("Fin? 1=oui 0=non: ",(0,1))==1:
        if hist:
            print("-- Historique --")
            for h in hist:print(h)
        break
    print()
