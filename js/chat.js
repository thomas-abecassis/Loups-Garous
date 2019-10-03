
document.getElementById('envoyer').onclick=function(){
  var form=new FormData();$
  form.append("message",document.getElementById("test").value);
  var oReq = new XMLHttpRequest();
  oReq.open("POST", "chat.php", true);
  oReq.send(form);
}



