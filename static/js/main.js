$(document).ready(function(){
    var sock = new WebSocket('ws://' + window.location.host + '/ws');

    sock.onopen = function(){
        console.log('open')
    }
    // send message from form
    $('#submit').click(function() {
        var msg = $('#message').val();
        console.log(msg, 'onsubmit');
        sock.send(msg);
    });

    // income message handler
    sock.onmessage = function(event) {
      console.log(event, 'event');
      showMessage(event.data);
    };
    
    // show message in div#subscribe
    function showMessage(message) {
      var messageElem = $('#subscribe')
      console.log(messageElem, 'messageElem');
      messageElem.append(message);
    }
    
    $('#signout').click(function(){
        window.location.href = "signout"
    });
});
