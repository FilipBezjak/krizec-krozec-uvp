<!DOCTYPE HTML>
<html lang="sl">
    <head style="align:center; margin:auto;">
        <title>xoxo</title>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css"/>
    </head>
    <body>
   <style> 
    td{
        height: 169.6px;
        width: 120px;
        border:5px solid white;
        padding: -10px;
        border-radius: 20px;
    }
    body {
        font-family:tahoma ;
        margin:auto;
        align:center;
        text-align: center;
        }
    table {
        font-size: 30pt;
        margin:auto;
        align:center;
        border: none;
        border-radius:40px;
        background-color: aquamarine;
        }
    button{
        color:aquamarine;
        border:none;
    }
    #teza{
        background-color:aquamarine;
        border:none;
        color: white;
        border-radius: 25px;
        height: 70px;
        width:230px;
        font-size: 45px;
        margin: 15px;
    }

</style>
%import model
%if model.ZMAGOVALEC == None:
        <section class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Križec-krožec
            </h1>
            <h2 class="subtitle">
              Igrate proti računalniku, vi ste igralec X
            </h2>
            <h2 class = "subtitle">
%if model.igralec == "X":
Ste na vrsti. Kliknite na polje.
%else:
<form action="/igra/" method="post">
        Na vrsti je računalnik. Pritisnite gumb, da se igra <button style="border-radius: 10px;height: 30px; color: black; background-color: aquamarine"name = "crka" value = "1" type = "submit">začne.</button>
</form>
%end
            </h2>
          </div>
        </div>
      </section>
%elif model.ZMAGOVALEC == "O":
<section class="hero is-danger">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Križec-krožec
            </h1>
            <h2 class="subtitle">
              Igrate proti računalniku, vi ste igralec X
            </h2>
            <h2 class = "subtitle">
                Žal ste izgubili
            </h2>
          </div>
        </div>
      </section>
%elif model.ZMAGOVALEC == "X":
<section class="hero is-success">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Križec-krožec
            </h1>
            <h2 class="subtitle">
              Igrate proti računalniku, vi ste igralec X.
            </h2>
            <h2 class = "subtitle">
                Čestitam, premagali ste računalnik.
            </h2>
          </div>
        </div>
      </section>
      %elif model.ZMAGOVALEC == False:
      <section class="hero is-info">
              <div class="hero-body">
                <div class="container">
                  <h1 class="title">
                    Križec-krožec
                  </h1>
                  <h2 class="subtitle">
                    Igrate proti računalniku, vi ste igralec X.
                  </h2>
                  <h2 class = "subtitle">
                      Izenačeno
                  </h2>
                </div>
              </div>
        </section>
