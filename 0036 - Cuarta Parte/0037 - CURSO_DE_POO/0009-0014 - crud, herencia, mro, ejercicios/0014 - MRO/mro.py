# method resolution order - método de orden para la resolucion o metodo resolucion ordenado
# El método de resolucion de orden es el orden en el que python busca métodos y atributos en las clases.
# Es importante para tener en cuenta
# Si una clase tiene una cadena larga de herencias debemos entender como fuciona para saber 
# que tiene prioridad y que se debe ejecutar primero
# Acá la funcion super() entra en juego.
# Cuando llamamos a super() python consulta al MRO, para saber cual es la próxima clase que debe buscar
# en la lista para hallar el método.
# ..
# .

# # clase A origen
# class A:
#     def hablar(self):
#         print('Hola desde A')

# # clase B hereda de A
# class B(A):
#     def hablar(self):
#         print('Hola desde B')

# # clase C hereda de A
# class C(A):
#     def hablar(self):
#         print('Hola desde C')

# # clase D hereda de B y C
# class D(B,C):
#     def hablar(self):
#         print('Hola desde D')


# # todas las clases tienen el mismo método "hablar()"
# # ¿cual es el que muestra?
# d = D()
# d.hablar()
# # respuesta: 'Hola desde D' 
# # porque le da prioridad a la clase que estamos llamando (D) y como D tiene un método hablar
# # entonces muestra el metodo de D.




# Ahora D sin método a quien le da prioridad a B o C?

# # clase A origen
# class A:
#     def hablar(self):
#         print('Hola desde A')

# # clase B hereda de A
# class B(A):
#     def hablar(self):
#         print('Hola desde B')

# # clase C hereda de A
# class C(A):
#     def hablar(self):
#         print('Hola desde C')

# # clase D hereda de B y C
# class D(B,C):
#     pass

# d=D()
# d.hablar()

# # respuesta 'Hola desde B'
# # al no tener nada desde D (pass) entonces se va a B porque es la primer clase que hereda


# # Ahora B no tiene nada
# # clase A origen
# class A:
#     def hablar(self):
#         print('Hola desde A')

# # clase B hereda de A
# class B(A):
#     pass

# # clase C hereda de A
# class C(A):
#     def hablar(self):
#         print('Hola desde C')

# # clase D hereda de B y C
# class D(B,C):
#     pass

# d=D()
# d.hablar()

# # respuesta 'Hola desde C'
# # al no tener nada desde D (pass) ni B (pass) entonces se va a C porque es 
# # la otra clase que hereda


# # Y si C no tiene nada????

# # Ahora C no tiene nada
# # clase A origen
# class A:
#     # def hablar(self):
#     #     print('Hola desde A')
#     pass

# # clase B hereda de A
# class B(A):
#     pass

# # clase C hereda de A
# class C(A):
#     pass

# # clase D hereda de B y C
# class D(B,C):
#     pass

# d=D()
# d.hablar()

# # respuesta 'Hola desde A'
# # al no tener nada desde D (pass) ni B (pass) ni C (pass) entonces se va a A porque es 
# # la clase principal que hereda a las demas


# A es padre o superclase de B
# A es padre o superclase de C
# B es hija o subclase de A
# C es hija o subclase de A
# B es padre o superclase de D
# C es padre o superclase de D
# D es hija o subclase de B y C (primero B y luego C)

# llamo el metodo desde D  --> si tiene metodo muestra el metodo de D
# llamo el método desde D  --> si no tiene método muestra el método de B
# llamo el método desde D  --> si D y B no tienen método muestra el método de C
# llamo el método desde D  --> si D, B y C no tienen método muestra el método de A
# llamo el método desde D  
#       --> si ninguna clase tiene el método que estoy llamando lanza una excepcion d.hblar() AttributeError


# Ahora tengo un leve cambio

# A         B   A padre de C;   B padre de D
# C         D   C padre de E e hijo de A; D padre de E e hijo de B
#      E        E hijo de C y D

# T o d o s  tienen el mismo metodo hablar()
# ee = E()
# ee.hablar()   --> hola desde E

