// Metodos y propiedades para arreglos.
var familia = ['Alejandro', 'Maria','Pedro']
var familiaDos = ['Facu','Raul','Marcos', 'Jimena']

// lengths para saber el tamaño de un arreglo.
var cantmiembrosUno = familia.length;

// contact para unir dos arreglos.

var nuevaFamilia = familia.concat(familiaDos);

// join convierte a texto un arreglo se le indica el separador es lo contrario a split

var joinfamilia = familia.join('-');

// pop elimina el ultimo elemento del arreglo.

var familiaIncompleta = familia.pop();

// push agrega un elemento al final del arreglo.

var familiaMasGrande = familia.push(1);

// shift elimina el primero elemento del arreglo.



//unshift agrega un elemento al comienzo del arreglo.

//reverse ordenar el arreglo al revés.

var familiInvertida = familia.reverse;
