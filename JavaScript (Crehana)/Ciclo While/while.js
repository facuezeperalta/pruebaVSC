// while (condicion) { codigo que se ejecuta hasta cumplir condición}

/* let i = 1;

while (i < 50000){
    document.write(i + '<br>');
    i++;
} */
/* 
do while permite ejecutar el codigo una vez al menos. se ejecuta 
luego se ve la condicion */

let i = 1;
do{
    document.write(i + '<br>' + 'do while');
    i++;
}while (i <11);