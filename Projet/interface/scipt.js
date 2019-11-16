var json={
"joueurs":[
	{"nom" : "1","role" : "role1", "etat" : "vivant"},
	{"nom" : "2","role" : "role2", "etat" : "vivant"},
	{"nom" : "3","role" : "role3", "etat" : "vivant" },
	{"nom" : "4","role" : "role4", "etat" : "vivant" },
	{"nom" : "5","role" : "role5", "etat" : "vivant" },
	{"nom" : "6","role" : "role6", "etat" : "vivant"},
	{"nom" : "7","role" : "role7", "etat" : "vivant"},
	{"nom" : "8","role" : "role8", "etat" : "vivant"},
	{"nom" : "9","role" : "role9", "etat" : "vivant"},
	{"nom" : "10","role" : "role10", "etat" : "vivant"},
	{"nom" : "11","role" : "role11", "etat" : "vivant"},
	{"nom" : "12","role" : "role12", "etat" : "mort"}
	],
	"nbJours":"1",
	"roleTour":"voyante",
};


function majJoueurs(json){
	var divASelectionner;
	var nom;
	var role;
	var joueur;
	var etat;
	for(var i=0; i<12; i++){
		divASelectionner="joueur" + (i+1).toString();
		joueur=document.getElementById(divASelectionner);


		nom=joueur.getElementsByClassName("nom");
		nom[0].innerHTML="mon nom est : " + json.joueurs[i].nom;


		role=joueur.getElementsByClassName("role");
		role[0].innerHTML="mon role est : " + json.joueurs[i].role;

		joueur.className+=" "+json.joueurs[i].etat;
	}
	var div=document.getElementById("nbJours");
	div.innerHTML="jour : "+json.nbJours;
	div=document.getElementById("tourRole");
	div.innerHTML="au tour de : " + json.roleTour;
}


var bouton=document.getElementById("boutonMAJ");
bouton.onclick=function(){
	majJoueurs(json);
}
