function elegirColor(){
    estadoActivador = document.getElementById('colorFavorito').checked;
    if(estadoActivador == true){
        document.getElementById('red').disabled = false;
        document.getElementById('green').disabled = false;
        document.getElementById('blue').disabled = false;
        document.getElementById('other').disabled = false;
    }else{
        document.getElementById('red').disabled = true;
        document.getElementById('green').disabled = true;
        document.getElementById('blue').disabled = true;
        document.getElementById('other').disabled = true;
    }
}
// evento change 
var inputColorFavorito = document.getElementById('colorFavorito');

inputColorFavorito.addEventListener('change', elegirColor);


