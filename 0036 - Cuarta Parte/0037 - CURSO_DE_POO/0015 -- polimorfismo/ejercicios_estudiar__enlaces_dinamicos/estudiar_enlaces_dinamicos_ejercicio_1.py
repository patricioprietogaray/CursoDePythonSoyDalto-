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



# Ejercicio 1
# Enunciado Simple (Resolución de Nombres): 
# Define una clase con un método. 
# Crea una instancia de la clase y llama al método utilizando 
# el nombre del método. 
# Explica cómo el intérprete de Python encuentra y 
# ejecuta este método en tiempo de ejecución.

# La parte que necesitas explicar en este primer enunciado 
# se centra en el proceso que sigue Python cuando haces algo 
# como mi_objeto.mi_metodo(). 
# Aquí te doy las ideas clave que deberías incluir en tu 
# explicación:
#   "Tiempo de Ejecución" es Crucial: 
# Subraya que este proceso ocurre mientras el programa 
# está corriendo, no antes.
# 
#   Búsqueda del Nombre: 
# Cuando el intérprete encuentra la línea mi_objeto.mi_metodo(), 
# lo primero que hace es buscar el nombre mi_metodo dentro 
# del objeto al que mi_objeto hace referencia.
# 
# ¿Dónde busca?
# 
#   Primero en el propio objeto: 
# Python mira si la instancia mi_objeto tiene un atributo 
# con el nombre mi_metodo. Esto podría ser un atributo de 
# datos o un método que se agregó directamente a la instancia 
# (aunque esto es menos común para métodos definidos en la clase).
# 
#   Luego en la clase del objeto: 
# Si no lo encuentra en la instancia, Python busca el 
# nombre mi_metodo en la definición de la clase a la que 
# pertenece mi_objeto. Los métodos se definen típicamente 
# a nivel de clase.
# 
#   Finalmente en la jerarquía de herencia: 
# Si la clase del objeto hereda de otras clases, 
# Python continúa buscando el nombre mi_metodo en las 
# clases padre, siguiendo el orden de resolución de 
# métodos (MRO - Method Resolution Order).
# 
#   "Encuentra" el Método: 
# Una vez que Python localiza un atributo con el 
# nombre mi_metodo que resulta ser un método 
# (una función ligada al objeto), sabe qué bloque de 
# código debe ejecutar cuando se llama al método.
# 
#   "Ejecuta" el Método: 
# Al encontrar el método, Python lo llama. 
# Esto implica ejecutar el bloque de código definido 
# dentro de la función del método. 
# Es importante mencionar que cuando un método de instancia 
# es llamado, la instancia del objeto 
# (mi_objeto en este caso) se pasa automáticamente 
# como el primer argumento al método (convencionalmente 
# llamado self dentro de la definición del método).
# 
#   En resumen, tu explicación debe destacar que Python 
# no sabe hasta el momento de ejecutar la línea de código 
# si mi_objeto tiene un método llamado mi_metodo y 
# dónde se encuentra su definición. 
# Esta búsqueda y vinculación (del nombre a la implementación) 
# ocurre dinámicamente durante la ejecución.

# class Perro:
#     def ladrar(self):
#         return 'El perro ladra!'

# firulais = Perro()
# print(firulais.ladrar())

# Tu explicación debería enfocarse en lo siguiente:
# Cuando el intérprete de Python llega a la línea 
# print(firulais.ladrar()):
# En ese momento (tiempo de ejecución): 
# Python examina el objeto al que hace referencia 
# la variable firulais.

# Busca el nombre ladrar: 
# Busca un atributo llamado ladrar dentro de ese objeto.
# Lo encuentra en la clase: 
# No lo encuentra como un atributo directamente en 
# la instancia firulais, pero lo encuentra como un 
# método definido en la clase Perro de la cual firulais 
# es una instancia.

# Vincula y ejecuta: 
# Python vincula el nombre ladrar con la implementación 
# del método en la clase Perro y luego ejecuta ese código. 
# La instancia firulais se pasa automáticamente como el 
# argumento self dentro del método.

# El resultado se imprime: 
# El valor retornado por el método ladrar() 
# ('El perro ladra!') es entonces pasado a la función print() 
# y se muestra en la consola.
# La clave es enfatizar que esta búsqueda y ejecución 
# ocurre paso a paso, en el momento en que se ejecuta 
# la línea de código, y no se decide de antemano 
# durante una fase de "compilación" como en lenguajes estáticos. 
# Python confía en que el objeto tendrá el atributo o 
# método solicitado cuando el código se ejecute.



