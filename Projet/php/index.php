<!DOCTYPE html>
<html>
<head>
  <title>Personal Website</title>
  <meta charset="utf-8">

  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous">


  <!--Import Google Icon Font-->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <!-- Social media Font -->
  <link rel="stylesheet" href="https://d1azc1qln24ryf.cloudfront.net/114779/Socicon/style-cf.css?9ukd8d">

  <!-- Materialize: Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link rel="stylesheet" type="text/css" href="../css/styles.css">

  <!--Let browser know website is optimized for mobile-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>

<body class=" grey lighten-3">
  <div class="mainJeu">
    <?php include("joueur.php"); ?>
  </div>


    <div class="chat">
      <fieldset>
       <legend>Un chat en jQuery</legend>
        <div id="conversation"></div>
        <form id="formChat" action="../php/chat.php" method="post">
          <input id="test" type="text" id="nom" value="pseudo" size="6">
          <input id="test2" type="text" id="message" size="27">
          <button type="button" id="envoyer" title="Envoyer"></button>
        </form>
      </fieldset>
    </div>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script src="../js/chat.js"></script>
<script src="../js/test.js"></script>
</body>
</html>
