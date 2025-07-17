const Suma = operacion =>  n => {
    operacion(n+2);
};

const op = Suma (n => {console.log(n*3)});

op(1);

