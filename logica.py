# -*- coding: utf-8 -*-
"""
Vocabular:
Multimea variabilelor propozitionale: A, B, C, ... , Z
Conectori propozitionali: ¬ negatie, ∧ conjunctie, ∨ disjunctie
                          ⇒ implicatie, ⇔ echivalenta
Paranteze: ()
Echivalenta logica: ∼
"""

a = input("Introduceti un input: ") #salvarea inputului in lista a

def verif_propcompl(a): #verific daca o propozitie e corecta sau nu
    par = [] # par e o lista in care vor fi salvate pozitiile pe care se afla '(' in input
    i = 0
    
    while i < len(a): #parcurgem lista a
        if a[i] == '(': # daca gasim '(' adaugam pozitia acestui caracter in lista par
            par.append(i)
        '''elif a[i] == ' ': #stergem spatiile ( ' ' )
            a = a[:i] + a[(i + 1):] 
            i -= 1'''
        i += 1
    
    #print(a)
    
    if len(par) == 0: #verificam daca nu exista paranteze
        if (len(a) == 1):
            if a[0] >= 'A' and a[0] <= 'Z': # daca inputul este format doar dintr-o variabila propozitionala, lista a este o propozitie
                print("Este o formula propozitionala.")
            else: #daca nu, nu este o propozitie
                print("Nu este o formula propozitionala deoarece este formata dintr-un singur caracter si acesta nu este o variabila propozitionala.")
        else: #daca nu, nu este o propozitie
            print("Nu este o formula propozitionala deoarece este format din mai multe caractere, dar nu exista paranteze.")        
    else: # daca se ajunge aici inseamna ca exista cel putin o paranteza
        d = 0
        for i in range(len(par) - 1, -1, -1): #parcurgem lista par in sens invers (sfarsit - inceput)
            if(len(a) > (par[i] + 1)):
                if a[par[i] + 1] == '¬': #daca caracterul de dupa paranteza este negatia( '¬' ), propozitia poate fi corecta doar daca este urmata de catre o variabila propozitionala
                    if(len(a) > (par[i] + 2)):
                        if (a[par[i] + 2] >= 'A') and (a[par[i] + 2] <= 'Z'): #propozitia poate fi corecta doar daca dupa variabila propozitionala urmeaza o paranteza inchisa( ')' )
                            if(len(a) > (par[i] + 3)):
                                if a[par[i] + 3] == ')':
                                    a = a[:par[i]] + 'P' + a[(par[i] + 4):] #observam ca secventa este una de tip ( '(¬P)' ) si intrucat este corecta o inlocuim cu variabila propozitionala 'P' pentru a simplifica lista in care se afla inputul
                                    print(a)
                                else:
                                    print("Nu este o formula propozitionala deoarece dupa '(', negatie ( '¬' ) si dupa variabila propozitionala ", end="")
                                    print(a[par[i] + 2], end="")
                                    print(" nu urmeaza caracterul ')'.")
                                    d = 1
                                    break
                            else:
                                print("Nu este o formula propozitionala deoarece dupa '(', negatie ( '¬' ) si dupa variabila propozitionala ", end="")
                                print(a[par[i] + 2], end="")
                                print(" nu urmeaza alte caractere ( ar trebui sa urmeze ')' ).")
                                d = 1
                                break
                        else:
                            print("Nu este o formula propozitionala deoarece dupa '(' si negatie ( '¬' ) nu urmeaza o variabila propozitionala.")
                            d = 1
                            break
                    else:
                        print("Nu este o formula propozitionala deoarece dupa '(' si negatie( '¬' ) nu mai urmeaza alte caractere( ar trebui sa urmeze o variabila propozitionala si ')' ).")
                        d = 1
                        break
                elif (a[par[i] + 1] >= 'A') and (a[par[i] + 1] <= 'Z'): #verificam daca paranteza deschisa este urmata de catre o variabila propozitionala
                    if(len(a) > (par[i] + 2)):
                        if (a[par[i] + 2] == '∧') or (a[par[i] + 2] == '∨') or (a[par[i] + 2] == '⇒') or (a[par[i] + 2] == '⇔'): #propozitia poate fi corecta doar daca dupa variabila propozitionala urmeaza un conector propozitional exceptand negatie
                            if(len(a) > (par[i] + 3)):
                                if (a[par[i] + 3] >= 'A') and (a[par[i] + 3] <= 'Z'): #propozitia poate fi corecta doar daca urmeaza o variabila propozitionala
                                    if(len(a) > (par[i] + 4)):
                                        if a[par[i] + 4] == ')': #propozitia poate fi corecta doar daca urmeaza o paranteza inchisa ( ')' )
                                            a = a[:par[i]] + 'P' + a[(par[i] + 5):] #in lista a apare o secventa de tip ' (P∧R) '  si deoarece este corecta o inlocuim cu 'P' pentru a simplifica lista in care se afla inputul
                                            print(a)
                                        else:
                                            print("Nu este o formula propozitionala deoarece dupa '(', variabila propozitionala ", end="")
                                            print(a[par[i] + 1], end="")
                                            print(", conectorul propozitional ", end="")
                                            print(a[par[i] + 2], end="")
                                            print(" si variabila propozitionala ", end="")
                                            print(a[par[i] + 3], end="")
                                            print(" nu urmeaza ')'.")
                                            d = 1
                                            break
                                    else:
                                        print("Nu este o formula propozitionala deoarece dupa '(', variabila propozitionala ", end="")
                                        print(a[par[i] + 1], end="")
                                        print(", conectorul propozitional ", end="")
                                        print(a[par[i] + 2], end="")
                                        print(" si variabila propozitionala ", end="")
                                        print(a[par[i] + 3], end="")
                                        print(" nu mai exista alte caractere( ar trebui sa urmeze ')' ).")
                                        d = 1
                                        break
                                else:
                                    print("Nu este o formula propozitionala deoarece dupa '(', variabila propozitionala ", end="")
                                    print(a[par[i] + 1], end="")
                                    print(" si conectorul propozitional ", end="")
                                    print(a[par[i] + 2], end="")
                                    print(" nu urmeaza o variabila propozitionala.")
                                    d = 1
                                    break
                            else:
                                print("Nu este o formula propozitionala deoarece dupa '(', variabila propozitionala ", end="")
                                print(a[par[i] + 1], end="")
                                print(" si conectorul propozitional ", end="")
                                print(a[par[i] + 2], end="")
                                print(" nu mai urmeaza caractere( ar trebui sa urmeze variabila propozitionala si ')' ).")
                                d = 1
                                break
                        else:
                            print("Nu este o formula propozitionala deoarece dupa '(' si variabila propozitionala ", end="")
                            print(a[par[i] + 1], end="")
                            print(" nu urmeaza un conector propozitional(execeptand negatia).")
                            d = 1
                            break
                    else:
                        print("Nu este o formula propozitionala deoarece dupa '(' si variabila propozitionala ", end="")
                        print(a[par[i] + 1], end="")
                        print(" nu mai exista alte caractere ( ar trebui sa urmeze un conector propozitional care sa nu fie negatia, o variabila propozitionala si ')' ).")
                        d = 1
                        break
                else:
                    print("Nu este o formula propozitionala deoarece caracterul care urmeaza dupa '(' nu este nici negatie nici variabila propozitionala.")
                    d = 1
                    break
            else:
                print("Nu este o formula propozitionala deoarece dupa '(' nu mai exista caractere.")
                d = 1
                break
        if d == 0: # daca nu am afisat deja ca nu este o formula propozitionala 
            if (len(a) == 1):
                if a[0] >= 'A' and a[0] <= 'Z': # daca lista a cuprinde un singur element si anume o variabila propozitionala, inputul este o formula propozitionala
                    print("Este o formula propozitionala.")
                else: #daca nu, nu este o propozitie
                    print("Nu este o formula propozitionala deoarece este formata dintr-un singur caracter si acesta nu este o variabila propozitionala.")
            else: #daca nu, nu este o propozitie
                print("Nu este o formula propozitionala deoarece este format din mai multe caractere, dar nu exista paranteze.")        



