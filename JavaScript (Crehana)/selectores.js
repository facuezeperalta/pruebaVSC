// Selectores individuales 
// getElementById(): selecciona el elemento por su Id.
// querySelector(): selecciona el elemento con un selector de css, devolviendo el primer 
// elemento que coincida.

//Selectores Múltiples:
// getElemementsbyName(): selecciona todos los elementos que tenga la clase
// especificada.
//getElemementsbyName(): selecciona todos los elementos con la etiqueta
// especificada.
// querySelectorAll(): selecciona todos los elementos con el selector css indicado.

//----------------------------------------------------------------

var boton = document.getElementById('boton');

var segundoPerrafo = document.querySelector('#segundo');

//----------------------------------------------------------------
//Selectores Multiples.

var parrafos = document.getElementsByClassName('texto');
var etiquetas = document.getElementsByTagName('p');
var parrafos2 = document.querySelectorAll('.texto');// puedo acceder también como un arreglo
