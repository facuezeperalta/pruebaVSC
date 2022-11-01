var parrafo = document.getElementsByClassName('texto')[0];

//evento mouseOver al colocar el mouse arriba 

parrafo.addEventListener('mouseover',function(){
    var newparrafo = document.createElement('p');
    var newtext = document.createTextNode('Aparecí perro');
    newparrafo.appendChild(newtext);
    newparrafo.setAttribute('class','texto2');
    newparrafo.id = 'nuevoparrafoId';
    var contenedor = document.getElementsByClassName('contenedor')[0];
    contenedor.appendChild(newparrafo);
});

//mouseout al sacar el mouse.
parrafo.addEventListener('mouseout',function(){
    var addedparrafo = document.getElementById('nuevoparrafoId');
    var contenedor = document.getElementsByClassName('contenedor')[0];    

    contenedor.removeChild(addedparrafo);
});


