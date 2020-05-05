//VARIABLES FORMULARIO
const form  = document.getElementById('form');
const nombreusuario = document.getElementById('nombre_usuario');
const nombrespanError = document.getElementById('nombreError');
const constraseñausuario = document.getElementById('contraseña');
const apodousuario = document.getElementById("apodo");
const apodospanError = document.getElementById("apodoError");
const mailusuario = document.getElementById("mail");
const mailspanError = document.getElementById("mailError");
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
    if (apodousuario.validity.valueMissing){
		apodoError();
		count++;
	}
	if (count>0){
		event.preventDefault();
	}
});




