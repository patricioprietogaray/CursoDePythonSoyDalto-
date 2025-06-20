# METODOS DUNDER O METODOS ESPECIALES

# https://youtu.be/HtKqSJX7VoM?t=9481
# 2.38.00

# _ _ metodo especial _ _ --> __init__ y un monton mas
# que es un metodo especial?
# los metodos especiales son los metodos que ya estan definidos por python y tampoco
# se pueden redefinir.

# Son funciones que tienen un nombre especial reservado.
# inician con dos guines bajos y terminan con dos guiones bajos.
# Estos métodos estan creados con la única finalidad 
# para crear funcionalidades especiales que con metodos normales no 
# podríamos 


class Persona:
    # método espacial: constructor (crea la clase Persona)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo especial: modo de texto
    # devuelve una representacion del objeto en 
    # una cadena de texto 
    # ej: Persona(nombre = Pato, edad = 25)
    def __str__(self):
        return f'Persona(nombre = {self.nombre}, edad = {self.edad})'
    
    
    # Si str no existe el resultado por pantalla es: 
    # # <__main__.Persona object at 0x7f38230136d0>
    # def __str__(self):
    #     return f'Persona(nombre = {self.nombre}, edad = {self.edad})'


    # reconstruir un objeto
    def __repr__(self):
        return f"Persona(nombre = '{self.nombre}', edad = {self.edad})"




class Es_Tupla:
    def __init__(self, dato1str, dato2int):
        self.dato1str = dato1str
        self.dato2int = dato2int
    
    def __str__(self):
        return (f'("Es tupla: Str:{self.dato1str}", Int:{self.dato2int})')

    # reconstruir un objeto
    def __repr__(self):
        return (f'("{self.dato1str}", {self.dato2int})')



pato = Persona('Pato', 25)
print(pato)

tupla = Es_Tupla('Pato', 25)
print(tupla)

patos = Persona('Patito', 15)

representacion = repr(tupla)
resultado = eval(representacion)
print(resultado[1]) # 25

repre = repr(patos) # Persona(nombre = 'Patito', edad = 15)
result = eval(repre) # Persona(nombre = Patito, edad = 15)
print(result)

# 2.43.00


# Aquí tienes una lista de los métodos especiales 
# (también conocidos como "métodos mágicos" 
# o "dunder methods" por el doble guion bajo que los rodea) en Python, 
# junto con una definición básica para cada uno:

# Métodos de Inicialización y Construcción

# __init__(self, ...): El constructor de la clase. 
# Se llama cuando se crea una nueva instancia del objeto. 
# Se utiliza para inicializar los atributos del objeto.

# __new__(cls, ...): 
# Un método de bajo nivel que se llama antes de __init__. 
# Se encarga de crear y devolver una nueva instancia del objeto. 
# Raramente se sobrescribe directamente a menos que se necesite 
# un control muy fino sobre la creación de instancias 
# (por ejemplo, para implementar singletons).

# __del__(self): 
# El destructor de la clase. 
# Se llama cuando una instancia del objeto está a punto de ser destruida 
# (cuando su conteo de referencias llega a cero). 
# Se usa para liberar recursos si es necesario.


# Métodos de Representación

# __repr__(self): 
# Retorna una representación "oficial" 
# (inequívoca) del objeto, útil para desarrolladores. 
# Idealmente, debería ser una cadena que, 
# si se evalúa, reconstruya el objeto.

# __str__(self): 
# Retorna una representación "informal" 
# (legible para humanos) del objeto. 
# Es lo que se muestra cuando usas print() o str() en el objeto.


# Métodos de Comparación

# __eq__(self, other): 
# Define el comportamiento del operador de igualdad ==.

# __ne__(self, other): 
# Define el comportamiento del operador de desigualdad !=.

# __lt__(self, other): 
# Define el comportamiento del operador "menor que" <.

# __le__(self, other): 
# Define el comportamiento del operador "menor o igual que" <=.

# __gt__(self, other): 
# Define el comportamiento del operador "mayor que" >.

# __ge__(self, other): 
# Define el comportamiento del operador "mayor o igual que" >=.


# Métodos de Atributos

# __getattr__(self, name): 
# Se llama cuando se intenta acceder a un atributo 
# que no existe normalmente en el objeto. 
# Permite definir un comportamiento para atributos dinámicos.

# __setattr__(self, name, value): 
# Se llama cuando se intenta asignar un valor a un atributo del objeto. 
# Permite interceptar y modificar la asignación de atributos.

# __delattr__(self, name): 
# Se llama cuando se intenta eliminar un atributo del objeto.

# __dir__(self): 
# Debería devolver una secuencia de cadenas con los nombres 
# de los atributos y métodos disponibles en el objeto. 
# Se utiliza por la función dir().

