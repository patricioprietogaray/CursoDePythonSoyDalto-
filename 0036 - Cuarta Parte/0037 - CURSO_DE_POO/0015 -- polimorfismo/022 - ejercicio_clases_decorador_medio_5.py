# Medio: @classmethod para gestionar instancias y decorador simple

# Crea una clase Usuario.
class Usuario:
# La clase debe tener un atributo de clase _usuarios_registrados (lista) 
# para llevar un registro de todos los nombres de usuario creados.
    _usuarios_registrados = []
    
# El constructor __init__(self, nombre_usuario) debe añadir el 
# nombre_usuario a _usuarios_registrados solo si no existe ya 
# (para evitar duplicados). 
# Si ya existe, que lance una excepción o imprima un mensaje.
    def __init__(self, nombre_usuario):
        
        if len(Usuario._usuarios_registrados) == 0:
            print(f'Lista está vacía, y por eso agrego al usuario: {nombre_usuario}!')
            Usuario._usuarios_registrados.append(nombre_usuario)
            return
        
        for user in Usuario._usuarios_registrados:
            # print(f'Dentro del for muestro user: {user}')
            if user == nombre_usuario:
                print(f'El usuario {nombre_usuario} ya se encuentra registrado!')
                break
            else:
                continue
        
        
        # if len(Usuario._usuarios_registrados) == 0:
        #     print('Sin usuarios registrados....')
        # elif Usuario._usuarios_registrados == nombre_usuario:
        #     print('Al menos tiene uno o más usuarios registrados')
        
        # print(f'Se agrega el usuario: {nombre_usuario}')
        # Usuario._usuarios_registrados.append(nombre_usuario)

# Crea un @classmethod llamado listar_usuarios() que imprima todos 
# los _usuarios_registrados.

# Crea un @staticmethod llamado validar_password(password) 
# que devuelva True si la contraseña tiene al 
# menos 8 caracteres y False en caso contrario.


# Crea un decorador simple llamado @requiere_login que, 
# antes de ejecutar un método de instancia, verifique un supuesto 
# atributo self.logueado (que deberás añadir y manejar en la clase, 
# por ejemplo, con métodos login() y logout()). 
# Si no está logueado, el decorador debe imprimir "Acceso denegado. 
# Por favor, inicie sesión." 
# y no ejecutar el método. Aplica este decorador a un método de 
# ejemplo como ver_perfil().


# comandos
user = Usuario('admin')
print(user._usuarios_registrados)
user = Usuario('admin2')
print(user._usuarios_registrados)
user = Usuario('admin')
print(user._usuarios_registrados)