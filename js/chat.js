

      $(function() {
    afficheConversation();
      
    $('#envoyer').click(function() {
        var nom = $('#nom').val();
        var message = $('#message').val();
        $.post('../php/chat.php', {
            'nom': nom,
            'message': message
        }, afficheConversation);
        $('#message').val('');
    });

    function afficheConversation() {
      $('#conversation').load('../files/ac.htm');
      $('#message').focus();
    }
      
    setInterval(afficheConversation, 4000);
  });