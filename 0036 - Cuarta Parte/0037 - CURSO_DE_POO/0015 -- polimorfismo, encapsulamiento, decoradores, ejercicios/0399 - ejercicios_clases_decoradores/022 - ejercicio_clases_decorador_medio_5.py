# # Medio: @classmethod para gestionar instancias y decorador simple

# # Crea una clase Usuario.
# class Usuario:
# # La clase debe tener un atributo de clase _usuarios_registrados (lista) 
# # para llevar un registro de todos los nombres de usuario creados.
    
#     # atributo de clase que se comparte con todas las funciones de esta clase
#     _usuarios_registrados = []
    
    
# # El constructor __init__(self, nombre_usuario) debe añadir el 
# # nombre_usuario a _usuarios_registrados solo si no existe ya 
# # (para evitar duplicados). 
# # Si ya existe, que lance una excepción o imprima un mensaje.
#     def __init__(self, nombre_usuario, logueado = False):
#         self.nombre_usuario = nombre_usuario
#         self.logueado = logueado
#         self.encontro = False
#         if len(Usuario._usuarios_registrados) == 0:
#             print(f'Lista está vacía, y por eso agrego al usuario: {nombre_usuario}!')
#             Usuario._usuarios_registrados.append(self.nombre_usuario)
#             return
        
#         for user in Usuario._usuarios_registrados:
#             # print(f'Dentro del for muestro user: {user}')
#             if user == self.nombre_usuario:
#                 print(f'El usuario {self.nombre_usuario} ya se encuentra registrado!')
#                 self.encontro = True
#                 break
#             else:
#                 continue
        
#         if self.encontro == False:
#             print(f'Se agrega el usuario: {self.nombre_usuario}')
#             Usuario._usuarios_registrados.append(self.nombre_usuario)
            
#         if requiere_login:
#             print('require_login')

# # Crea un @classmethod llamado listar_usuarios() que imprima todos 
# # los _usuarios_registrados.
#     @classmethod
#     def listar_usuarios(cls):
#         # devuelve la lista de todos los usuarios que se 
#         # encuentran registrados
#         return f'Los usuarios hasta ahora registrados son: {cls._usuarios_registrados}.' 
    

# # Crea un @staticmethod llamado validar_password(password) 
# # que devuelva True si la contraseña tiene al 
# # menos 8 caracteres y False en caso contrario.

# # @staticmethod en Python 
# # se utiliza para definir un método estático dentro de una clase. 
# # Un método estático no depende de la instancia (self) 
# # ni de la clase (cls). 
# # Es simplemente una función que se agrupa dentro de una clase 
# # por razones organizativas o lógicas, 
# # pero no accede ni modifica atributos de instancia ni de clase.


#     @staticmethod
#     def validar_password(password):
#         if len(password) > 7:
#             return True
#         return False


# # Crea un decorador simple llamado @requiere_login que, 
# # antes de ejecutar un método de instancia, verifique un supuesto 
# # atributo self.logueado (que deberás añadir y manejar en la clase, 
# # por ejemplo, con métodos login() y logout()). 
# # Si no está logueado, el decorador debe imprimir "Acceso denegado. 
# # Por favor, inicie sesión." 
# # y no ejecutar el método. Aplica este decorador a un método de 
# # ejemplo como ver_perfil().

# # decorador (va por fuera de la clase)
# def requiere_login(funcion):
#     def wrapper(self, *args, **kwargs):
#         if not self.logueado:
#             print('Acceso denegado. Por favor inicie la sesión.')
#             return
#         return funcion(self, *args, **kwargs)
#     return wrapper

# # comandos
# user = Usuario('admin')
# print('Usuario agregado "admin".')
# print(f'Con instancia: Los usuarios que estan en la lista son:\n{user.listar_usuarios()}')
# # mismo resultado sin instanciar por que es un metodo de clase
# print(f'Sin instancia: Los usuarios que estan en la lista son:\n{Usuario.listar_usuarios()}')
# print(user.validar_password('pepe'))

# # user.listar_usuarios
# # print(user._usuarios_registrados)
# # user = Usuario('admin2')
# # print(user._usuarios_registrados)
# # user = Usuario('admin3')
# # print(user._usuarios_registrados)
# # user = Usuario('admin')
# # print(user._usuarios_registrados)



# COMO QUEDA EL CODIGO

# Medio: @classmethod para gestionar instancias y decorador simple

# Crea una clase Usuario.
# La clase debe tener un atributo de clase _usuarios_registrados (lista) para llevar un registro de todos los nombres de usuario creados.
# El constructor __init__(self, nombre_usuario) debe añadir el nombre_usuario a _usuarios_registrados solo si no existe ya (para evitar duplicados). Si ya existe, que lance una excepción o imprima un mensaje.
# Crea un @classmethod llamado listar_usuarios() que imprima todos los _usuarios_registrados.
# Crea un @staticmethod llamado validar_password(password) que devuelva True si la contraseña tiene al menos 8 caracteres y False en caso contrario.
# Crea un decorador simple llamado @requiere_login que, antes de ejecutar un método de instancia, verifique un supuesto atributo self.logueado (que deberás añadir y manejar en la clase, por ejemplo, con métodos login() y logout()). Si no está logueado, el decorador debe imprimir "Acceso denegado. Por favor, inicie sesión." y no ejecutar el método. Aplica este decorador a un método de ejemplo como ver_perfil().

# CREAR EL DECORADOR
def requiere_login(func):
    def wrapper(self, *args, **kwargs):
        if not self.logueado:
            print('Acceso denegado, por favor inicie la sesión.')
            return
        return func(self, *args, **kwargs)
    return wrapper

# CREAR LA CLASE
class Usuario:
    # atributo de clase
    _usuarios_registrados = []
    
    # constructor
    def __init__(self, nombre_usuario, logueado = False):
        if nombre_usuario in Usuario._usuarios_registrados:
            raise ValueError(f'El usuario "{nombre_usuario}" ya se encuentra registrado.')
        self.nombre_usuario = nombre_usuario
        self.logueado = logueado
        Usuario._usuarios_registrados.append(self.nombre_usuario)
        print(f'Usuario {self.nombre_usuario} agregado!')
        
    # class method
    @classmethod
    def listar_usuarios(cls):
        return f'Usuarios registrados: {cls._usuarios_registrados}'
    
    # static method
    @staticmethod
    def validar_password(password):
        return len(password) > 7
    
    def login(self):
        self.logueado = True
        print(f'{self.nombre_usuario} ha iniciado la sesión')
    
    def logout(self):
        self.logueado = False
        print(f'{self.nombre_usuario} ha cerrado la sesión.')

    # llama al decorador
    # ver_perfil llama a requiere_login
    @requiere_login
    def ver_perfil(self):
        print(f'Perfil de usuario: {self.nombre_usuario}.')
    
    
    
user = Usuario('admin')
print(Usuario.listar_usuarios())  # Muestra los usuarios registrados

print(Usuario.validar_password('1234'))         # False
print(Usuario.validar_password('segura123'))    # True

user.ver_perfil()   # No debe funcionar si no está logueado
user.login()
user.ver_perfil()   # Ahora sí muestra el perfil
user.logout()
user.ver_perfil()   # Otra vez denegado