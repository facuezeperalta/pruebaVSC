var boton = document.getElementById('boton');

boton.addEventListener('dblclick',function(){
    var nuevoparrafo = document.createElement('p');
    var textonuevo = document.createTextNode('texto de parrafo creado con JS');

    nuevoparrafo.appendChild(textonuevo);
    nuevoparrafo.className ='texto';
    var contenedor = document.getElementsByClassName('contenedor')[0];
    contenedor.appendChild(nuevoparrafo);
});

