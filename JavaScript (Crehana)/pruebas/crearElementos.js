// crear un nuevo elemento o nodo

// Creamos un nuevo parrafor
var newparrafo =  document.createElement('p');

// creamos un nuevo texto para el parrafo

var newtext = document.createTextNode('Hola soy un nuevo texto para agregar.');

// Luego tomamos en texto y lo ponemos dentro del párrafo creado.
// lo agregamos al texto en el parrafo.

newparrafo.appendChild(newtext);

// luego agregamos un nuevo atributo de clase. 

newparrafo.setAttribute('class','texto'); // recibe dos valres: atributo
//y el valor, en este caso así tiene el mismo estilo de css.

// Seleccionamos la clase contenedor creamos una variable para tenerlo.

var contenedor = document.getElementsByClassName('contenedor')[0];

// agrego el nuevo parrafo dentro del contenedor

contenedor.appendChild(newparrafo);

/*



*/
