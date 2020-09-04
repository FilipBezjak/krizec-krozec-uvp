import os
import random
os.system("cls")
#tisti, ki igra je vedno X, računalnik pa O
igralec="X"
ZMAGOVALEC=None
Tezavnost = "Težko"
o=0
x=0
i=0


class Tabela():
    def __init__(self):
        self.kvadratki = ["-","-","-","-","-","-","-","-","-"]
        self.Tezavnost = Tezavnost

    def pokazi(self):
        #izpiše polje
        print(self.kvadratki[0] + " | "+self.kvadratki[1]+" | "+self.kvadratki[2])
        print(self.kvadratki[3] + " | "+self.kvadratki[4]+" | "+self.kvadratki[5])
        print(self.kvadratki[6] + " | "+self.kvadratki[7]+" | "+self.kvadratki[8])

    def update_tabelo(self, izbira, igralec):
        if igralec == "X":
            self.kvadratki[int(izbira)-1] = igralec
        else:
            self.kvadratki[int(izbira)] = igralec
        self.menjaj_igralca()

    def je_zmaga(self):
        global ZMAGOVALEC
        #poglej vrstice
        zmagovalec_vrstice = self.poglej_vrstice()
        #poglej stolpce
        zmagovalec_stolpci = self.poglej_stolpce()
        #poglej diagonale mora biti self. ker gledas matodo na objektu tabela
        zmagovalec_diagonale = self.poglej_diagonale()
        if zmagovalec_vrstice:
            ZMAGOVALEC = zmagovalec_vrstice
            return True
        elif zmagovalec_diagonale:
            ZMAGOVALEC = zmagovalec_diagonale
            return True
        elif zmagovalec_stolpci:
            ZMAGOVALEC = zmagovalec_stolpci
            return True
        else:
            ZMAGOVALEC = None
        return False


    def reset(self):
        self.kvadratki = ["-","-","-","-","-","-","-","-","-"]

    def poglej_stolpce(self):
        #poglej, ce imajo vse enako vrednost in  niso prazne
        prvi_stolpec = self.kvadratki[0] == self.kvadratki[3] == self.kvadratki[6] != "-"
        drugi_stolpec = self.kvadratki[1] == self.kvadratki[4] == self.kvadratki[7] != "-"
        tretji_stolpec = self.kvadratki[2] == self.kvadratki[5] == self.kvadratki[8] != "-"
        if prvi_stolpec or drugi_stolpec or tretji_stolpec:
            #pove ali je zmagovalec x ali 0
            if prvi_stolpec:
                return self.kvadratki[0]
            elif drugi_stolpec:
                return self.kvadratki[4]
            elif tretji_stolpec:
                return self.kvadratki[8]
            return

    def poglej_vrstice(self):
        #poglej, ce imajo vse enako vrednost in  niso prazne
        prva_vrstica = self.kvadratki[0] == self.kvadratki[1] == self.kvadratki[2] != "-"
        druga_vrstica = self.kvadratki[3] == self.kvadratki[4] == self.kvadratki[5] != "-"
        tretja_vrstica = self.kvadratki[6] == self.kvadratki[7] == self.kvadratki[8] != "-"
        if prva_vrstica or druga_vrstica or tretja_vrstica:
            #pove ali je zmagovalec x ali 0
            if prva_vrstica:
                return self.kvadratki[0]
            elif druga_vrstica:
                return self.kvadratki[4]
            elif tretja_vrstica:
                return self.kvadratki[8]
            return

    def poglej_diagonale(self):
        #poglej, ce imajo vse enako vrednost in  niso prazne
        prva_diagonala = self.kvadratki[0] == self.kvadratki[4] == self.kvadratki[8] != "-"
        druga_diagonala = self.kvadratki[6] == self.kvadratki[4] == self.kvadratki[2] != "-"
        if prva_diagonala or druga_diagonala:
                #pove ali je zmagovalec x ali 0
            if prva_diagonala:
                return self.kvadratki[0]
            elif druga_diagonala:
                return self.kvadratki[2]
            return

    def je_neodločeno(self):
        global ZMAGOVALEC
        if "-" not in self.kvadratki:
            ZMAGOVALEC = False
            return True

    def stevilo_moznosti_za_zmago_igralca(self):
        trojke = self.seznam_trojk()
        omogocijo = 0
        for trojka in trojke:
            if "X" in trojka and trojka.count("X") == 2 and "O" not in trojka:
        #preveri, ali sta na kaki diagonali, vrstici ali stolpcu 2 "X"-a in en "-",
                omogocijo += 1
        return omogocijo

