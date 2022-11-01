var Parrafonuevo = document.createElement('p');
var Textonuevo = document.createTextNode('Hola soy un texto creado en Js');

Parrafonuevo.appendChild(Textonuevo);

Parrafonuevo.setAttribute('class','texto');

/* var contenedor = document.getElementsByClassName('contenedor')[0];
 */



//seleccionar el elemento padre de un elemento.
var primerparrafo =  document.getElementsByClassName('texto')[0];

padreparrafos = primerparrafo.parentNode;

padreparrafos.className = 'contenedor';

//con insertBefore inserto el parrafo nuevo antes de primero parrafo.
padreparrafos.insertBefore(Parrafonuevo, primerparrafo)


// Selecciono el elemento padre del parraforSelected,parentNode es para ir al padre y lo guardo en una variable..
// ahora ubico el parrafoUbicado dentro del contenedor.

//padreParrafos.insertBefore(NuevoParrafo, primerParrafo);
//creo una variable sin seleccion en el Arreglo.








