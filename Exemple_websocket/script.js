socket= new WebSocket('ws:/localhost:6790');

socket.onmessage= function(s) {
    data = JSON.parse(event.data);
    chat=document.getElementById('chat');
    chat.innerHTML+="<div style=\" width=400px\">"+data.contenu+"</div>";

}


function envoieMessageServeur(){
	var boutChat=document.getElementById('boutonChat');
	var inpChat=document.getElementById('nomChat');


	boutChat.onclick=function(){
		socket.send(JSON.stringify({type : "chat", contenu : inpChat.value}));
	}



}
/*
function envoiePseudo(){
	var boutPseudo=document.getElementById('boutonPseudo');
	var nom=document.getElementById('nom');

	boutPseudo.onclick=function(){
		socket.send(JSON.stringify({type : "chat", contenu : inpChat.value}));
	}


}*/
window.onload=envoieMessageServeur();