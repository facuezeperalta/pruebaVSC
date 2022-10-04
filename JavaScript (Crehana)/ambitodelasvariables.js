//Scope
// es el alcance de una variable, puede ser local o global.

// Variable global - se declara fuera de la funcion

var mensaje = 'Hola soy un mensajes';

function saludar(){
    alert(mensaje);
}
//saludar(); //ejecuto la función.


// Variables locales, se crean dentro de la función.

function despedir(){
    var despedida = 'Adiós, hasta luego.'; // La variable tiene alcance dentro 
    //de la funcion.
    alert(despedida);
}

despedir(); 

