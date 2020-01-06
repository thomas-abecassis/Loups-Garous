socket= new WebSocket('ws:/localhost:6789');

var joueursHTML; //variable ici pour la rendre globale

socket.onmessage= function(s) {
    data = JSON.parse(s.data);
    switch(data.type){
    case 'utilisateur':
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
        var i=0;
        joueursHTML=document.getElementById("boxJoueurs");
        if(nbJoueurs==0){
            data.contenu.joueurs.forEach(function(joueur) {
                //on créer une div 
                var div = document.createElement("div");
                div.setAttribute("class", "joueur");
                div.innerHTML=joueur[0];
                //on créer un bouton
                var b = document.createElement("input");
                b.setAttribute("type", "button");
                b.setAttribute("class", "boutonVote");
                //on lui rajoute un event
                b.addEventListener('click',function(){
                    vote(b);
                });
                //on rajoute le bouton dans la div
                div.appendChild(b);
                //pour finir on rajoute la div dans le boJoueurs
                joueursHTML.appendChild(div);
                i++;
            })}else{
                var i=0;
                joueursHTML = document.getElementById("boxJoueurs");
                data.contenu.joueurs.forEach(function(joueur) {
                    if(joueur[1]){
                        joueursHTML.children[i].className= "joueur vivant";
                        }else{
                            joueursHTML.children[i].className="joueur mort ";
                            joueursHTML.children[i].children[0].classList.add('desactiver');
                        }
                i++;
            })
            }
        if(data.contenu.jour==false ){
            if(document.getElementById('imagefondJour')!==null){
                document.getElementById('imagefondJour').id="imagefondNuit";        
                chat=document.getElementById('chat');
                chat.innerHTML+="<div class=\"msgChat\" style=\" width=400px\">La nuit tombe et le village s\'endort </div>";}
        }
        else {
            if(document.getElementById('imagefondNuit')!==null){
                document.getElementById('imagefondNuit').id="imagefondJour";}
                chat=document.getElementById('chat');
                chat.innerHTML+="<div class=\"msgChat\" style=\" width=400px\">Le village se réveille, il est temps pour les villageois de voter</div>";
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

function vote(b){
    var div=b.parentNode;
    var i=0; 
    while((div=div.previousSibling )!=null){ // ici je compte l'index du bouton sur lequel on clique par rapport à la boxJoueur
        if( !div.classList.contains("mort")){ 
            i++;
        }
    }
    socket.send(JSON.stringify({type : "vote", contenu : i}));
}



window.onload=function(){
    var form=document.getElementById("chatForm");
    var inpChat=document.getElementById('nomChat');
    form.addEventListener("submit",function(){
        socket.send(JSON.stringify({type : "chat", contenu : inpChat.value}));
        inpChat.value="";
    });

    var boutChat=document.getElementById('boutonChat');
    boutChat.addEventListener("click",function(){
        socket.send(JSON.stringify({type : "chat", contenu : inpChat.value}));
        inpChat.value="";
    });
}