# # EJEMPLO
# class Canto:
#     def sonar(self):
#         return "El pájaro está cantando."

# mi_pajaro = Canto()
# resultado = mi_pajaro.sonar()
# print(resultado)
# Explicación de cómo el intérprete de Python encuentra y 
# ejecuta el método sonar() en tiempo de ejecución:

# Cuando el intérprete de Python llega a la línea 
# resultado = mi_pajaro.sonar():

# Tiempo de Ejecución: Es crucial entender que este proceso 
# de búsqueda y ejecución ocurre mientras el programa 
# está corriendo, en el momento exacto en que se 
# alcanza esta línea de código. Python no determina 
# qué código ejecutar para mi_pajaro.sonar() hasta este instante.

# Búsqueda del Nombre: El intérprete toma la variable mi_pajaro 
# y busca el atributo con el nombre sonar dentro del objeto 
# al que mi_pajaro hace referencia.

# Búsqueda en la Clase: Python primero busca si la instancia 
# mi_pajaro tiene un atributo llamado sonar. En este caso, 
# sonar no es un atributo de datos directamente adjunto a la 
# instancia. Entonces, Python busca el nombre sonar en la definición 
# de la clase Canto a la que pertenece mi_pajaro.

# Encuentra el Método: El intérprete encuentra que sonar está 
# definido como un método (una función ligada a la clase Canto).

# Vinculación y Llamada: Python vincula el nombre sonar con la 
# implementación de la función sonar que pertenece a la 
# clase Canto. Cuando se llama al método utilizando los 
# paréntesis (), el intérprete ejecuta el bloque de código 
# definido dentro de la función sonar. Es importante destacar 
# que la instancia del objeto (mi_pajaro) se pasa automáticamente 
# como el primer argumento al método, que convencionalmente 
# se llama self dentro de la definición del método sonar.

# Ejecución del Método: El código dentro del método 
# sonar() (return "El pájaro está cantando.") se ejecuta.

# Retorno del Valor: El valor retornado por el método 
# sonar() (la cadena "El pájaro está cantando.") se asigna 
# a la variable resultado.

# Finalmente, la siguiente línea print(resultado) toma 
# el valor retornado y lo muestra en la consola.

# En resumen, Python, gracias al enlace dinámico, 
# no necesita saber en tiempo de "compilación" 
# (si es que se puede hablar de compilación en el mismo 
# sentido que en lenguajes estáticos) qué código se 
# ejecutará cuando se llame a mi_pajaro.sonar(). 
# La resolución del nombre sonar al método específico 
# en la clase Canto ocurre dinámicamente en el momento 
# en que se ejecuta la línea de código. Esta flexibilidad 
# es una característica fundamental del enlace dinámico en Python.






# Ejercicio 1
# Enunciado Simple (Resolución de Nombres): 
# Define una clase con un método. 
# Crea una instancia de la clase y llama al método utilizando 
# el nombre del método. 
# Explica cómo el intérprete de Python encuentra y 
# ejecuta este método en tiempo de ejecución.

class Niebla:
    def __init__(self, visibilidad):
        self.visibilidad = visibilidad
        
    def vision(self):
        if self.visibilidad <= 30:
            print('No se ve un pomo, la niebla es mayor al 70%')
        elif self.visibilidad >= 31 and self.visibilidad <= 70:
            print('Poca visibilidad, la niebla es mayor al 30% y menor que el 70%')
        else:
            print('La visibilidad es aceptable, la niebla es menor al 30%')
 
niebla_en_el_suelo = Niebla(50)
niebla_en_el_suelo.vision()

# explicacion
# Se instancia en la variable niebla_en_el_suelo la clase Niebla
# y se le pasa el argumento 50.
# Se inicializa la clase y se le pasa 50 como argumento y
# este dato es recibido por el método __init__ y se carga
# a la variable local de la clase. 
# Quedando self.visibilidad con un valor de 50.
# Sigue en la proxima linea de comandos
# Por medio de niebla_en_el_suelo se llama al método vision().
# El método visión evaluará el valor del self.visibilidad
# Según su valor se imprimirá un mensaje.
# En este caso como tiene valor 50
# el mensaje será: 
# 'Poca visibilidad, la niebla es mayor al 30% y menor que el 70%'
# El mismo se imprime y se da por concluido el programa
# .
        
