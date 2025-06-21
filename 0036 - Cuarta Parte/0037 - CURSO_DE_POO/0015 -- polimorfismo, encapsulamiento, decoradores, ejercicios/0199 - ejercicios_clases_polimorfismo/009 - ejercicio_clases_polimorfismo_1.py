# Concepto 3: Clases y Polimorfismo

# El polimorfismo (muchas formas) permite que objetos de diferentes 
# clases respondan al mismo mensaje 
# (llamada a método) de manera diferente. 
# Generalmente se logra a través de la herencia y la sobrescritura de métodos.

# Ejercicio de Ejemplo: Polimorfismo con InstrumentoMusical

# Python

class InstrumentoMusical:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar_melodia(self, melodia):
        raise NotImplementedError("Cada instrumento debe implementar este método")

    def afinar(self):
        return f"Afinando el instrumento: {self.nombre}"

class Guitarra(InstrumentoMusical):
    def tocar_melodia(self, melodia):
        return f"Guitarra {self.nombre} tocando la melodía '{melodia}' con acordes."

    def cambiar_cuerdas(self):
        return f"Cambiando cuerdas de la guitarra {self.nombre}."

class Piano(InstrumentoMusical):
    def tocar_melodia(self, melodia):
        return f"Piano {self.nombre} tocando la melodía '{melodia}' con teclas."

    def limpiar_teclas(self):
        return f"Limpiando las teclas del piano {self.nombre}."

class Violin(InstrumentoMusical):
    def tocar_melodia(self, melodia):
        return f"Violín {self.nombre} tocando la melodía '{melodia}' con arco y cuerdas."

    def aplicar_resina_arco(self):
        return f"Aplicando resina al arco del violín {self.nombre}."


# Lista de instrumentos
instrumentos = [
    Guitarra("Criolla"),
    Piano("De cola"),
    Violin("Stradivarius"),
    Guitarra("Eléctrica")
]

# Polimorfismo en acción
melodia_prueba = "Estrellita dónde estás"
for instrumento in instrumentos:
    print(instrumento.afinar())
    print(instrumento.tocar_melodia(melodia_prueba)) # Mismo método, diferente comportamiento
    if isinstance(instrumento, Guitarra): # Comprobación de tipo para métodos específicos
        print(instrumento.cambiar_cuerdas())
    elif isinstance(instrumento, Piano):
        print(instrumento.limpiar_teclas())
    print("-" * 20)