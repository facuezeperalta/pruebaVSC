// setTimeout(function, tiempo en ms) para definir retrasos 

let texto = 'tiempo cumplido';

function saludar(){
    console.log(texto);
}

function alertainactivo(){
    alert('se ha cerrado tu sesión');
}

setTimeout(saludar,2000);


setTimeout(alertainactivo,5000);

// esta función setTimeout se ejecuta una sola vez luego del tiempo transcurrido.