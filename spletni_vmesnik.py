import bottle
import model
tabela=model.Tabela()

@bottle.get("/")
#zacetno stran naredimo v drugi datoteki
def zacetna_stran():
    return bottle.template("123/zacetna-tictac.tpl")

@bottle.get('/igra/')
def pokazi_igro():
    return bottle.template('123/zacetna-xoxo.tpl', pozicije = tabela.kvadratki, tabela=tabela, crka=1)

@bottle.post('/igra/')
def ugibaj():
    crka = bottle.request.forms.getunicode('crka')
    reset = bottle.request.forms.getunicode("reset")
    tezavnost = bottle.request.forms.getunicode("tezavnost")
    if tezavnost:
        tabela.Tezavnost = tezavnost
        tabela.reset()
        model.ZMAGOVALEC = None
    if reset == "O":
        model.ZMAGOVALEC = None
        model.igralec = "O"
        tabela.reset()
    elif reset == "X":
        model.ZMAGOVALEC = None
        model.igralec = "X"
        tabela.reset()
    elif reset == "igra":
        model.x = 0
        model.o = 0
        model.i = 0
    elif crka:
        if model.igralec == "X":
            tabela.update_tabelo(crka, model.igralec)
        if tabela.konec():
            bottle.redirect('/igra/')
        tabela.racunalnik_na_potezi()
        if tabela.konec():
            bottle.redirect('/igra/')
    else:
        tabela.racunalnik_na_potezi()
    bottle.redirect("/igra/")


bottle.run(debug=True, reloader=True)