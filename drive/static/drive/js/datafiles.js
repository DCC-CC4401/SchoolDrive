//VARIABLES FORMULARIO
const form  = document.getElementById('archivo-nuevo');
const nombrearchivo = document.getElementById('nombreArchivo');
const nombrearchivospanError = document.getElementById('nombrearchivospanError');
const archivo = document.getElementById('archivo');
const archivospanError = document.getElementById('archivospanError');
const treeFolder = document.getElementById('treeFolder');
const currentFolder = document.getElementById('currentFolder');
var nombrearchivoregex = /[\\/:"*?<>\.|]+/;

$(document).ready(function() {
    $("#treeview").append($('#treeFolder').val())
    var treeview = $("#treeview").shieldTreeView().swidget();
    treeview.expanded(true, [0,0]);



    $(window).keydown(function(event){
        if(event.keyCode == 13) {
          event.preventDefault();
          return false;
        }
      });
  });

  $(function(){

    $('#tagsNewFile').tagInput({
        labelClass:"badge badge-primary"
      });
  
  });

$(nombrearchivo).change( function (){
    if (!nombrearchivoregex.test($(nombrearchivo).val())){
        nombrearchivo.classList.remove("invalid");
        nombrearchivospanError.style.display = "none";
    } else {
        nombrearchivoError();
    }
})
function nombrearchivoError() {
    nombrearchivo.classList += " invalid";
    nombrearchivospanError.style.display = "block";
};

$(archivo).change( function (){
    if (archivo.files.length != 0){
        archivospanError.style.display = "none";
    } else {
        archivoError();
    }
})

$(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});

function archivoError() {
    //archivo.classList += " invalid";
    archivospanError.style.display = "block";
};

form.addEventListener('submit', function (event){
    console.log($('#tagsNewFileVal').val())
    var count = 0;
    if (nombrearchivoregex.test($(nombrearchivo).val()) && $(nombrearchivo).val()!=""){
        nombrearchivoError();
        count++;
    }
    if (archivo.files.length == 0){
        archivoError();
        count++;
    }
	if (count>0){
		event.preventDefault();
    }
});




