function SelectRedirect() {
    // ON selection of section this function will work
    //alert( document.getElementById('s1').value);

    switch (document.getElementById('s1').value) {
        case "voter":
            window.location = "{% url 'register_voter' %}";
            break;

        case "candidate":
            window.location = "{% url 'reg_cand'%}";
            break;

        case "party":
            window.location = "{% url 'register_party'%}";
            break;
        case "official":
            window.location = "{% url 'register_official'%}";
            break;

        /// Can be extended to other different selections of SubCategory //////
        default:
            window.location = "{% url 'home'%}"; // if no selection matches then redirected to home page
            break;
    }// end of switch 
}
