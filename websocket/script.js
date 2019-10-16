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

    }
};

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