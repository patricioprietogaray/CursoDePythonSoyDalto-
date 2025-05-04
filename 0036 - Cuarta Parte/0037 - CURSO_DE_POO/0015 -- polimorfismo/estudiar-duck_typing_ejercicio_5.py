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


# Enunciado Complejo con Interacción: 
# Define dos clases: 
# Canino con un método ladrar() y 
class Canino:
    def ladrar(self):
        return f'El canino esta ladrando...'
    def emitir_sonido(self):
        return self.ladrar()
    def mover_cola(self):
        return 'El canino mueve la cola...'

# Felino con un método maullar(). 
class Felino:
    def maullar(self):
        return f'El felino esta maullando...'
    def emitir_sonido(self):
        return self.maullar()
# Crea una función llamada interactuar_con_mascota que tome un objeto. 
# Si el objeto tiene un método llamado emitir_sonido(), lo llama. 
def interactuar_con_mascota(objeto):
    if hasattr(objeto, 'emitir_sonido'):
        print(objeto.emitir_sonido())
    else:
        print(f'No existe el método "emitir_sonido()" en {type(objeto).__name__}.')

    if hasattr(objeto, 'mover_cola'):
        print(objeto.mover_cola())
    else:
        print(f'No existe el método "mover_cola()" en {type(objeto).__name__}.')

# Además, si tiene un método llamado mover_cola(), también lo llama. 
# Modifica las clases Canino y Felino para que implementen estos métodos 
# de manera apropiada (solo Canino debería tener una implementación 
# significativa para mover_cola()). 
# Demuestra cómo la función interactuar_con_mascota 
# se comporta de manera diferente según el tipo de mascota, 
# basándose en los métodos que implementan.

# terminal demostracion
can = Canino()
fel = Felino()
interactuar_con_mascota(fel)
interactuar_con_mascota(can)






