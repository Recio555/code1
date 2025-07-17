var log = function(mensaje){
    console.log(mensaje);

};
var log2 = mensaje =>{
    console.log(mensaje);

};

const mensajes = [
    "Puede ser incertado en arreglos",
    "Hola que tal?",
    log,
    log("Hola mundo"),
    log2
    
];

const dentroFn = ingreso =>{
    ingreso("Puede ser enviados como argumentos a otras funciones");
};

const crearMayus = function(registro){
    return function(mensaje){
        registro(mensaje.toUpperCase()+"!!!!");
    };
};

const crearMayus2 = registro => mensaje => {
    registro(mensaje.toUpperCase()+"!!!!"); 
};

//const enfasis = crearMayus(mensaje => console.log(mensaje));
const enfasis2 = crearMayus2(mensaje => console.log(mensaje));
//log("Hola mundo");
//log2("Hola mundo 2")
//mensajes[1](mensajes[0]);
//mensajes[3](mensajes[2]);
//dentroFn(mensaje => console.log(mensaje));
//enfasis("Las funciones pueden ser retornadas por otras funciones");
//enfasis("crearMayus retorna una funcion");
//enfasis("enfasis invoca la funcion retornada");
enfasis2("usa de la funcion tipo flechas");