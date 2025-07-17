class Saludar:
    def __call__(self, nombre):
        return f"Hola, {6*nombre}!"



s = Saludar()
print(s(5))