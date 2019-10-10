<?php

require_once 'Model.php';

$rep=Model::$pdo->query('select * from envoi JOIN messages on envoi.message_nb=messages.nbMessage JOIN compte on envoi.compte_login=compte.login ORDER BY messages.nbMessage'); // je ne crois pas que le order soit obligatoire
$rep->setFetchMode(PDO::FETCH_ASSOC);
$tab = $rep->fetchAll();

$tab_logins=array();
$tab_messages=array();

foreach($tab as $message){
	array_push($tab_logins,$message['nom']);
	array_push($tab_messages,$message['message']);
}

$data = array(
	'login'=> $tab_logins,
	'message'=>$tab_messages
);



echo json_encode($data, JSON_FORCE_OBJECT);
?>