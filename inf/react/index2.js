const crearMayus = function(registro){
    return function(mensaje){
        registro(mensaje.toUpperCase()+"!!!!");
    };
};


const enfasis = crearMayus(
    function(mensaje){ 
        console.log(mensaje)
    }
);

enfasis("Las funciones pueden ser retornadas por otras funciones");
enfasis("");