def prop_relax(a):
    a1 = neg(a)
    '''if a1 != -1:
        a1 = semn(a1, '∧')
        if a1 != -1:
            a1 = semn(a1, '∨')
            if a1 != -1:
                a1 = semn(a1, '⇒')
                if a1 != -1:
                    a1 = semn(a1, '⇔')'''
    if a1 != -1:
        return a1
    else:
        return a

def semn(a, x):# verific daca semnele date au paranteze si daca nu, le adaug
    i = len(a) - 1
    while i >= 0:
        if(a[i] == x):
            d = 0
        i -= 1
    return a

def neg(a): # verific daca negatiile au paranteze si daca nu, le adaug
    i = 0
    while i < len(a):
        if(a[i] == '¬'): # daca gasim o negatie vrem sa verficam daca are paranteze sau daca nu sa le adaugam
            d = 0
            if i > 0: # verif daca are paranteza inainte, daca nu o adaug
                if a[i - 1] != '(':
                    a = a[:i] + '(' + a[i:]
                    i += 1
                else:
                    d = i
            else:
                a = '(' + a[:]
                i += 1
            e = 0
            if (i + 1) < len(a):
                if not((a[i + 1] >= 'A') and (a[i + 1] <= 'Z')):
                    if a[i + 1] == '¬':
                        k = 0
                        d1 = 0
                        for j in range(i + 2, len(a)):
                            if a[j] == '(':
                                k += 1
                                d1 = 1
                            elif a[j] == ')':
                                k -= 1
                            elif (a[j] >= 'A') and (a[j] <= 'Z'):
                                if k == 0:
                                    if d != 0:
                                        if (j + 1) < len(a):
                                            if a[j + 1] != ')':
                                                a = a[:(j + 1)] + ')' + a[(j + 1):]
                                                if d != 0:
                                                    a = a[:d] + '(' + a[d:]
                                                print(a)
                                                break
                                        else:
                                            a = a[:] + ')'
                                            if d != 0:
                                                a = a[:d] + '(' + a[d:]
                                            print(a)
                                            break
                                    else:
                                        if (j + 1) < len(a):
                                            a = a[:(j + 1)] + ')' + a[(j + 1):]
                                            if d != 0:
                                                a = a[:d] + '(' + a[d:]
                                            print(a)
                                        else:
                                            a = a[:(j + 1)] + ')'
                                            print(a)
                                        break
                                d1 = 1
                            if k == 0:
                                if d1 == 1:
                                    if d != 0:
                                        if (j + 1) < len(a):
                                            if a[j + 1] != ')':
                                                a = a[:(j + 1)] + ')' + a[(j + 1):]
                                                if d != 0:
                                                    a = a[:d] + '(' + a[d:]
                                                print(a)
                                                break
                                        else:
                                            a = a[:] + ')'
                                            if d != 0:
                                                a = a[:d] + '(' + a[d:]
                                            print(a)
                                            break
                                    else:
                                        if (j + 1) < len(a):
                                            a = a[:(j + 1)] + ')' + a[(j + 1):]
                                            if d != 0:
                                                a = a[:d] + '(' + a[d:]
                                            print(a)
                                        else:
                                            a = a[:(j + 1)] + ')'
                                            if d != 0:
                                                a = a[:d] + '(' + a[d:]
                                            print(a)
                                        break
                                    
                    elif a[i + 1] != '(':
                        print("Nu este formula propozitionala, deoarece dupa negatie urmeaza ", end="")
                        print(a[i + 1])
                        return -1
                    else:
                        k = 1
                        a1 = 0
                        for j in range(i + 2, len(a)):
                            if a[j] == '(':
                                k += 1
                            elif a[j] == ')':
                                k -= 1
                            if k == 0:
                                k = j
                                a1 = 1
                                break
                        if a1 == 0:
                            print("Nu este formula propozitionala, deoarece dupa negatie nu urmeaza un numar egal de '(' si ')'.")
                            return -1
                        else:
                            if (k + 1) < len(a):
                                if not(a[k + 1] == ')' and d != 0):
                                    a = a[:(k + 1)] + ')' + a[(k + 1):]
                                    if d != 0:
                                        a = a[:d] + '(' + a[d:]
                                    print(a)
                            else:
                                a = a[:] + ')'
                                if d != 0:
                                    a = a[:d] + '(' + a[d:]
                                print(a)
                        
                else: # daca negatia e urmata de o variabila propozitionala adaugam o paranteza dupa daca nu exista deja
                    if (i + 2) < len(a):
                        if a[i + 2] != ')':
                            a = a[:(i + 2)] + ')' + a[(i + 2):]
                            if d != 0:
                                a = a[:d] + '(' + a[d:]
                            print(a)
                        else:
                            if d == 0:
                                a = a[:(i + 2)] + ')' + a[(i + 2):]
                                if d != 0:
                                    a = a[:d] + '(' + a[d:]
                                print(a)
                    else:
                        a = a[:] + ')'
                        if d != 0:
                            a = a[:d] + '(' + a[d:]
                        print(a)
            else:
                print("Nu este formula propozitionala, deoarece sirul se termina cu caracterul negatie.")
                return -1
        i += 1
    return a


