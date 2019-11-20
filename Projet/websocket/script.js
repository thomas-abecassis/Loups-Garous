socket= new WebSocket('ws:/localhost:6789');

socket.onmessage= function(s) {
    data = JSON.parse(event.data);
    switch(data.type){
    case 'nbUtilisateurs':
        compteur=document.getElementById('contenu');
        compteur.innerHTML+=data.contenu;
        break;
    case 'chat':
    	chat=document.getElementById('chat');
        chat.innerHTML+="<div class=\"msgChat\" style=\" width=400px\">"+data.contenu+"</div>";
        break;
    case 'jeu' :
        jeu=document.getElementById('jeu');
        jeu.innerHTML="<div class=\"msgChat\" style=\" width=50px\">"+"Compteur :"+data.contenu+"</div>";
        break;
    case 'etatPartie':
        console.log(data.contenu);
        var nbJoueurs = document.getElementById("boxJoueurs").children.length;
        if(nbJoueurs==0){
            data.contenu.joueurs.forEach(function(joueur) {
                document.getElementById('boxJoueurs').innerHTML+="<div class=\" joueur \">"+ joueur[0]+"</div>";
            })}else{
                var i=0;
                var joueursHTML = document.getElementById("boxJoueurs");
                data.contenu.joueurs.forEach(function(joueur) {
                    if(joueur[1]){
                        joueursHTML.children[i].className= "joueur vivant";
                        }else{
                            joueursHTML.children[i].className="joueur mort ";
                        }
                i++;
            })
            }
        if(data.contenu.jour==false ){
            if(document.getElementById('imagefondJour')===null){}
            else{
            document.getElementById('imagefondJour').id="imagefondNuit";}
            }else {
                if(document.getElementById('imagefondNuit')===null){}
                else{
                document.getElementById('imagefondNuit').id="imagefondJour";
                }
            }
    }
}

function envoieMessageServeur(){
	var boutChat=document.getElementById('boutonChat');
	var inpChat=document.getElementById('nomChat');

	var boutJeu=document.getElementById('boutonJeu');
	var inpJeu=document.getElementById('nomJeu');

	boutChat.onclick=function(){
		socket.send(JSON.stringify({type : "chat", contenu : inpChat.value}));
	}

	boutJeu.onclick=function(){
		socket.send(JSON.stringify({type : "jeu", contenu : inpJeu.value}));
	}


}

window.onload=envoieMessageServeur();