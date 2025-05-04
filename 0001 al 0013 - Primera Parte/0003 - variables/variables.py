print("Variables string")

# las variables primero se definen y luego se asignan
# defino_variable = "valor_asignado"
# las variables se pueden cambiar de asignación en cualquier
# momento.

nombre = "Patricio"

# como ya está definida o declarada asigno un valor a la 
# variable nombre. Ahora el valor de la variable es Sebastián
# redefino la variable (se cambia de valor)

nombre = "Sebastián"


# muestro por pantalla el último valor asignado a 
# la variable nombre (el primer valor "Patricio" es reemplazado
# por Sebastián).

print(nombre)

# minuto 40

print("---------------------------------------------")
print(" ")
print(" Variables numéricas")
# numeros enteros
print(40)
numero=20
print(numero)



num1=20
num2=40
suma=num1+num2
# print("la suma entre "+str(num1)+" y "+str(num2)+" es: "+str(suma))
print(suma)

print("---------------------------------------------")
print(" ")
print("adición")
# defino una variable llamada numero1 en 10
# incremento en 1 a la variable numero1
# el más delante del igual significa: Che el valor que ya tiene (numero1) le sumo 1


numero1 = 10
numero1 += 1
print(numero1)


print("---------------------------------------------")
print(" ")
print("sustracción")
# tambien se puede restar
# el menos adelante significa que el valor que tengo se le reste x unidades
numero2 = 10
numero2 -= 1
print(numero2)

print("---------------------------------------------")
print(" ")
print("Forma 1 :concatenar strings o caracteres")
mensaje1="Hola"
nombre="Patricio"
mensaje2="¿Cómo estas?"
bienvenida = mensaje1 + ", " + nombre + ", " +mensaje2
print(bienvenida)
print(" ")
print("Forma 2 :concatenar strings o caracteres")
bienvenida = "Hola " + nombre +", ¿Cómo estás????"
print(bienvenida)



print("---------------------------------------------")
print(" ")
titulo = "concatenar strings o caracteres con 'f String' + datos:"
# print("concatenar strings o caracteres con f'\"{dato}\"')
mensaje01="Hola"
nombre01=3.14159
mensaje02="¿Cómo estas?"

# concatenar con f-strings
parrafo = f"{titulo} {mensaje01} {nombre01}, {mensaje02}"

print(parrafo)


# Aquí, se elimina la variable parrafo de la memoria. 
# Esto significa que parrafo ya no podrá usarse después de esta línea.
del parrafo

# concatenar con +
titulo = "concatenar strings o caracteres con '+': "
bienvenida = titulo + "Hola " + "Pato" + "!!!!!"
print(bienvenida)

# bienvenida = "{mensaje01} {nombre01}! {mensaje02}"
# muestra: {mensaje01} {nombre01}! {mensaje02}


# mostrar su valor poniendo una f antes de las comillas
# bienvenida = f"{mensaje01} {nombre01}! {mensaje02}"
# print(bienvenida)

# 46 minutos

# COMENTARIO: EL INTERPRETE DE PYTHON NO LO TIENE EN CUENTA

# Operadores de pertenencia
# Este tipo de operadores evalúan si un objeto pertenece a otro. 
# Hay dos: in y not in, que es el complementario del anterior. 
# El primero (in) devuelve True cuando el elemento pertenece al segundo. 
# Por ejemplo, si estamos utilizando cadenas de texto:

# che, ¿Data esta en el texto? (True)
pertenencia="Data" in "Python aplica en Data Science"
print(pertenencia)
# che, ¿Data no esta en el texto? (False)
pertenencia="Data" not in "Python aplica en Data Science"
print(pertenencia)

texto = "Python use for data science"
buscar = "use"
buscar1 = "Use"
print(f"Buscar use en {texto}: ")
print(buscar in texto)

# python es sencible a las minusculas y mayúsculas, es un lenguaje CaseSensitive
# 
# Case sensitive 
# es una expresión utilizada en informática que se aplica 
# a todos los textos en los que tiene importancia escribir 
# un carácter en mayúsculas o minúsculas
print(f"Buscar Use en {texto}:")
print(buscar1 in texto)


# formato camel case o camelCase la primer letra de la segunda palabra
# se pone en mayúsculas
# variableDeEjemplo
# nombreUsuario = "pepe"
# contraseñaUsuario = "ñññ"
# print(f"Nombre de usuario: {nombreUsuario}; contraseña: {contraseñaUsuario}")

# lo correcto es usar en programacion snake_case
# palabras_en_minúsculas_y_con_guión_bajo

nombre_usuario = "pepe"
contraseña_usuario = "ñññ"
print(f"Nombre de usuario: {nombre_usuario}; contraseña: {contraseña_usuario}")



#¿Mario es el usuario que esta actualmente logueado? 

# variable de tipo booleana
marioLogueado = "Mario" in nombre_usuario

# convertir a una cadena 
print(f"Mario se ha logueado: {marioLogueado}")






# se borra la variable pero no el dato porque el dato se carga antes que 
# borre la variable. Cuando borro la variable el dato ya fue cargado a la 
# variable bienvenida

# defino una variable y asigno un dato
mensaje = "dato que se borra"
# concateno los string con mensaje y lo asigno a bienvenida
bienvenida = f"la accion: {mensaje}"
# borro mensaje
del mensaje
# imprimo bienvenida con los datos de mensaje
print(bienvenida)



# se borra la variable con el dato porque el dato se borra antes
# de cargase a bienvenida, por lo tanto bienvenido tiene error.

# defino una variable y asigno un dato
mensaje = "dato que se borra"
# borro mensaje   # ERROR: name 'mensaje' is not defined

# del mensaje

# concateno los string con mensaje y lo asigno a bienvenida
bienvenida = f"la accion: {mensaje}"
# imprimo bienvenida con los datos de mensaje
print(bienvenida)


# minuto 54