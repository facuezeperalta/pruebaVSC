// Metodos y propiedades de cadenas de texto.
var texto = 'hola, soy un texto'

//Metodo length 
var numeroCaracteres = texto.length;

//Metoedo toUpperCase() - Transforma todos los caracteres a mayuscula.
var mayus = texto.toUpperCase();

// Metodo toLowerCase() - Transforma todos los caracteres a minúscula.
var minus = texto.toLowerCase();

// Metodo substring(0,0) Extrae de un punto hasta otro 
//los caracteres de una cadena
var extract = texto.substring(0,-1);

// replace (valor1,valor2) -- Reemplaza cadena de caract por otra. valor1 es 
// el valor a reemplazar y valor2 es el valor de reemplazo.
var textreplace = texto.replace('texto','niño');


// indexOf('o')Buscar el primer caracter que coincidia con el valor buscado
var buscarO = texto.indexOf('o');

// lastIndexOf('o') Busca la ultima posición que conicida con el valor.
var buscarLastO = texto.lastIndexOf('o');

// split(' ') convierte la cadena de texte en un arreglo dividiendo los elemetntos 
//segun el separador indicado en el ejemplo es un ' ' espacio.

var textoarreglo = texto.split(' ');