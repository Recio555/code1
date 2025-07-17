var log = function(mensaje){
    console.log(mensaje + " desde log");
};
var log2 = mensaje =>{
    console.log(mensaje + " dese log2");
};

const mensajes = [
    "Puede ser incertado en arreglos",
    log,
    log("Hola mundo"),
    log2  
];

const dentroFn = ingreso =>{
    ingreso("Puede ser enviados como argumentos a otras funciones");
};


//log("Hola mundo");
//log2("Hola mundo 2")
mensajes[1](mensajes[0]);
mensajes[3](mensajes[0]);
//dentroFn(mensaje => console.log(mensaje));