let parrafos = document.getElementsByClassName('texto');

parrafos[0].style.width = '50%';
parrafos[0].style.height = '200px';
parrafos[0].style.padding = '30px';
parrafos[0].style.border = '10px solid red';

let boton = document.getElementById('boton');
let boton2 = document.getElementById('boton2');

boton.addEventListener('click', function(){
    parrafos[0].style.width = '100%';
});



