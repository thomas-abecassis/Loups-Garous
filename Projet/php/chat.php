<?php

require_once 'Model.php';

$nom = $_POST['nom'];                    //On récupère le pseudo et on le stocke dans une variable
$message = $_POST['message'];            //On fait de même avec le message
$sql="INSERT INTO messages(message) VALUES ('$message')";
Model::$pdo->exec($sql);


?>
