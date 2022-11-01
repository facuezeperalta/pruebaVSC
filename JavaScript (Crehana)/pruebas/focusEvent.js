//Evento focus.
// es una variable global.
var campoNombre = document.getElementById('nombre');

campoNombre.addEventListener('focus', function(){
    campoNombre.setAttribute('value', 'Tengo el foco');
});

campoNombre.addEventListener('blur', function(){
    campoNombre.setAttribute('value','');
});