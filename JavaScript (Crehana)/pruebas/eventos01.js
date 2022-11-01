//agregar un eventListeners
var boton = document.getElementById('boton');
var boton2 = document.getElementById('boton2');

function alerta(){
    alert('Hola a todos');
}

boton.addEventListener('click',alerta);

//eliminar escuchadores removeventlisener
function removarAlerta(){ 
    boton.removeEventListener('click',alerta);
}
boton2.addEventListener('click',removarAlerta);