import model

tabela = model.Tabela()

def zacetek():
    print("Igrate proti računalniku, vi ste igralec X.")

def konec():
    tabela.konec()
    if model.ZMAGOVALEC == False:
        izpis_neodločeno()
    elif model.ZMAGOVALEC == "X" or model.ZMAGOVALEC == "O" :
        izpis_zmage()
        tabela.pokazi()
    if not model.ZMAGOVALEC == None:
        nova_igra()

def zahtevaj_vnos():
    return input("Na potezi je {}\n Izberi kvadratek 1-9, ki še ni bil izbran: ".format(model.igralec))

def preveri_izbiro(poteza):
    #prvo preveri, ali je poteza število
    if je_stevilo(poteza):
        #ga zmanjša za 1, zaradi pythonovega načina štetja
        poteza = int(poteza)-1
        #preveri, ali je med 1 in 9 in, ali je to mesto prosto
        if  0<=poteza<=8:
            if tabela.kvadratki[poteza] == "-":
                return True
            else:
                print("Kvadratek " + str(poteza+1) + " ni na voljo.")
                tabela.pokazi()
                return False
        else:
            print(str(poteza + 1) + " ni število med 1 in 9.")
            tabela.pokazi()
            return False
    else:
        print(str(poteza) + " ni število.")
        tabela.pokazi()
        return False

def izpis_zmage():
    if model.ZMAGOVALEC == "O":
        print("Žal vas je računalnik premagal.")
    else:
        print("Zmagali ste, čestitam")
    tabela.pokazi()

def izpis_neodločeno():
    print("Neodločeno.")

#ko končamo, nam da možnost da ponovno začnemo
def nova_igra():
    global tabela
    dane = input("Bi igrali novo igro? Napišite DA ali NE: ")
    if dane == "DA" or dane == "Da" or dane == "da":
        tabela.reset()
        igraj()

def igraj():
    zacetek()
    while True:
        tabela.pokazi()
        #preveri, ali je igra končana
        #če je na potezi računalnik, se izvede računalnik_na potezi
        #če ne pa zahteva vnos
        if model.igralec == "X":
            izbira = zahtevaj_vnos()
        #preveri, ali je vnos stevilo med 1 in 9
            while not preveri_izbiro(izbira):
                izbira=zahtevaj_vnos()
            tabela.update_tabelo(izbira, model.igralec)
        konec()
        tabela.racunalnik_na_potezi()
        konec()

#preveri, ali smo vnesli stevilo
def je_stevilo(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
igraj()