# preveri, ali poteza igralcu omogoči zmago
    def omogoči_zmago(self, poteza):
        omogocijo1 = self.stevilo_moznosti_za_zmago_igralca()
        self.kvadratki[poteza]="O"
        omogocijo2 = self.stevilo_moznosti_za_zmago_igralca()
        if omogocijo1 == 0 or omogocijo1 > omogocijo2:
                return False
        else:
            self.kvadratki[poteza] = "-"
            return True


    def moznost_za_zmago(self):
        #pogleda, koliko moznost za zmago ima racunalnik v naslednji potezi,
        #da racunalnik izbere to polje in zmaga
        moznosti = []
        for a in self.izbira_poteze()[1]:
            self.kvadratki[a] = "O"
            if self.je_zmaga():
                moznosti.append(a)
            self.kvadratki[a] = "-"
        if len(moznosti) > 0:
            return moznosti
        else:
            return False

    def racunalnik_poteza(self):
        poteza, izbira = self.izbira_poteze()
        #pogleda, če naslednja poteza omogoči nasprotniku zmago
        while self.omogoči_zmago(poteza):
            if len(izbira) == 1:
                return izbira[0]
            izbira.remove(poteza)
            poteza=random.choice(izbira)
        self.update_tabelo(poteza, "O")

    def racunalnik_na_potezi(self):
        global igralec
        if igralec == "O":
            if self.Tezavnost == "Lahko":
                poteza = self.izbira_poteze()[0]
                self.update_tabelo(poteza, "O")
    #preveri ali lahko z naslednjo potezo zmaga
            elif self.moznost_za_zmago():
                self.update_tabelo(random.choice(self.moznost_za_zmago()), "O")
            elif self.stevilo_moznosti_za_zmago_igralca() > 0:
                self.racunalnik_poteza()
            elif self.Tezavnost == "Srednje":
                self.racunalnik_poteza()
            else:
                poteza = self.poteza()
                self.update_tabelo(poteza, "O")

    def izbira_poteze(self):
        izbira = [i for i in range(9) if self.kvadratki[i] == "-"]
        poteza = random.choice(izbira)
        return [poteza, izbira]


    def menjaj_igralca(self):
        global igralec
        #zamenja igralca
        if igralec == "O":
            igralec = "X"
        else:
            igralec = "O"

# preveri, ali je igre konec
    def konec(self):
        if self.je_zmaga():
            return True
        elif self.je_neodločeno():
            return True

# seznam vseh diagonal, stolpceh, vrstic
    def seznam_trojk(self):
        a = [self.kvadratki[0],self.kvadratki[1],self.kvadratki[2]]
        b = [self.kvadratki[3],self.kvadratki[4],self.kvadratki[5]]
        c = [self.kvadratki[6],self.kvadratki[7],self.kvadratki[8]]
        d = [self.kvadratki[0],self.kvadratki[3],self.kvadratki[6]]
        e = [self.kvadratki[1],self.kvadratki[4],self.kvadratki[7]]
        f = [self.kvadratki[2],self.kvadratki[5],self.kvadratki[8]]
        g = [self.kvadratki[0],self.kvadratki[4],self.kvadratki[8]]
        h = [self.kvadratki[6],self.kvadratki[4],self.kvadratki[2]]
        return [i for i in [a,b,c,d,e,f,g,h]]

# preveri, ali je igra enaka kateri izmed spodaj napisanih. Potem vrne najboljšo možno potezo
    def poteza(self):
        polje = self.kvadratki
        if "X" not in polje:
            return random.choice([0,2,6,8])
        elif "O" in polje and polje.count("O") == 1 and polje.index("X") == 4:
            return self.nasproti()
        elif "O" in polje and polje.count("O") == 1 and polje.index("X") in [1, 3, 5, 7]:
            return 4
        elif polje.count("O") == 2 and 4 in [i for i, x in enumerate(polje) if x == "O"] and polje.count("X") == 2 and enak_element([i for i, x in enumerate(polje) if x == "X"],[1, 3, 5, 7]):
            return self.napad_na_zmago(2)
        elif "O" not in polje:
            return random.choice([i for i in [4, self.nasproti()] if polje[i] != "X"])
        elif self.moznost_za_zmago():
            return self.moznost_za_zmago()[0]
        elif self.izbira_poteze()[1]:
            return self.napad_na_zmago(1)

#potezo postavi tako, da ima pri naslednji potezi n možnosti za zmago. Če je n enak 2, je zmaga zagotovljena
    def napad_na_zmago(self, n):
        if self.kvadratki.count("-") == 1 :
            return self.kvadratki.index("-")
        izbire = self.izbira_poteze()[1]
        random.shuffle(izbire)
        self.kvadratki[izbire[-1]] = "O"
        while self.moznost_za_zmago() != False and len(self.moznost_za_zmago()) < n:
            if len(izbire) > 1:
                self.kvadratki[izbire[-1]] = "-"
                izbire.pop()
                self.kvadratki[izbire[-1]] = "O"
            else:
                self.kvadratki[izbire[-1]] = "-"
                return izbire[0]
        self.kvadratki[izbire[-1]] = "-"
        return izbire[-1]

# da potezo v kot, ki je nasproti že zasedenega polja
    def nasproti(self):
        if self.kvadratki[0] != "-" :
            return 8
        elif self.kvadratki[2] != "-" :
            return 6
        elif self.kvadratki[6] != "-" :
            return 2
        elif self.kvadratki[8] != "-" :
            return 0

    
#preveri, ali imata 2 seznama vsaj en enak element
def enak_element(sez1, sez2):
    for x in sez1:
        for y in sez2:
            if x == y:
                return True
    return False
