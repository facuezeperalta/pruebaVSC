let parrafos = document.getElementsByClassName('texto');

//agrego evento.
/* parrafos[0].addEventListener('click',function(e){
    parrafos[0].className = 'texto fondo-rojo'
}); */

for (var i = 0; i < parrafos.length; i++){
    parrafos[i].addEventListener('click',function(e){
        this.className = 'texto fondo-rojo';
    });
}