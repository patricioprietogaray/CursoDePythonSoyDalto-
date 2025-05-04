# estudiar en python

# duck typing
# El "Duck Typing" o "tipado pato" en español, 
# es un concepto en programación que enfatiza el comportamiento 
# de un objeto sobre su tipo. En esencia, si un objeto tiene el 
# comportamiento necesario para una tarea, entonces se considera 
# que pertenece a esa categoría, incluso si no pertenece a una 
# clase específica. El nombre viene de la frase "Si parece un pato, 
# nada como un pato y grazna como un pato, entonces probablemente 
# sea un pato". 
class Pato:
    def graznar(self):
        return 'Grazna'
class Gato:
    def graznar(self):
        return 'No grazna'
class Perro:
    def graznar(self):
        return 'No grazna'
def hacer_graznar(instancia):
    return instancia.graznar()
pato = Pato()
gato = Gato()
perro = Perro()
print(hacer_graznar(pato))
print(hacer_graznar(gato))
print(hacer_graznar(perro))

# en este caso es mas importante el comportamiento (metodo graznar)
# que el tipo de objeto que es. (clase pato, gato o perro)

# enlaces dinámicos


# enlaces estáticos


# tipo real


# tipo declarado