# E pass
# ee = E()
# ee.hablar()   --> hola desde C


# E pass
# A pass
# ee = E()
# ee.hablar()   --> hola desde D

# E pass
# A pass
# D pass
# ee = E()
# ee.hablar()   --> hola desde B

# class A:
#     # pass
#     def hablar(self):
#         print('Hola desde A')

# class B:
#     def hablar(self):
#         print('Hola desde B')

# class C(A):
#     # pass
#     def hablar(self):
#         print('Hola desde C')

# class D(B):
#     # pass
#     def hablar(self):
#         print('Hola desde D')

# class E(C,D):
#     pass
#     # def hablar(self):
#     #     print('Hola desde E')

# # A         B   A padre de C;   B padre de D
# # C         D   C padre de E e hijo de A; D padre de E e hijo de B
# #      E        E hijo de C y D

# ee = E()
# ee.hablar()

# print('¿Cual es el orden de ejecución?')
# print(E.mro()) # --> clase.mro()
# # [<class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, 
# # <class '__main__.D'>, <class '__main__.B'>, <class 'object'>]

# # si quiero ejecutar un metodo de otra clase (clase B) desde mi instancia (a la clase E) 

# # instancio ee desde la clase E (tento atributos y metodos de E)
# ee=E()

# # ejecuto el metodo hablar de la clase B y se lo asigno a la instancia ee
# # correccion: por ia
# # No estás "asignando" el método a ee, simplemente estás ejecutando el método hablar de B pasándole ee como self.
# B.hablar(ee)

# # "Estoy ejecutando el método hablar de la clase B sobre un objeto ee que es instancia de E."



# # mas prolijo usando super()

# class A:
#     def hablar(self):
#         print('Hola desde A')

# class B:
#     def hablar(self):
#         print('Hola desde B')

# class C(A):
#     def hablar(self):
#         print('Hola desde C')
#         super().hablar()

# class D(B):
#     def hablar(self):
#         print('Hola desde D')
#         super().hablar()

# class E(C, D):
#     def hablar(self):
#         print('Hola desde E')
#         super().hablar()

# ee = E()
# ee.hablar()


# # salida  
# # Hola desde E
# # Hola desde C
# # Hola desde A
# # Hola desde D
# # Hola desde B


# # object
# #   ├── A
# #   │    └── C
# #   │         └── E
# #   └── B
# #        └── D
# #            └── E









class A:
    def hablar(self):
        print('Hola desde A')

class B:
    def hablar(self):
        print('Hola desde B')

class C(A):
    def hablar(self):
        print('Hola desde C')
        super().hablar()

class D(B):
    def hablar(self):
        print('Hola desde D')
        super().hablar()

class E(C, D):
    def hablar(self):
        print('Hola desde E')
        super().hablar()

ee = E()
ee.hablar()


# terminal:
    
# Hola desde E
# Hola desde C
# Hola desde A






# Te explico por qué pasa eso:

# ee.hablar() llama a E.hablar()

# imprime Hola desde E

# y hace super().hablar().

# super() sigue el orden del MRO:

# E → C

# entonces salta a C.hablar().

# C.hablar() imprime Hola desde C

# y luego hace super().hablar().

# super() otra vez sigue el MRO:

# después de C viene A.

# entonces ejecuta A.hablar().

# A.hablar() imprime Hola desde A

# pero A no llama más super(), así que se corta ahí.

# ¿Y por qué no sigue a D o B?
# Porque C.hablar() ya tomó su propio super() (que apunta a A), 
# y después de A no hay más hablar() en A (ni llamada a super()).

# Entonces no hay forma de llegar a D o B a menos que manualmente lo hicieras.

# 📚 Recordá:
# El super() siempre avanza en el orden de MRO:
# E ➔ C ➔ A ➔ D ➔ B ➔ object

# Pero solo si en cada método hacemos super().hablar(), se seguiría caminando más abajo.




# https://www.youtube.com/watch?v=HtKqSJX7VoM&t=1762s
