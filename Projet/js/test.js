

function reqListener () {

  	obj = JSON.parse(this.responseText);
  	var login = obj.login;
  	var message = obj.message;

  	for(var key in login){
		var node = document.createElement("div");
		node.className="message";
		var textnode = document.createTextNode(login[key].concat('>',message[key]));      
		node.appendChild(textnode);                            
		document.getElementById("conversation").appendChild(node);
	}  
}


var oReq = new XMLHttpRequest();
oReq.onload = reqListener;
oReq.open("get", "test.php", true);
oReq.send();
