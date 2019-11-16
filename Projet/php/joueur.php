<?php   
$test=array(
"joueur1"=>array("nom" => "Reimu", "role" => "touhou", "image" => "../files/images/1.png"),
"joueur2"=>array("nom" => "2B", "role" => "nierAutomata", "image" => "../files/images/2.png"),
"joueur3"=>array("nom" => "Cypra", "role" => "Xenoblade Chronicle 2", "image" => "../files/images/3.png"),
"joueur4"=>array("nom" => "Futaba", "role" => "Persona 5", "image" => "../files/images/4.png"),
"joueur5"=>array("nom" => "Giorno Giovanna", "role" => "Jojo's bizarre's adventures", "image" => "../files/images/5.png"),
"joueur6"=>array("nom" => "Kira", "role" => "Watashi wa kira desu", "image" => "../files/images/6.png"),
"joueur7"=>array("nom" => "Beatrice-sama", "role" => "Umineko", "image" => "../files/images/7.png"),
"joueur8"=>array("nom" => "Rem or Emilia ?", "role" => "Re Zero(rem)", "image" => "../files/images/8.png"),
"joueur9"=>array("nom" => "Mitsuha", "role" => "Your Name", "image" => "../files/images/4.png"),
"joueur10"=>array("nom" => "Reimu", "role" => "touhou", "image" => "../files/images/5.png"),
"joueur11"=>array("nom" => "Reimu", "role" => "touhou", "image" => "../files/images/3.png"),
"joueur12"=>array("nom" => "Reimu", "role" => "touhou", "image" => "../files/images/8.png"),
);

for($e=0;$e<=2;$e++){
  echo "<div class=\"row\">";
  for($i=1;$i<=4;$i++){

    $compteur=$e*4+$i;
    $joueur="joueur" .strval($compteur);

    echo 
          "<div class=\"col s3 card small\" >
          <div class=\"card-image\">
            <img src=\"" .$test[$joueur]["image"]  ."\">
            <span class=\"card-title black-text\">" .$test[$joueur]["nom"] ."</span>
          </div>
          <div class=\"card-content\">
            <p>" .$test[$joueur]["role"] ."</p>
          </div>
        </div>";
  }
  echo "</div>";
}
?>