# CORRECION}
# Explicación de cómo el intérprete de Python encuentra 
# y ejecuta el método vision() en tiempo de ejecución:

# Tiempo de Ejecución: Es fundamental entender que el 
# proceso de encontrar y ejecutar el método vision() 
# ocurre mientras el programa está en funcionamiento, 
# precisamente cuando se alcanza la línea 
# niebla_en_el_suelo.vision(). Python no determina de antemano 
# qué código se ejecutará para esta llamada.

# Búsqueda del Nombre: Cuando el intérprete de Python 
# encuentra la expresión niebla_en_el_suelo.vision(), 
# lo primero que hace es buscar el nombre vision dentro 
# del objeto al que hace referencia la variable 
# niebla_en_el_suelo.

# Búsqueda en la Clase: Python primero verifica si la 
# instancia niebla_en_el_suelo tiene un atributo llamado 
# vision directamente asociado a ella. En este caso, 
# vision no es un atributo de datos de la instancia. 
# Entonces, el intérprete busca el nombre vision en la 
# definición de la clase Niebla a la que pertenece 
# niebla_en_el_suelo.

# Encuentra el Método: Python localiza que vision está definido 
# como un método (una función ligada a la clase Niebla).

# Vinculación y Llamada: El intérprete vincula el nombre vision 
# con la implementación de la función vision dentro de la 
# clase Niebla. Al encontrar los paréntesis (), 
# Python sabe que debe ejecutar este método. En este momento, 
# la instancia del objeto (niebla_en_el_suelo) se pasa 
# automáticamente como el primer argumento al método vision, 
# que dentro de la definición del método se conoce como self.

# Ejecución del Método: El código dentro del método vision() 
# se ejecuta, utilizando el valor del atributo self.visibilidad 
# (que se estableció en 50 durante la inicialización del objeto). 
# Las condicionales if/elif/else evalúan este valor y se ejecuta 
# la instrucción print() correspondiente.

# En resumen para el enlace dinámico: Python no determina la 
# implementación del método vision() que se va a ejecutar 
# hasta el momento en que se llama. Busca el nombre vision en 
# el objeto y su clase en tiempo de ejecución y luego vincula 
# esa llamada con el código del método definido en la clase Niebla. 
# Esta resolución tardía es la esencia del enlace dinámico en Python.

# Tu explicación inicial era buena para describir el flujo del programa, 
# pero para el ejercicio específico sobre enlace dinámico, 
# es importante enfocar la explicación en cómo Python encuentra 
# y vincula el nombre del método a su implementación durante la ejecución.
        
        
        
        
        
        
        
# vamos de nuevo
# Creá un "molde" para hacer algo (una clase). 
# Imaginate que este molde dice qué cosas puede hacer un objeto 
# que se haga con él. Por ejemplo, un molde para un "Hablar" 
# que tenga la capacidad de "decir algo".

class Humano:
    def hablar(self):
        print('Estoy hablando')

# Hacé un objeto usando ese molde (una instancia). 
# Es como si usaras el molde "Hablar" para crear un 
# objeto específico, digamos, un "Pájaro".

pepe = Humano()

# Decile a ese objeto que haga algo que sabe hacer (llama al método). 
# Le decís al "Pájaro": "¡Decí algo!".
pepe.hablar()

# Ahora, la parte importante que tenés que explicar es: 
# ¿cómo hace Python para saber qué significa "¡Decí algo!" 
# para ese "Pájaro" en el momento en que se lo pedís?

# Pensalo así:

# Vos escribís el código. Python lo lee.

# # # Python lee todo el codigo que he escrito
# # # Cuando pepe quiere hablar pepe.hablar() python no tiene idea que es eso
# # # En tiempo de ejecución (lenguaje de enlace dinamico o interpretado, 
# # # mientras el programa se ejecuta en el ordenador):
# # #   Encuentra el objeto pepe (instancia) e indaga si pepe sabe "hablar()"
# # #   Busca en la clase y luego en el método hablar() y verifica si hay una 
# # #   instuccion que exista
# # #   Python ejecuta la instrucción que se encuentra
# # #   dentro del método hablar()  
# # #   python sabe que hacer ->  imprime por pantalla un mensaje: "Estoy hablando".
###     En definitiva esto es el "enlace dinámico": 
# # #   la conexión entre la orden ("hablar") y lo que realmente 
# # #   se hace ("Estoy hablando") se establece dinámicamente,
# # #   durante la ejecución del programa.


