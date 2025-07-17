const persona = {
    nombre: "Daniela",
    caminar: function(){},
    hablar(){}
};

persona.caminar();
persona['nombre'] = 'Alejandra';

const nombreobjectivo = 'nombre';
persona[nombreobjectivo.value] = "Patricia";