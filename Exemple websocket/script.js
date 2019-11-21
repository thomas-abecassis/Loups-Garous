


socket= new WebSocket('ws:/localhost:6790'); //on creer la connexion avec notre websocket python

socket.onmessage= function(s) { // quand on recoit un message du websocket on execute le code de la fonction
    data = JSON.parse(event.data); //event.data est un json que le socket nous a envoyé, on le charge avec json.parse
    chat=document.getElementById('chat');//on récupère la div qui a l'id "chat" dans le html
    chat.innerHTML+="<div class=\"msgChat\" style=\" width=400px\">"+data.contenu+"</div>";// et on ajoute une div dedant avec comme
    																					  // contenu le message envoyé par le socket

}


function envoieMessageServeur(){
	var boutChat=document.getElementById('boutonChat');
	var inpChat=document.getElementById('nomChat');


	boutChat.onclick=function() {
		socket.send(JSON.stringify({type : "chat", contenu : inpChat.value}));//avec inpChat.value on recupère la valeur écrite par l'utilisateur dans le chat
	}



}

window.onload=envoieMessageServeur();