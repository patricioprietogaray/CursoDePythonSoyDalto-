# decorador funcion simple
def requiere_login(func):
    def wrapper(self, *args, **kwargs):
        if not self.logueado:
            print('Se debe loguear')
            return
        return func(self, *args, **kwargs)
    return wrapper
    


class Usuario:
    # atributo de clase
    _usuarios_registrados = []
    
    # constructor de la clase
    def __init__(self, nombre_usuario, logueado = False):
        self.logueado = logueado
        self.nombre_usuario = nombre_usuario    
        if self.nombre_usuario in Usuario._usuarios_registrados:
            # se puede lanzar una excepcion con 
            raise ValueError(f'{self.nombre_usuario} ya es un usuario registrado!') 
            # print(f'{self.nombre_usuario} ya es un usuario registrado!')
        else:
            Usuario._usuarios_registrados.append(self.nombre_usuario)
    
    # listar los usuarios con decorado con class method
    @classmethod
    def listar_usuarios(cls):
        # cls en vez de self, muestro la lista
        print(f'Los usuarios son: {cls._usuarios_registrados}')
    
    # metodo estático es como no perteneciera a la clase y por eso no usa self ni cls
    # (esta en la clase solo por acomodarlo en algun lugar)
    @staticmethod
    def validar_password(password):
        return len(password) > 7
    
    def login(self):
        self.logueado = True
        print('Inicio la sesión...')
    
    def logout(self):
        self.logueado = False
        print('Cierro la sesión...')
        
    @requiere_login
    def ver_perfil(self):
        print(f'Este es el perfil de {self.nombre_usuario}')
        
        
# Crear un usuario
u1 = Usuario("juan")

# Intentar ver el perfil sin estar logueado
u1.ver_perfil()  # Debería mostrar: "Se debe loguear"

# Loguearse
u1.login()

# Ahora sí ver el perfil
u1.ver_perfil()  # Debería mostrar: "Este es el perfil de juan"

# Ahora cierro la sesión
u1.logout()



# # EXPLICACION

# # 👨‍🏫 El decorador requiere_login
# Primero tenemos una función especial llamada decorador, 
# que se llama requiere_login.

# Un decorador es una función que recibe otra función, 
# la envuelve y le agrega comportamiento 
# extra antes o después de que se ejecute.

# def requiere_login(func):
#     def wrapper(self, *args, **kwargs):
#         ...
#         return func(self, *args, **kwargs)
#     return wrapper
# En este caso, el decorador:

# Recibe una función func (por ejemplo, ver_perfil).

# Crea una función interna llamada wrapper, 
# que será la nueva función que realmente 
# se ejecuta cuando llamamos a ver_perfil.

# Antes de ejecutar func, chequea si self.logueado es True.

# Si no estás logueado, imprime un mensaje y no deja ejecutar el método.

# Si sí estás logueado, permite la ejecución.

# 🧱 La clase Usuario
# Ahora vamos con la clase:

# Usuario._usuarios_registrados: es una lista compartida 
# entre todas las instancias, que guarda los nombres de usuario creados.

# En el __init__, si el nombre ya existe, 
# lanza un error. Si no, lo agrega a la lista.

# listar_usuarios: método de clase para imprimir los usuarios.

# validar_password: método estático para validar contraseñas (más de 7 caracteres).

# login y logout: métodos para cambiar el estado de logueado.

# ver_perfil: método decorado con @requiere_login, 
# así que solo se ejecuta si estás logueado.

# 🧪 En uso:
# u1 = Usuario("juan")       # Se crea el usuario "juan"
# u1.ver_perfil()            # No está logueado, muestra "Se debe loguear"
# u1.login()                 # Cambia logueado a True
# u1.ver_perfil()            # Ahora sí muestra el perfil
# u1.logout()                # Cambia logueado a False
# Este patrón es muy útil para proteger métodos 
# que no deberían ejecutarse sin autenticación. 
# Se usa muchísimo en desarrollo web, APIs y sistemas de usuarios.


