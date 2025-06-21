class Perro:
    # Atributo de clase (compartido por todas las instancias)
    reino = "Animal"

    # Constructor: se llama al crear un objeto de la clase
    def __init__(self, nombre, raza):
        # Atributos de instancia (propios de cada objeto)
        self.nombre = nombre
        self.raza = raza
        self.energia = 100 # Energía inicial

    # Método de instancia
    def ladrar(self):
        if self.energia >= 10:
            self.energia -= 10
            return f"¡Guau! Soy {self.nombre} y me quedan {self.energia} de energía."
        else:
            return f"{self.nombre} está demasiado cansado para ladrar."

    def alimentar(self, cantidad_comida):
        self.energia += cantidad_comida * 5 # Cada unidad de comida da 5 de energía
        if self.energia > 150:
            self.energia = 150 # Límite máximo de energía
        return f"{self.nombre} ha comido y ahora tiene {self.energia} de energía."

# Crear objetos (instancias) de la clase Perro
mi_perro1 = Perro("Fido", "Labrador")
mi_perro2 = Perro("Luna", "Chihuahua")

# Acceder a atributos y llamar a métodos
print(f"{mi_perro1.nombre} es un {mi_perro1.raza} del reino {Perro.reino}.")
print(mi_perro1.ladrar())
print(mi_perro1.alimentar(10))
print(mi_perro2.ladrar())
print(mi_perro2.alimentar(5))
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar())
print(mi_perro1.ladrar()) # Fido se cansará