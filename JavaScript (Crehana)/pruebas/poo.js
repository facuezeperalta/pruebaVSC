// Programacion orientada a objetos
//Clases son funciones llamadas funciones constructura 
// se inician con mayusculas. Palabra();
/*
var texto = new String('Hola soy un texto');
console.log(texto);
*/

// clases personalizadas

function Persona(){
    this.nombre;
    this.edad;
}

var persona1 =  new Persona();
persona1.nombre = 'Facundo';
persona1.edad = 18;

var persona2 =  new Persona();

persona2.nombre = 'Roberto';
persona2.edad = 25;


console.log(persona1);
console.log(persona2);
//Puedo pasar parámetros también a la hora de crear la clase.
function Mascota(nombremascota,edadmascota) {
    this.nombrem = nombremascota;
    this.edadm = edadmascota;
}

perro1 = new Mascota('Ringo',8);
console.log(perro1);



// Objetos se pueden crear desde 0. 
// es un colecció de propiedades y metodos.
// método es una función dentro de un objeto.


var planta = {
    //estas son propiedades 
    color: 'verde',
    tamanio: 'Grande',
    // también podemos agregar métodos.
    plant_Info: function(precio){
        console.log('El color de la planta es ' + planta.color + 'y su tamaño es ' + planta.tamanio + 'y su precio es ' + precio);
    
    }

}

console.log(planta.color);
console.log(planta.tamanio);
planta.plant_Info('$1500');





