# class Foo:
#     pass

# f1 = Foo()
# f2 = Foo()
# print(type(f1))

# numero = 56
# print(type(numero))

# print(dir(Foo))
# print(dir(int))

# print(dir(f1))
# f1.nombre='F1'
# print(dir(f1))
# print(f1.nombre)
# print(vars(f1))
# print(vars(f2))

# # otra
# class Gato:
#     num_patas = 4
#     orejas = 2
#     nombres = []
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.nombres.append(nombre)

# micha = Gato('Micha')
# garfield = Gato('Garfield')

# print(micha.num_patas)
# print(micha.nombre)
# print(garfield.nombres)



# # otra más
# #      _protegido de la clase
# #     __privado (name mangling)

# class Foo:
#     _atributo_cls_protegido = 0
#     __atributo_cls_privado = 0
    
#     def __init__(self, x):
#         self.x = x
#         self._x = x * 2
#         self.__x = x * 3
    
#     def obtener_x(self):
#         return self.x
    
#     def obtener_x_protegida(self):
#         return self._x
    
#     def obtener_x_privada(self):
#         return self.__x
    
    
# fo = Foo(2)
# print(f'Acceso a fo._atributo_cls_protegido: {fo._atributo_cls_protegido}')
# print(fo.x) # 2
# print(fo._x) # 4
# # print(fo.__x) #### AttributeError



# # NO SE PUEDE ACCEDER AL ATRIBUTO PRIVADO DE FORMA DIRECTA
#     # print(f'Acceso a fo.__atributo_cls_privado: {fo.__atributo_cls_privado}')
#                                                 #  ^^^^^^^^^^^^^^^^^^^^^^^^^
# # AttributeError: 'Foo' object has no attribute '__atributo_cls_privado'. Did you mean: '_Foo__atributo_cls_privado'?


# fo = Foo(2)
# print(f'Obtener x: {fo.obtener_x()}')
# print(f'Obtener x protegida: {fo.obtener_x_protegida()}')
# print(f'Obtener x privada: {fo.obtener_x_privada()}')
# print(dir(fo))

# print('Si trato de acceder a métodos o atributos de forma directa \n')
# print('clase.atributo --> Sin problemas porque es publico\n')
# print('clase._atributo --> Sin problemas porque es protegido\n')
# print('clase.__atributo --> Con problemas porque es privado\n')
# print('clase.__atributo --> Solo se accede por medio de un método que pase el valor interno al exterior con return\n')


# # construccion de clases personalizadas
# class Corredor:
#     __numeros_usados = set()
    
#     def __new__(cls, nombre, num = 1):
#         while num in cls.__numeros_usados:
#             num += 1
#             cls.__numeros_usados.add(num)
#             instancia = super(Corredor, cls).__new__(cls)
#             instancia.__init__(nombre)
#             instancia.num = num
#             return instancia