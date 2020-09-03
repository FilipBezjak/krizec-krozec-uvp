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
        background-color:aquamarine;
        border:none;
        color: white;
        border-radius: 25px;
        height: 110px;
        width:300px;
        font-size: 70px;
        margin: 30px;
    }

 </style>
<body>
<h1>Igra križec-krožec</h1>
<h2>Projekt pri predmetu UVP</h2>

<img src="https://miro.medium.com/max/1000/1*mIjIjWIUc45MQjLDVkOC-w.png" alt="slika" width=100px/>
<p>
  <form action="/igra/" method="post">
    <button name="tezavnost" value="Lahko" type="submit">Lahko</button>
  </form>
</p>
<p>
<form action="/igra/" method="post">
  <button name="tezavnost" value="Srednje" type="submit">srednje</button>
</form>
</p>
<p>
  <form action="/igra/" method="post">
  <button name="tezavnost" value="Težko" type="submit">Težko</button>
</form>
</p>
</body>