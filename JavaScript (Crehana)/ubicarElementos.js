var NuevoParrafo = document.createElement('p');

var textNuevo = document.createTextNode('Hola soy un texto nuevo');

NuevoParrafo.appendChild(textNuevo);

NuevoParrafo.setAttribute('class', 'texto');

//var contenedor2 = document.getElementsByClassName('contenedor') [0];

//seleccionar el elemento padre de un elemento.

//voy al elemento hijo y lo selecciono por su ClassName.

var primerParrafo = document.getElementsByClassName('texto')[0];

// Selecciono el elemento padre del parraforSelected,parentNode es para ir al padre y lo guardo en una variable..
var padreParrafos = primerParrafo.parentNode;

padreParrafos.className = 'contenedor';
// ahora ubico el parrafoUbicado dentro del contenedor.

//padreParrafos.insertBefore(NuevoParrafo, primerParrafo);
//creo una variable sin seleccion en el Arreglo.

var parrafos = document.getElementsByClassName('texto');

padreParrafos.insertBefore(NuevoParrafo, parrafos[0]);











