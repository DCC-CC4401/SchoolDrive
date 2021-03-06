//VARIABLES FORMULARIO
const form  = document.getElementById('form');
const nombreusuario = document.getElementById('nombre_usuario');
const nombrespanError = document.getElementById('nombreError');
const apellidousuario = document.getElementById('Apellido');
const apellidospanError = document.getElementById('apellidoError');
const constraseñausuario = document.getElementById('contraseña');
const constraseñaVerifusuario = document.getElementById('contraseñaVerif');
const contraseñaspanErrorInput = document.getElementById('contraseñaErrorInput');
const contraseñaspanError = document.getElementById('contraseñaError');
const apodousuario = document.getElementById("apodo");
const apodospanError = document.getElementById("apodoError");
const mailusuario = document.getElementById("mail");
const mailspanError = document.getElementById("mailError");
const searchFiles = document.getElementById("search-files");
const searchUsers = document.getElementById("search-users");
const searchTags = document.getElementById("search-tags");
const searchForm = document.getElementById("searchf");
var usuarioregex = /([a-zA-Z ]){3,30}/;
var apodoregex = /([a-zA-Z0-9]){3,15}/;

$(nombreusuario).change( function (){
    if (usuarioregex.test($(nombreusuario).val())){
        nombreusuario.classList.remove("invalid");
        nombrespanError.style.display = "none";
    } else {
        nombreError();
    }
})

function nombreError() {
    nombreusuario.classList += " invalid";
    nombrespanError.style.display = "block";
};

$(apellidousuario).change( function (){
    if (usuarioregex.test($(apellidousuario).val())){
        apellidousuario.classList.remove("invalid");
        apellidospanError.style.display = "none";
    } else {
        apellidoError();
    }
})

function apellidoError() {
    apellidousuario.classList += " invalid";
    apellidospanError.style.display = "block";
};

$(constraseñausuario).change( function (){
    if (!constraseñausuario.validity.valueMissing){
        contraseñaspanErrorInput.style.display = "none";
    } else {
        contraseñaInputError();
    }
})

$(constraseñaVerifusuario).change( function (){
    if ($(constraseñaVerifusuario).val()==$(constraseñausuario).val()){
        constraseñausuario.classList.remove("invalid");
        constraseñaVerifusuario.classList.remove("invalid");
        contraseñaspanError.style.display = "none";
    } else {
        contraseñaError();
    }
})

function contraseñaError() {
    constraseñausuario.classList += " invalid";
    constraseñaVerifusuario.classList += " invalid";
    contraseñaspanError.style.display = "block";
};

function contraseñaInputError() {
    constraseñausuario.classList += " invalid";
    constraseñaVerifusuario.classList += " invalid";
    contraseñaspanErrorInput.style.display = "block";
};


$(apodousuario).change( function (){
    if (apodoregex.test($(apodousuario).val())){
        apodousuario.classList.remove("invalid");
        apodospanError.style.display = "none";
    } else {
        apodoError();
    }
})

function apodoError() {
    apodousuario.classList += " invalid";
    apodospanError.style.display = "block";
};

$(mailusuario).change( function (){
    if (mailusuario.validity.valid){
        mailusuario.classList.remove("invalid");
        mailspanError.style.display = "none";
    } else {
        mailError();
    }
})

function mailError() {
    mailusuario.classList += " invalid";
    mailspanError.style.display = "block";
};


form.addEventListener('submit', function (event){
    var count = 0;
    if (!mailusuario.validity.valid){
		mailError();
		count++;
    }
    if (nombreusuario.validity.valueMissing){
		nombreError();
		count++;
    }
    if (apellidousuario.validity.valueMissing){
		apellidoError();
		count++;
    }
    if (apodousuario.validity.valueMissing){
		apodoError();
		count++;
    }
    if (constraseñausuario.validity.valueMissing){
		contraseñaInputError();
		count++;
    }
    if ($(constraseñaVerifusuario).val()!=$(constraseñausuario).val()){
        contraseñaError();
        count++;
    }
	if (count>0){
		event.preventDefault();
	}
});

function send_form(){
    $('#selected_search').val($(this).attr('data-value'));
    $('#search_form').submit();
}
