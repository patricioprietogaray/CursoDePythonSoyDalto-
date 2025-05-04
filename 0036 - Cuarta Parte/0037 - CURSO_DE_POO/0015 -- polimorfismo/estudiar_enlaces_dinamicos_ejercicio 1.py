# En Python, el concepto de "enlace dinámico" se refiere principalmente a 
# cómo el intérprete de Python resuelve los nombres de los métodos y atributos 
# de un objeto en tiempo de ejecución, en lugar de en tiempo de compilación 
# (como sucede en lenguajes compilados con tipado estático).

# A diferencia de lenguajes como C++ o Java, donde la vinculación de una 
# llamada a un método con la implementación específica del método 
# a menudo se decide durante la compilación (enlace estático), 
# Python realiza esta vinculación en el momento en que el código se está ejecutando.

# Características clave del enlace dinámico en Python:

# Resolución de nombres en tiempo de ejecución: 
# Cuando llamas a un método en un objeto (por ejemplo, objeto.metodo()), 
# el intérprete de Python busca el método "metodo()" dentro del objeto y 
# su jerarquía de clases en el momento en que esa línea de código se ejecuta.

# Flexibilidad y Duck Typing: 
# El enlace dinámico es fundamental para el "duck typing" en Python. 
# Como el tipo de un objeto no se verifica estrictamente en tiempo de compilación, 
# el intérprete espera hasta la ejecución para asegurarse de que el objeto realmente 
# tenga el método o atributo al que se está intentando acceder. 
# Si el objeto tiene un método con el nombre correcto, se llamará, 
# independientemente de su tipo o herencia.



# Facilidad para la modificación en tiempo de ejecución: 
# Debido al enlace dinámico, es posible modificar la estructura de los objetos 
# y las clases (agregar, eliminar o reemplazar métodos y atributos) incluso 
# mientras el programa se está ejecutando. Esto permite una gran flexibilidad y 
# metaprogramación.

# A TENER EN CUENTA:
# MODIFIQUE EL CODIGO MIENTRAS SE HACIA UN BUCLE Y EL PRINT NO CAMBIO....

# ¡Ah, entiendo perfectamente lo que experimentaste! 
# Lo que observaste no es una falla del enlace dinámico en sí, 
# sino más bien cómo funciona la ejecución de scripts en Python 
# y cómo tu entorno de desarrollo (probablemente VS Code u otro editor) 
# interactúa con el intérprete.

# En resumen, Python no "recarga" automáticamente los archivos de código fuente 
# que ya están en memoria mientras un script se está ejecutando. 
# Para que los cambios en el archivo tengan efecto, necesitas detener la ejecución actual 
# y volver a ejecutar el script.

# Esto no contradice el concepto de enlace dinámico. 
# El enlace dinámico se refiere a que la resolución de 
# los nombres de los métodos y atributos ocurre en tiempo de ejecución. 
# Sin embargo, la definición de las clases y funciones en sí misma 
# se carga cuando el intérprete inicia la ejecución del script.
# Tu experimento ilustra perfectamente la diferencia entre 
# la carga inicial del código y la ejecución posterior. ¡Buena observación!


# Reflexión: 
# El enlace dinámico facilita la reflexión, que es la capacidad de un programa 
# para examinar y manipular su propia estructura 
# (clases, métodos, atributos) en tiempo de ejecución. 
# Funciones como getattr(), setattr(), hasattr(), dir() 
# y el módulo inspect se basan en esta capacidad.

# Ejemplo para ilustrar el enlace dinámico y el duck typing:

# Python

# class Pato:
#     def volar(self):
#         print("El pato está volando.")

# class Avion:
#     def volar(self):
#         print("El avión está volando.")

# def hacer_volar(algo_que_vuela):
#     algo_que_vuela.volar()

# p = Pato()
# a = Avion()

# hacer_volar(p)  # En tiempo de ejecución, se encuentra el método volar en Pato.
# hacer_volar(a)  # En tiempo de ejecución, se encuentra el método volar en Avion.

# # Si intentáramos pasar un objeto sin el método volar:
# class Roca:
#     pass

# r = Roca()
# # hacer_volar(r)  # Esto generaría un AttributeError en tiempo de ejecución.
# En este ejemplo, la función hacer_volar no verifica 
# el tipo de algo_que_vuela en tiempo de compilación. 
# Solo en el momento de la ejecución intenta llamar al método volar(). 
# Si el objeto tiene ese método, la llamada se realiza con éxito. 
# Si no, se produce un error en tiempo de ejecución.

# En resumen, el enlace dinámico en Python significa que la resolución 
# de nombres (de métodos y atributos) ocurre durante la ejecución del programa. 
# Esto proporciona una gran flexibilidad, permite el duck typing y 
# facilita la metaprogramación y la reflexión. 
# Es una de las características fundamentales que definen la naturaleza 
# dinámica del lenguaje Python.