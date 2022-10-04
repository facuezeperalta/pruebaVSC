/* for(variable de inicio; longitud o condición; incremento)
{
    colocamos el codigo aqui adentro}*/

// contar hasta diez con console.log()

for(var i = 1;i <= 100; ++i){//No olvidar incrementar el valor de la variable.
    console.log(i);
}

//Ciclos para recorrer arreglos.

var semana= ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado']

for(var i = 0; i < semana.length; ++i){
    console.log(semana[i]);
}

// for in 

for(dia in semana){ // for i in variable.
    console.log(semana[dia]);
}