def sterg_spatii(a):
    i = 0
    while i < len(a): #parcurgem lista a
        if a[i] == ' ': #stergem spatiile ( ' ' )
            a = a[:i] + a[(i + 1):] 
            i -= 1
        i += 1
    return a

def verif_prop(a):
    a = sterg_spatii(a)
    a = prop_relax(a)
    #print(a)
    # verif_propcompl(a)
    
def tabeldeadv(a, valsat):
    par = [] # par e o lista in care vor fi salvate pozitiile pe care se afla '(' in input
    el = [] #lista in care o sa apara toate elementele care trebuie sa apara in tabel in afara de variabilele propozitionales
    el1 = [] #lista in care o sa apara toate elementele care trebuie sa apara in tabel in afara de variabilele propozitionales, dar buna de afisat
    i = 0
    s = set() #toate formulele propozitionale care apar
    valid = 1
    satisf = 0
    
    while i < len(a): #parcurgem lista a
        if a[i] == '(': # daca gasim '(' adaugam pozitia acestui caracter in lista par
            par.append(i)
        elif a[i] == ' ': #stergem spatiile ( ' ' )
            a = a[:i] + a[(i + 1):] 
            i -= 1
        elif (a[i] >='A') and (a[i] <= 'Z'): #facem un set care sa contina formulele propozitionale
            s.add(a[i])
        i += 1
    
    i = len(par) - 1
    k = 0 # index of last element added to el
    while i >= 0: 
        si = "(" # elementul care o sa fie adaugat la el
        si1 = "(" # elementul care o sa fie adaugat la el1
        k1 = 1
        k2 = 0
        d = 0
        nrpar = 1
        x = par[i] + 1
        if a[x] == '¬':
            d = 1
        while k1 > 0:
            k3 = k1
            if a[x] == '(':
                if k1 == 1:
                    if d == 1:
                        si = si[:] + "*" + str(k - nrpar) + "*"
                    else:
                        if k2 == 0:
                            si = si[:] + "*" + str(k - nrpar) + "*"
                        elif k2 == 1:
                            si = si[:] + "*" + str(k - nrpar) + "*"
                        k2 += 1
                k1 += 1
                nrpar += 1
            elif a[x] == ')':
                k1 -= 1
            if k1 == 1 and k1 == k3 and (a[x] >= 'A' and a[x] <= 'Z'):
                j = 0
                for d in s:
                    if a[x] == d:
                        si = si[:] + "%" + str(j) + "%"
                        break
                    j += 1
            elif k1 <= 1 and k1 == k3:
                si = si[:] + a[x]
            if k1 > 0:
                si1 = si1[:] + a[x]
            x += 1
        si = si[:] + ')'
        si1 = si1[:] + ')'
        el.append(si)
        el1.append(si1)
        k += 1
        i -= 1

    #print(el)
    for i in s:
        print(i, end="  ")
    for i in el1:
        print(i, end="  ")
    print()

    
    for i in range(0, 2 ** len(s)):
        vs = []
        vel = []
        bi = int(bin(i)[2:]) #generam toate variantele pt formulele propozitionale
        for j in range(0, len(s)):
            vs.append((bi // (10 ** (len(s) - 1 - j))) % 10)
        k = 0
        
        for j in s:
            if vs[k] == 0:
                print("F", end="  ")
            else:
                print("A", end="  ")
            k += 1
        
        def calcval(x):
            if x[1] == '¬':
                if x[2] == '*':
                    str1 = ""
                    i = 3
                    while x[i] != '*':
                        str1 = str1[:] + x[i]
                        i += 1
                    str1 = int(str1)
                    vel.append(not(vel[str1]))
                    return not(vel[str1])
                else:
                    str1 = ""
                    i = 3
                    while x[i] != '%':
                        str1 = str1[:] + x[i]
                        i += 1
                    str1 = int(str1)
                    vel.append(not(vs[str1]))
                    return not(vs[str1])
            elif x[1] == '*':
                str1 = ""
                i = 2
                while x[i] != '*':
                    str1 = str1[:] + x[i]
                    i += 1
                str1 = int(str1)
                i += 1
                semn = x[i]
                i += 1
                if x[i] == '*':
                    i += 1
                    str2 = ""
                    while x[i] != '*':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        h = (vel[str1] and vel[str2])
                        vel.append(h)
                        return h
                    elif semn == "∨":
                        h = (vel[str1] or vel[str2])
                        vel.append(h)
                        return h
                    elif semn == "⇒":
                        h = (not(vel[str1]) or vel[str2])
                        vel.append(h)
                        return h
                    else:
                        h = (vel[str1] == vel[str2])
                        vel.append(h)
                        return h
                else:
                    i += 1
                    str2 = ""
                    while x[i] != '%':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        vel.append(vel[str1] and vs[str2])
                        return (vel[str1] and vs[str2])
                    elif semn == "∨":
                        vel.append(vel[str1] or vs[str2])
                        return (vel[str1] or vs[str2])
                    elif semn == "⇒":
                        vel.append(not(vel[str1]) or vs[str2])
                        return (not(vel[str1]) or vs[str2])
                    else:
                        vel.append(vel[str1] == vs[str2])
                        print(vel[str1], end = " ")
                        print(vs[str2], end = " ")
                        return (vel[str1] == vs[str2])
            else: # %
                str1 = ""
                i = 2
                while x[i] != '%':
                    str1 = str1[:] + x[i]
                    i += 1
                str1 = int(str1)
                i += 1
                semn = x[i]
                i += 1
                if x[i] == '*':
                    i += 1
                    str2 = ""
                    while x[i] != '*':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        vel.append(vs[str1] and vel[str2])
                        return (vs[str1] and vel[str2])
                    elif semn == "∨":
                        vel.append(vs[str1] or vel[str2])
                        return (vs[str1] or vel[str2])
                    elif semn == "⇒":
                        vel.append(not(vs[str1]) or vel[str2])
                        return (not(vs[str1]) or vel[str2])
                    else:
                        vel.append(vs[str1] == vel[str2])
                        return (vs[str1] == vel[str2])
                else:
                    i += 1
                    str2 = ""
                    while x[i] != '%':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        vel.append(vs[str1] and vs[str2])
                        return (vs[str1] and vs[str2])
                    elif semn == "∨":
                        vel.append(vs[str1] or vs[str2])
                        return (vs[str1] or vs[str2])
                    elif semn == "⇒":
                        vel.append(not(vs[str1]) or vs[str2])
                        return (not(vs[str1]) or vs[str2])
                    else:
                        vel.append(vs[str1] == vs[str2])
                        return (vs[str1] == vs[str2])
        
        for j in el:
            if calcval(j) == 1:
                print("A", end="  ")
                for l in range(0, len(j)):
                    print(" ", end="")
            else:
                print("F", end="  ")
                for l in range(0, len(j)):
                    print(" ", end="")
        if vel[len(el) - 1] == 1:
            satisf = 1
        else:
            valid = 0
        print()
    if valsat != 0:
        if valid == 1:
            print(a, end=" ")
            print("este valida")
        else:
            print(a, end=" ")
            print("nu este valida")
        if satisf == 1:
            print(a, end=" ")
            print("este satisfiabila")
        else:
            print(a, end=" ")
            print("nu este satisfiabila")

def echiv_logica(a):
    d = -1
    for i in range(0, len(a)):
        if a[i] == '∼':
            d = i
    b = a[(d + 1):]
    a = a[:d]
    ech(a, b)
            

def ech(a, b):
    par = [] # par e o lista in care vor fi salvate pozitiile pe care se afla '(' in input
    parb = []
    el = [] #lista in care o sa apara toate elementele care trebuie sa apara in tabel in afara de variabilele propozitionales
    el1 = [] #lista in care o sa apara toate elementele care trebuie sa apara in tabel in afara de variabilele propozitionales, dar buna de afisat
    i = 0
    s = set() #toate formulele propozitionale care apar
    
    while i < len(a): #parcurgem lista a
        if a[i] == '(': # daca gasim '(' adaugam pozitia acestui caracter in lista par
            par.append(i)
        elif a[i] == ' ': #stergem spatiile ( ' ' )
            a = a[:i] + a[(i + 1):] 
            i -= 1
        elif (a[i] >='A') and (a[i] <= 'Z'): #facem un set care sa contina formulele propozitionale
            s.add(a[i])
        i += 1
    
    i = 0
    while i < len(b): #parcurgem lista a
        if b[i] == '(': # daca gasim '(' adaugam pozitia acestui caracter in lista par
            parb.append(i)
        elif b[i] == ' ': #stergem spatiile ( ' ' )
            b = b[:i] + b[(i + 1):] 
            i -= 1
        i += 1
    
    i = len(par) - 1
    k = 0 # index of last element added to el
    while i >= 0: 
        si = "(" # elementul care o sa fie adaugat la el
        si1 = "(" # elementul care o sa fie adaugat la el1
        k1 = 1
        k2 = 0
        d = 0
        nrpar = 1
        print(len(par))
        if len(par) >= 1:
            x = par[i] + 1
            if a[x] == '¬':
                d = 1
            while k1 > 0:
                k3 = k1
                if a[x] == '(':
                    if k1 == 1:
                        if d == 1:
                            si = si[:] + "*" + str(k - nrpar) + "*"
                        else:
                            if k2 == 0:
                                si = si[:] + "*" + str(k - nrpar) + "*"
                            elif k2 == 1:
                                si = si[:] + "*" + str(k - nrpar) + "*"
                            k2 += 1
                    k1 += 1
                    nrpar += 1
                elif a[x] == ')':
                    k1 -= 1
                if k1 == 1 and k1 == k3 and (a[x] >= 'A' and a[x] <= 'Z'):
                    j = 0
                    for d in s:
                        if a[x] == d:
                            si = si[:] + "%" + str(j) + "%"
                            break
                        j += 1
                elif k1 <= 1 and k1 == k3:
                    si = si[:] + a[x]
                if k1 > 0:
                    si1 = si1[:] + a[x]
                x += 1
            si = si[:] + ')'
            si1 = si1[:] + ')'
            el.append(si)
            el1.append(si1)
            k += 1
            i -= 1
    
    if len(parb) >= 1:
        i = len(parb) - 1
        while i >= 0: 
            si = "(" # elementul care o sa fie adaugat la el
            si1 = "(" # elementul care o sa fie adaugat la el1
            k1 = 1
            k2 = 0
            d = 0
            nrpar = 1
            x = parb[i] + 1
            if b[x] == '¬':
                d = 1
            while k1 > 0:
                k3 = k1
                if b[x] == '(':
                    if k1 == 1:
                        if d == 1:
                            si = si[:] + "*" + str(k - nrpar) + "*"
                        else:
                            if k2 == 0:
                                si = si[:] + "*" + str(k - nrpar) + "*"
                            elif k2 == 1:
                                si = si[:] + "*" + str(k - nrpar) + "*"
                            k2 += 1
                    k1 += 1
                    nrpar += 1
                elif b[x] == ')':
                    k1 -= 1
                if k1 == 1 and k1 == k3 and (b[x] >= 'A' and b[x] <= 'Z'):
                    j = 0
                    for d in s:
                        if b[x] == d:
                            si = si[:] + "%" + str(j) + "%"
                            break
                        j += 1
                elif k1 <= 1 and k1 == k3:
                    si = si[:] + b[x]
                if k1 > 0:
                    si1 = si1[:] + b[x]
                x += 1
            si = si[:] + ')'
            si1 = si1[:] + ')'
            el.append(si)
            el1.append(si1)
            k += 1
            i -= 1
    
    #print(el)
    for i in s:
        print(i, end="  ")
    for i in el1:
        print(i, end="  ")
    print()

    
    for i in range(0, 2 ** len(s)):
        vs = []
        vel = []
        bi = int(bin(i)[2:]) #generam toate variantele pt formulele propozitionale
        for j in range(0, len(s)):
            vs.append((bi // (10 ** (len(s) - 1 - j))) % 10)
        k = 0
        
        for j in s:
            if vs[k] == 0:
                print("F", end="  ")
            else:
                print("A", end="  ")
            k += 1
        
        def calcval(x): #calc daca x e adv sau fals
            if x[1] == '¬':
                if x[2] == '*':
                    str1 = ""
                    i = 3
                    while x[i] != '*':
                        str1 = str1[:] + x[i]
                        i += 1
                    str1 = int(str1)
                    vel.append(not(vel[str1]))
                    return not(vel[str1])
                else:
                    str1 = ""
                    i = 3
                    while x[i] != '%':
                        str1 = str1[:] + x[i]
                        i += 1
                    str1 = int(str1)
                    vel.append(not(vs[str1]))
                    return not(vs[str1])
            elif x[1] == '*':
                str1 = ""
                i = 2
                while x[i] != '*':
                    str1 = str1[:] + x[i]
                    i += 1
                str1 = int(str1)
                i += 1
                semn = x[i]
                i += 1
                if x[i] == '*':
                    i += 1
                    str2 = ""
                    while x[i] != '*':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        h = (vel[str1] and vel[str2])
                        vel.append(h)
                        return h
                    elif semn == "∨":
                        h = (vel[str1] or vel[str2])
                        vel.append(h)
                        return h
                    elif semn == "⇒":
                        h = (not(vel[str1]) or vel[str2])
                        vel.append(h)
                        return h
                    else:
                        h = (vel[str1] == vel[str2])
                        vel.append(h)
                        return h
                else:
                    i += 1
                    str2 = ""
                    while x[i] != '%':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        vel.append(vel[str1] and vs[str2])
                        return (vel[str1] and vs[str2])
                    elif semn == "∨":
                        vel.append(vel[str1] or vs[str2])
                        return (vel[str1] or vs[str2])
                    elif semn == "⇒":
                        vel.append(not(vel[str1]) or vs[str2])
                        return (not(vel[str1]) or vs[str2])
                    else:
                        vel.append(vel[str1] == vs[str2])
                        print(vel[str1], end = " ")
                        print(vs[str2], end = " ")
                        return (vel[str1] == vs[str2])
            else: # %
                str1 = ""
                i = 2
                while x[i] != '%':
                    str1 = str1[:] + x[i]
                    i += 1
                str1 = int(str1)
                i += 1
                semn = x[i]
                i += 1
                if x[i] == '*':
                    i += 1
                    str2 = ""
                    while x[i] != '*':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        vel.append(vs[str1] and vel[str2])
                        return (vs[str1] and vel[str2])
                    elif semn == "∨":
                        vel.append(vs[str1] or vel[str2])
                        return (vs[str1] or vel[str2])
                    elif semn == "⇒":
                        vel.append(not(vs[str1]) or vel[str2])
                        return (not(vs[str1]) or vel[str2])
                    else:
                        vel.append(vs[str1] == vel[str2])
                        return (vs[str1] == vel[str2])
                else:
                    i += 1
                    str2 = ""
                    while x[i] != '%':
                        str2 = str2[:] + x[i]
                        i += 1
                    str2 = int(str2)
                    if semn == "∧":
                        vel.append(vs[str1] and vs[str2])
                        return (vs[str1] and vs[str2])
                    elif semn == "∨":
                        vel.append(vs[str1] or vs[str2])
                        return (vs[str1] or vs[str2])
                    elif semn == "⇒":
                        vel.append(not(vs[str1]) or vs[str2])
                        return (not(vs[str1]) or vs[str2])
                    else:
                        vel.append(vs[str1] == vs[str2])
                        return (vs[str1] == vs[str2])
        
        for j in range(0, len(el)):
            if calcval(el[j]) == 1:
                print("A", end="  ")
                for l in range(0, len(el1[j])):
                    print(" ", end="")
            else:
                print("F", end="  ")
                for l in range(0, len(el1[j])):
                    print(" ", end="")
        print()
    v = "Linia pe care se afla {} are aceleasi valori ca si linia pe care se afla {} => echivalenta logica.".format(a, b)
    print(v)

echiv_logica(a)
#tabeldeadv(a, 1) # pt a afisa tabelul de adv pt o prop
#verif_prop(a) #pt a verif daca este o propozitie sau nu]
#verif_propcompl(a)
