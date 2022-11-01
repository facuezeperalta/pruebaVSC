// setInterval(funcion,tiempo en ms);

var tiempo = 0;
/* function contar(){
    ++tiempo;
    console.log('tiempo');
} */

setInterval(function(){
    ++tiempo;
    console.log(tiempo);
},1000);

