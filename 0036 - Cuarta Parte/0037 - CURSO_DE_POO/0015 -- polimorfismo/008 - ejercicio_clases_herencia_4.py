# ejemplo
# Concepto 2: Clases y Herencia

# La herencia permite que una clase (llamada subclase o clase derivada) herede atributos y métodos de otra clase (llamada superclase o clase base). Esto 1  promueve la reutilización de código.   
# 1.
# github.com
# github.com

# Ejercicio de Ejemplo: Herencia con Vehiculo y Coche

# Python

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.marca} {self.modelo} está encendido."
        return f"El {self.marca} {self.modelo} ya estaba encendido."

    def apagar(self):
        if self.encendido:
            self.encendido = False
            return f"El {self.marca} {self.modelo} está apagado."
        return f"El {self.marca} {self.modelo} ya estaba apagado."

class Coche(Vehiculo): # Coche hereda de Vehiculo
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo) # Llama al constructor de la clase base
        self.numero_puertas = numero_puertas

    def tocar_bocina(self):
        return "¡Pip pip!"

    # Sobrescribimos el método encender de la clase base
    def encender(self):
        estado_base = super().encender()
        if self.encendido:
            return f"{estado_base} ¡Listo para conducir con {self.numero_puertas} puertas!"
        return estado_base


class Moto(Vehiculo): # Moto hereda de Vehiculo
    def __init__(self, marca, modelo, tipo_cadena):
        super().__init__(marca, modelo)
        self.tipo_cadena = tipo_cadena

    def hacer_wheelie(self):
        if self.encendido:
            return f"¡La {self.marca} {self.modelo} está haciendo un wheelie con su cadena tipo {self.tipo_cadena}!"
        return f"La {self.marca} {self.modelo} debe estar encendida para hacer un wheelie."


# Crear objetos
mi_vehiculo = Vehiculo("Genérico", "V1")
mi_coche = Coche("Toyota", "Corolla", 4)
mi_moto = Moto("Yamaha", "MT-07", "Reforzada")

print(mi_vehiculo.encender())
print(mi_coche.encender())
print(mi_coche.tocar_bocina())
print(f"Mi coche tiene {mi_coche.numero_puertas} puertas.")
print(mi_moto.encender())
print(mi_moto.hacer_wheelie())
print(mi_moto.apagar())
