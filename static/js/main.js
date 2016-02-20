$(document).ready(function(){
    var sock = new WebSocket('ws://' + window.location.host + '/ws');

    // show message in div#subscribe
    function showMessage(message) {
      var messageElem = $('#subscribe')
      messageElem.append(message);
    }

    sock.onopen = function(){
        showMessage('Connection to server started\n')
    }

    // send message from form
    $('#submit').click(function() {
        var msg = $('#message');
        sock.send(msg.val());
        msg.val('').focus()
    });

    // income message handler
    sock.onmessage = function(event) {
      console.log(event, 'event');
      showMessage(event.data);
    };

    $('#signout').click(function(){
        window.location.href = "signout"
    });
});
