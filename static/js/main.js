var sock = new SockJS('http://' + window.location.host + '/ws', 'xhr-streaming', {debug:true});

sock.onopen = function(){
    console.log('open')
}
// send message from form
document.forms.publish.onsubmit = function() {
  console.log(this.message.value, 'onsubmit');
  sock.send(this.message.value);
  return false;
};

// income message handler
sock.onmessage = function(event) {
  console.log(event, 'event');
  showMessage(event.data);
};

// show message in div#subscribe
function showMessage(message) {
  var messageElem = document.createElement('div');
  messageElem.appendChild(document.createTextNode(message));
  console.log(document.getElementById('subscribe'));
  console.log(messageElem, 'messageElem');
  document.getElementById('subscribe').appendChild(messageElem);
}

document.getElementById('signout').addEventListener("click", function(e){
    window.location.href = "signout"
});
