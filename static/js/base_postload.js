var contact = document.getElementById("contact-link");
contact.addEventListener("click", scrollToBottom);

function scrollToBottom() {
    window.scrollTo(0,document.body.scrollHeight);
}

// Django Messages Code
$('.toast').toast('show'); //Required to change opacity CSS of message container
//This timeout function hides the message container after 3 seconds
var message_ele = document.getElementById("message-container-id");
setTimeout(function(){ 
    $('.toast').toast('hide');
}, 3000);