# __getattribute__(self, name): 
# Se llama siempre que se accede a un atributo, 
# independientemente de si existe o no. 
# Si se sobrescribe, debe llamarse a la implementación de la clase base 
# para evitar recursiones infinitas. Es más potente que __getattr__.

# Métodos de Contenedores (Emulación de Secuencias, Mapeos, etc.)

# __len__(self): 
# Define el comportamiento de la función len(). 
# Debe retornar la longitud del objeto.

# __getitem__(self, key): 
# Define el comportamiento de acceder a un elemento por índice o clave (ej. obj[key]).

# __setitem__(self, key, value): 
# Define el comportamiento de asignar un valor a un elemento 
# por índice o clave (ej. obj[key] = value).

# __delitem__(self, key): 
# Define el comportamiento de eliminar un elemento 
# por índice o clave (ej. del obj[key]).

# __contains__(self, item): 
# Define el comportamiento del operador in. 
# Debe retornar True si el item está en el objeto, False de lo contrario.

# __iter__(self): 
# Debe retornar un objeto iterador. 
# Se utiliza para hacer que un objeto sea iterable 
# (permitiendo su uso en bucles for).

# __next__(self): 
# Retorna el siguiente elemento del iterador. 
# Se utiliza en conjunción con __iter__ para la iteración.


# Métodos Aritméticos

# __add__(self, other): 
# Define el comportamiento del operador de suma +.

# __sub__(self, other): 
# Define el comportamiento del operador de resta -.

# __mul__(self, other): 
# Define el comportamiento del operador de multiplicación *.

# __truediv__(self, other): 
# Define el comportamiento del operador 
# de división verdadera / (división de punto flotante).

# __floordiv__(self, other): 
# Define el comportamiento del operador de división entera //.

# __mod__(self, other): 
# Define el comportamiento del operador de módulo %.

# __pow__(self, other): 
# Define el comportamiento del operador de potencia **.

# __and__(self, other): 
# Define el comportamiento del operador AND bit a bit &.

# __or__(self, other): 
# Define el comportamiento del operador OR bit a bit |.

# __xor__(self, other): 
# Define el comportamiento del operador XOR bit a bit ^.

# __lshift__(self, other): 
# Define el comportamiento del operador de desplazamiento a la izquierda <<.

# __rshift__(self, other): 
# Define el comportamiento del operador de desplazamiento a la derecha >>.



# Métodos Aritméticos Reflejados 
# (para operaciones donde el operando izquierdo no soporta la operación)

# __radd__(self, other): 
# Versión reflejada de __add__.

# __rsub__(self, other): 
# Versión reflejada de __sub__.

# ... y así sucesivamente para todos 
# los operadores aritméticos (__rmul__, __rtruediv__, etc.).



# Métodos Aritméticos de Asignación (para operaciones como +=, -=)

# __iadd__(self, other): 
# Define el comportamiento de la asignación con suma +=.

# __isub__(self, other): 
# Define el comportamiento de la asignación con resta -=.

# ... y así sucesivamente para todos 
# los operadores aritméticos (__imul__, __itruediv__, etc.).



# Métodos de Conversión de Tipos

# __int__(self): 
# Define el comportamiento de la función int().

# __float__(self): 
# Define el comportamiento de la función float().

# __complex__(self): 
# Define el comportamiento de la función complex().

# __bool__(self): 
# Define el comportamiento de la función bool(). 
# Debe retornar True o False. 
# Si no se define, Python usa __len__ (si existe y retorna cero para False) 
# o siempre True por defecto.


# Métodos de Contexto (para el uso de with statements)

# __enter__(self): 
# Se llama al entrar en el bloque with. 
# Debe retornar el objeto que se asignará a la variable as.

# __exit__(self, exc_type, exc_val, exc_tb): 
# Se llama al salir del bloque with. Maneja la limpieza y el manejo de excepciones.



# Métodos de Llamada (Callables)

# __call__(self, ...): 
# Permite que una instancia de una clase sea llamada como una función (ej. objeto()).



# Métodos de Hash

# __hash__(self): 
# Retorna un valor hash entero para el objeto. 
# Necesario para que un objeto pueda ser usado como clave 
# en un diccionario o elemento en un conjunto (set). 
# Si se define __eq__, se recomienda definir también __hash__.



# Métodos de Pickle

# __reduce__(self): 
# Proporciona la información necesaria para el 
# protocolo de "pickling" (serialización).


# Esta lista cubre la mayoría de los métodos especiales comunes 
# y esenciales en Python. 
# Comprenderlos te permite crear clases que interactúan de manera más 
# "Pythonica" con el lenguaje y sus funciones incorporadas.