# Cuando llega a la parte donde le decís al "Pájaro" que "diga algo", 
# Python no tiene una lista prearmada de qué significa "decir algo" 
# para cada cosa que existe en tu programa.
# Lo que hace Python en ese momento (en "tiempo de ejecución", 
# o sea, mientras el programa está corriendo):
# Mira al objeto "Pájaro". Dice: "A ver, ¿tú sabes cómo 'decir algo'?" 
# Busca en el "molde" del "Pájaro" (la clase). 
# Va a la definición del "molde" "Hablar" para ver si ahí hay una instrucción 
# de qué hacer cuando alguien le dice a un objeto de ese tipo que "diga algo".

# Encuentra la instrucción. Si en el molde "Hablar" hay una parte 
# que dice que "decir algo" significa mostrar un mensaje 
# como "¡Pío pío!", entonces Python sabe qué hacer.

# Ejecuta la instrucción. Python agarra esa instrucción ("¡Pío pío!") 
# y la muestra en la pantalla.

# La clave es que Python no hace esta búsqueda de 
# "¿qué significa 'decir algo' para un Pájaro?" 
# hasta el momento exacto en que se lo pedís en el programa. 
# No lo decide antes de empezar a correr el programa. 
# Esto es el "enlace dinámico": 
# la conexión entre la orden ("decir algo") 
# y lo que realmente se hace ("¡Pío pío!") se establece dinámicamente, 
# durante la ejecución del programa.

# Tu tarea en el ejercicio es explicar este proceso usando el código que escribas. 
# Tenés que mostrar cómo creás el molde (la clase), el objeto (la instancia) 
# y cómo le pedís que haga algo (llamas al método). 
# Y luego, contá cómo Python hace para encontrar la acción correcta en ese momento.

# ¿Se entiende un poco mejor ahora? ¡No dudes en preguntar si hay alguna parte que todavía no quede clara!






# FINAL DEL EJERCICIO EJERCICIO RESUELTO

class Humano:
    def hablar(self):
        print('Estoy hablando')

pepe = Humano()
pepe.hablar()



# # # Python lee todo el codigo que he escrito lo tiene en memoria pero no lo interpreta.
# # # Cuando pepe quiere hablar pepe.hablar() python no tiene idea que es eso
# # # En tiempo de ejecución (lenguaje de enlace dinamico o interpretado,
# # # mientras el programa se ejecuta en el ordenador):
# # # Encuentra el objeto pepe (instancia) e indaga si pepe sabe "hablar()"
# # # Busca en la clase y luego en el método hablar() y verifica si hay una
# # # instuccion que exista
# # # Python ejecuta la instrucción que se encuentra
# # # dentro del método hablar()
# # # python sabe que hacer -> imprime por pantalla un mensaje: "Estoy hablando".
### En definitiva esto es el "enlace dinámico":
# # # la conexión entre la orden ("hablar") y lo que realmente
# # # se hace ("Estoy hablando") se establece dinámicamente,
# # # durante la ejecución del programa.

# ¡Exacto! ¡Entendiste perfectamente el concepto!

# Tu explicación es clara y precisa. Capturaste la esencia de cómo Python maneja la llamada a un método en tiempo de ejecución.

# Resaltaste correctamente los puntos clave:

# Python lee el código pero la "acción" ocurre al ejecutar.
# Cuando llamas a pepe.hablar(), Python no tiene una idea predefinida de qué significa hablar() para pepe hasta ese momento.
# En tiempo de ejecución, busca en el objeto y su clase la definición del método.
# Una vez que la encuentra, ejecuta las instrucciones dentro de ese método.
# Y finalmente, definiste muy bien el "enlace dinámico" como esa conexión que se establece justo en el momento de la ejecución.
# ¡Excelente! Con esta comprensión, estás listo para explicar el "cómo" del enlace dinámico en tu solución del Ejercicio 1. ¡Muy bien! ¿Pasamos al siguiente enunciado o quieres repasar algo más de este?
