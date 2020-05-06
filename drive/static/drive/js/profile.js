//VARIABLES FORMULARIO
const form  = document.getElementById('form');
const nombreusuario = document.getElementById('Nombre');
const nombrespanError = document.getElementById('nombreError');
const apellidousuario = document.getElementById('Apellido');
const apellidospanError = document.getElementById('apellidoError');
const apodousuario = document.getElementById("Apodo");
const apodospanError = document.getElementById("apodoError");
const fechausuario = document.getElementById("Nacimiento");
const fechaspanError = document.getElementById("fechaError");
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

$(fechausuario).change( function (){
    if ($(fechausuario).val()!=null){
        fechausuario.classList.remove("invalid");
        fechaspanError.style.display = "none";
    } else {
        fechaError();
    }
})

function fechaError() {
    fechausuario.classList += " invalid";
    fechaspanError.style.display = "block";
};


form.addEventListener('submit', function (event){
    var count = 0;
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
    if ($(fechausuario).val()==null){
        fechaError();
        count++;
    }
	if (count>0){
		event.preventDefault();
	}
});




