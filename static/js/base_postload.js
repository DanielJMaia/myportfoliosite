var contact = document.getElementById("contact-link");
contact.addEventListener("click", scrollToBottom);

function scrollToBottom() {
    window.scrollTo(0,document.body.scrollHeight);
}