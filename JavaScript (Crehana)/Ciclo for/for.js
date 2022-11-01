// ciclo for 
/* // for (variable inicio;longitud o condición; incremento) {
    codigo que queremos repetir

} */
//con arreglos
/* let semana = ['lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']
for (let i = 0; i < semana.length; i++){
    console.log(semana[i]);
}
 */
// For in  sirven para recorrer arreglos especificamente.

let semana = ['lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']

for (dia in semana){
    console.log(semana[dia]+'.');
}