function show_password() {
    var x = document.getElementById("login-pass");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}