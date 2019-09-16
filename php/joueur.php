<?php   
$test=array(
"joueur1"=>array("nom" => "Reimu", "role" => "touhou"),
"joueur2"=>array("nom" => "2B", "role" => "nierAutomata"),
"joueur3"=>array("nom" => "Cypra", "role" => "Xenoblade Chronicle 2"),
"joueur4"=>array("nom" => "Futaba", "role" => "Persona 5"),
"joueur5"=>array("nom" => "Giorno Giovanna", "role" => "Jojo's bizarre's adventures"),
"joueur6"=>array("nom" => "Kira", "role" => "Watashi wa kira desu"),
"joueur7"=>array("nom" => "Beatrice-sama", "role" => "Umineko"),
"joueur8"=>array("nom" => "Rem or Emilia ?", "role" => "Re Zero(rem)"),
"joueur9"=>array("nom" => "Mitsuha", "role" => "Your Name"),
"joueur10"=>array("nom" => "Reimu", "role" => "touhou"),
"joueur11"=>array("nom" => "Reimu", "role" => "touhou"),
"joueur12"=>array("nom" => "Reimu", "role" => "touhou"),
);

for($e=0;$e<=2;$e++){
  echo "<div class=\"row\">";
  for($i=1;$i<=4;$i++){

    $compteur=$e*4+$i;
    $joueur="joueur" .strval($compteur);

    echo 
          "<div class=\"col s3 card small\" >
          <div class=\"card-image\">
            <img src=\"../css/images/dango.jpg\">
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