%end
<body>
        <div class="columns">
        <div class="column">
                <form action="/igra/" method="post">
                        <p>
                                <button class="button is-large"  style="border-radius: 40px; margin: 15px;white-space: normal; height:100.2px;width:180px;background-color:aquamarine "name = "reset" value = "O" type = "submit">Nova igra <br/>Začne  O </button>
                                <button class="button is-large"  style="border-radius: 40px; margin: 15px;white-space: normal; height:100.2px;width:180px;background-color:aquamarine "name = "reset" value = "X" type = "submit">Nova igra <br/> Začne X</button>
                        </p>
                        <p>
                                <form action="/igra0/" method="post">
                                <button style="background-color:rgb(117, 212, 243)" id=teza name="tezavnost" value="Lahko" type="submit">Lahko</button>
                                </form>
                        </p>
                        <p>
                              <form action="/igra/" method="post">
                                <button style="background-color:rgb(236, 236, 145)" id=teza name="tezavnost" value="Srednje" type="submit">Srednje</button>
                              </form>
                      </p>
                      <p>
                                <form action="/igra/" method="post">
                                <button style="background-color:rgb(253, 133, 133)" id=teza name="tezavnost" value="Težko" type="submit">Težko</button>
                                </form>
                        </p>
                </form>
        </div>
        <div class="column is-two-fifts">
        <table >
        <tr>
              <td> 
        % if pozicije[0]=="X":
                <p style="font-size:110px;  float:center">X</p>
        %elif pozicije[0]=="O":
        <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="1">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        %end
             </td>
             <td>
        % if pozicije[1]=="X":
                <p style="font-size:110px; float:center">X</p>
        %elif pozicije[1]=="O":
                <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="2">klikni</button>
                </form>
        %else:
        
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        %end
        </td>
        <td>
        % if pozicije[2]=="X":
        <p style="font-size:110px; float:center">X</p>
        %elif pozicije[2]=="O":
        <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="3">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        %end
        </td>
        </tr>
        <tr>
                <td>
        % if pozicije[3]=="X":
                        <p style="font-size:110px; float:center">X</p>
        %elif pozicije[3]=="O":
                        <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                  <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="4">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        
        %end
              </td>
              <td>
                      % if pozicije[4]=="X":
                <p style="font-size:110px; float:center">X</p>
                %elif pozicije[4]=="O":
                <p style="font-size:110px; float:center">O</p>
                %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                  <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="5">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        %end
              </td>
              <td>
        % if pozicije[5]=="X":
        <p style="font-size:110px; float:center">X</p>
        %elif pozicije[5]=="O":
                <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="6">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        %end
        </td>
            </tr>
            <tr>
                    <td>
        % if pozicije[6]=="X":
        <p style="font-size:110px; float:center">X</p>
        %elif pozicije[6]=="O":
        <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="7">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        
        %end
        </td>
              <td>
        % if pozicije[7]=="X":
        <p style="font-size:110px; float:center">X</p>
        %elif pozicije[7]=="O":
        <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="8">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        
        %end
        </td>
        <td>
        % if pozicije[8]=="X":
        <p style="font-size:110px; float:center">X</p>
        %elif pozicije[8]=="O":
                <p style="font-size:110px; float:center">O</p>
        %elif model.ZMAGOVALEC == None:
                <form action="/igra/" method="post">
                        <button style="height:169.2px;width:115px;background-color:aquamarine" name="crka" type="submit" value="9">klikni</button>
                </form>
        %else:
                <button style="height:169.2px;width:115px;background-color:aquamarine">klikni</button>
        %end
        </td>
            </tr>
        </table>
        </div>
        <div class="column">
                <p>
                        <big><big><big><big><big><big>X  :   O</big></big></big></big></big></big>
                </p>
                <p>
                <big><big><big>{{model.x}}  :  {{model.o}}</big></big></big>
                </p>
                <p>
                        %if model.ZMAGOVALEC=="X":
                        %model.x += 1
                        %elif model.ZMAGOVALEC=="O":
                        %model.o += 1
                        %elif model.ZMAGOVALEC == False:
                        %model.i += 1
                        %end
                        %end
                </p>
                <p>
                <form action="/igra/" method="post">
                        <button style="color: black"name = "reset" value = "igra" type = "submit">Resetiraj igre</button>
                </form>
                </p>
                <p>
                        %c=model.i + model.x + model.o
                        %x = model.x/(c+1)
                        %o = model.o/(c+1)
                        %i = model.i/(c + 1)
                        <div class="container is-fullhd">
                                <div class="notification">
                                  Zmage <strong>X</strong>
                                </div>
                        </div>
                        <progress class="progress is-large is-success" value="{{model.x}}" max="{{c}}">100%</progress>
                        <div class="container is-fullhd">
                                <div class="notification">
                                  Zmage <strong>O</strong>
                                </div>
                        </div>
                        <progress class="progress is-large is-danger" value="{{model.o}}" max="{{c}}">30%</progress>
                        <div class="container is-fullhd">
                                <div class="notification">
                                 <strong>Izenačeno</strong>
                                </div>
                        </div>
                        <progress class="progress is-large is-info" value="{{model.i}}" max="{{c}}">45%</progress>
                </p>
        </div>
        <div class="column is-1">
        </div>
        </body>
        </html>