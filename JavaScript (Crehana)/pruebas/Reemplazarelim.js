// creamos elementos

var newParrafo = document.createElement('p');

var newText = document.createTextNode('Hola, soy otro nuevo texto');

newParrafo.appendChild(newText);

newParrafo.setAttribute('class','texto');

//ahora voy a agregar un nuevo elemento.

var parrafosSelected = document.getElementsByClassName('texto');

var padreParrafos_ = parrafosSelected[0].parentNode;

//Reemplazar un elmento

padreParrafos_.replaceChild(newParrafo,parrafosSelected[0]);
/*
eliminar un elemento. se le pasa como parametro el elemento que queremos 
 eliminar */

padreParrafos_.removeChild(parrafosSelected[0]);
