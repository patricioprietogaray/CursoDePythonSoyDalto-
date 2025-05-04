#  https://lathack.com/ejercicios-en-python-poo/

# Ejercicio 1
# Realizar un programa que conste de una clase llamada Estudiante, 
# que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y 
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante:
    # atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    # metodo        
    def imprimir(self):
        print(f"\nAlumno: {self.nombre}\nNota: {self.nota}")
    
    def aprobado(self):
        if self.nota >= 7.0:
            print(f"El alumno {self.nombre} ha aprobado con {self.nota}. Felicidades!!!")
        else:
            print(f"El alumno {self.nombre} ha desaprobado con {self.nota}. Debes Recursar.")


nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese su nota: "))

estudiante_1 = Estudiante(nombre, nota)
estudiante_1.imprimir()
estudiante_1.aprobado()


# Ejercicio 2
# Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un método “cumpleaños”, que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”.
# Tendríamos que lograr ejecutar el siguiente código con la clase creada:

# p=Persona(«Nombre», edad)
# p.cumpleaños()
# print(f»{p.nombre} cumple {p.edad} años»)


# Ejercicio 3
# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.




# Ejercicio 4
# Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto:
# En la clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido. Además, esta clase , debe tener un método para mostrar nombre_completo() el cual debe mostrar el nombre acompañado del apellido.
# La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir los argumentos nombre y edad. También la clase “Estudiante”, recibe el valor “carrera”, y además contar con un método mostrar_carrera(). Las dos clases son obligatorias.




# Ejercicio 5
# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
# Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.



# Ejercicio 6
# Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga «Hola, soy un animal marino!». Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por «Hola soy un Pulpo!».
# Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parámetro.



# Ejercicio 7
# Desarrollar un programa con tres clases:
# La primera debe ser Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.











