<?php

class Compte{

private $login;
private $nom;

public function __construct($l = null,$ $n =null){
	if(!isnull($l) && !isnull($n)){
		$this->login=$l;
		$this->nom=$n; 
	}
}
}




  ?>