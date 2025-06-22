# El polimorfismo orientado al "duck typing" en Python 
# es un concepto poderoso y fundamental que permite que objetos de diferentes 
# clases sean tratados de manera uniforme 
# **siempre y cuando implementen los métodos y atributos necesarios**, 
# sin importar su herencia o tipo explícito.

# La frase clave aquí es: 
# **"Si camina como un pato y grazna como un pato, entonces es un pato."** 
# De ahí viene el nombre "duck typing".

# **En esencia, Python no se preocupa por el tipo de un objeto, sino por su comportamiento.** 
# Si un objeto tiene los métodos que se esperan en un contexto determinado, 
# Python lo tratará como si fuera del tipo esperado, aunque no lo sea formalmente.

# **Características Clave del Duck Typing en Python:**

# 1.  **No se basa en la herencia o interfaces explícitas:** 
# A diferencia de otros lenguajes donde el polimorfismo a menudo se logra 
# a través de la herencia de una clase base o la implementación 
# de una interfaz, en Python, dos objetos pueden ser tratados 
# polimórficamente si ambos tienen un método con el mismo nombre 
# y que realiza una acción similar, incluso si sus clases no están relacionadas.

# 2.  **Énfasis en el comportamiento (métodos y atributos):** 
# Lo que importa es si un objeto puede "hacer" lo que se espera de él. 
# Si un objeto tiene un método llamado `hablar()` que imprime un sonido, 
# puede ser usado en cualquier lugar donde se espere algo que pueda "hablar", 
# sin importar si es un perro, un gato o un loro.

# 3.  **Flexibilidad y dinamismo:** 
# Esto hace que el código en Python sea muy flexible y dinámico. 
# Puedes trabajar con objetos de diferentes clases de manera 
# intercambiable siempre que cumplan con los requisitos de comportamiento 
# en un contexto dado.

# **Ejemplo Ilustrativo:**

# Imagina que tienes una función que necesita interactuar con objetos que 
# pueden "hablar":

# # ```python
# def hacer_hablar(animal):
#     animal.hablar()

# class Pato:
#     def hablar(self):
#         print("¡Cuac!")

# class Perro:
#     def hablar(self):
#         print("¡Guau!")

# class Robot:
#     def hablar(self):
#         print("¡Bleep bloop!")

# pato = Pato()
# perro = Perro()
# robot = Robot()

# hacer_hablar(pato)  # Imprime: ¡Cuac!
# hacer_hablar(perro) # Imprime: ¡Guau!
# hacer_hablar(robot) # Imprime: ¡Bleep bloop!
# # ```

# En este ejemplo:

# * La función `hacer_hablar` no verifica el tipo de `animal`.
# * Simplemente asume que el objeto pasado como `animal` tiene un método 
# llamado `hablar()`.
# * Las clases `Pato`, `Perro` y `Robot` son completamente 
# independientes entre sí (no hay herencia común relacionada con "hablar").
# * Sin embargo, como los tres objetos tienen el método `hablar()`, 
# la función `hacer_hablar` puede trabajar con ellos polimórficamente.

# **Ventajas del Duck Typing:**

# * **Mayor flexibilidad:** Permite trabajar con objetos de diferentes 
# clases sin necesidad de una jerarquía de herencia rígida.

# * **Menor acoplamiento:** Las clases no necesitan estar explícitamente 
# relacionadas, lo que reduce las dependencias en el código.

# * **Reutilización de código:** Las funciones pueden ser más genéricas 
# y trabajar con una variedad más amplia de objetos.

# * **Desarrollo más rápido:** A menudo es más rápido prototipar 
# y desarrollar sin tener que definir una estructura de 
# tipos compleja desde el principio.

# **Consideraciones:**

# * **Posibles errores en tiempo de ejecución:** 
# Si un objeto se pasa a una función que espera un cierto comportamiento 
# (ciertos métodos), pero ese objeto no implementa esos métodos, 
# se producirá un error en tiempo de ejecución (AttributeError).

# * **Menor verificación estática:** 
# A diferencia de los lenguajes con tipado estático, 
# los errores de tipo relacionados con el comportamiento pueden 
# no detectarse hasta que se ejecuta el código.

# **En resumen, el polimorfismo orientado al duck typing en Python 
# es una forma poderosa y flexible de lograr el polimorfismo 
# al enfocarse en el comportamiento de los objetos en lugar 
# de su tipo explícito. 
# Permite escribir código más genérico y adaptable, 
# aunque requiere una cuidadosa consideración para evitar errores 
# en tiempo de ejecución.**

# Aquí tienes 5 enunciados para trabajar con polimorfismo (duck typing) en Python, 
# ordenados de menor a mayor complejidad:



# Enunciado Intermedio: Crea dos clases: 
# Coche con un método acelerar() y Bicicleta con un método pedalear(). 
# Escribe una función llamada mover que acepte un objeto 
# y, si este objeto tiene un método llamado avanzar(), 
# lo llama. Modifica las clases Coche y Bicicleta para que
# ambas tengan un método avanzar() que realice la acción apropiada 
# (usando los nombres originales de los métodos internamente). 
# Demuestra cómo la función mover puede trabajar con ambas clases.

class Coche:
    def acelerar(self):
        return 'El coche se mueve hacia adelante.'
    
    def avanzar(self):
        # return 'El coche avanza!!!'
        # llamo a acelerar
        return self.acelerar()

class Bicicleta:
    def pedalear(self):
        return 'La bicicleta se mueve hacia adelante.'

    def avanzar(self):
        # return 'La bicicleta avanza!!!'
        # llamo a pedalear
        return self.pedalear()

def mover(objeto):
    # para saber si tiene el atributo avanzar()
    if hasattr(objeto,'avanzar'):
        return objeto.avanzar()
    else:
        return f'{objeto} no posee el metodo "avanzar()"'

auto = Coche()
bici = Bicicleta()

print(mover(auto))
print(mover(bici))

# Esta modificación cumple exactamente con la sugerencia de que el método avanzar() 
# utilice internamente los métodos específicos de cada clase (acelerar() para Coche 
# y pedalear() para Bicicleta).

# Ahora, la función mover() puede trabajar con ambos objetos llamando a su método 
# avanzar(), y cada objeto realizará la acción de "avanzar" de la manera que le 
# corresponde, utilizando su lógica interna.




