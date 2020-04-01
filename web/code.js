// a function called when the button is clicked
function buttonClicked() {
    var myMessage = document.getElementById("message");
    myMessage.innerHTML = "it is " + new Date().getTime();
}

// go get some data from the server and show it on the page
fetch('/users/1').then(r=>r.json()).then(user => {

    document.getElementById('name').innerHTML = "Logged in as " + user.name;

})
