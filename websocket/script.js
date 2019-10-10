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
    }
};

function envoieMessageServeur(){
	var bout=document.getElementById('bouton');
	var inp=document.getElementById('nom');

	bout.onclick=function(){
		socket.send(inp.value);
	}
}

window.onload=envoieMessageServeur();