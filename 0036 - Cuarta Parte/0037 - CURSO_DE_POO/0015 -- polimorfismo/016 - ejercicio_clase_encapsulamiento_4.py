# Complejo: ConfiguracionSistema

# Crea una clase ConfiguracionSistema que maneje configuraciones "sensibles".
# Tendrá un atributo "privado" __api_key y otro __modo_debug 
# (booleano, por defecto False).
# El constructor debe permitir inicializar __api_key 
# (solo se puede establecer una vez al crear el objeto, 
# no debe haber un setter público para cambiarla después).
# Crea un método get_api_key_ofuscada() que devuelva solo 
# los últimos 4 caracteres de la API key, precedidos 
# por asteriscos (ej. "****-XYZ1"). 
# Si la key tiene menos de 4 caracteres, que devuelva solo asteriscos.
# Crea métodos activar_modo_debug() y desactivar_modo_debug() 
# para cambiar __modo_debug.
# Crea un método esta_en_modo_debug() para consultar el estado de 
# __modo_debug.
# Añade un método "protegido" _registrar_cambio(mensaje) 
# que imprima un mensaje de log (simulado con print) 
# cada vez que se cambie el modo debug. 
# Este método debe ser llamado internamente por activar_modo_debug 
# y desactivar_modo_debug.
# Intenta que no sea posible modificar la __api_key directamente 
# desde fuera una vez creada la instancia.



# Crea una clase ConfiguracionSistema que 
# maneje configuraciones "sensibles".
class ConfiguracionSistema:

# El constructor debe permitir inicializar __api_key 
# (solo se puede establecer una vez al crear el objeto, 
# no debe haber un setter público para cambiarla después).
    def __init__(self, api_key, modo_debug = False):
        # Tendrá un atributo "privado" __api_key y otro __modo_debug 
        # (booleano, por defecto False).    
        self.__api_key = api_key
        self.__modo_debug = modo_debug
    
    # Crea un método get_api_key_ofuscada() que devuelva solo 
    # los últimos 4 caracteres de la API key, precedidos 
    # por asteriscos (ej. "****-XYZ1").
    def get_api_key_ofuscada(self):
        # texto_api_key='Api Key: ****' 
        longitud_api_key = len(self.__api_key)
        # Si la key tiene menos de 4 caracteres, 
        # que devuelva solo asteriscos.
        if longitud_api_key < 4:
            # return texto_api_key
            return '*' * longitud_api_key
        else:
            # texto_api_key +='-'
            # for index,letra in enumerate(self.__api_key):
            #     if (longitud_api_key - 4) <= index <= (longitud_api_key - 1):
            #         texto_api_key += letra 
            # return texto_api_key
            
            # del final 4 elementos desde el final al principio
            return '****-' + self.__api_key[-4:]
    # Crea métodos activar_modo_debug() y desactivar_modo_debug()
    # para cambiar __modo_debug.
    def activar_modo_debug(self):
        # self.__modo_debug = True   OJO ACA
        if not self.__modo_debug: #es falso
            self.__modo_debug = True
            self._registrar_cambio('Modo debug activado')
        
    def desactivar_modo_debug(self):
        # self.__modo_debug = False
        if self.__modo_debug: #es verdadero
            self.__modo_debug = False
            self._registrar_cambio('Modo debug desactivado')
        
    # Crea un método esta_en_modo_debug() para consultar el estado de 
    # __modo_debug.
    def esta_en_modo_debug(self):
        # if self.__modo_debug == True:
        #     self._registrar_cambio('El modo debug está activado') 
        # else:
        #     self._registrar_cambio('El modo debug está desactivado')

        # el codigo anterior se acomodo en activar / desactivar
        return self.__modo_debug


    # Añade un método "protegido" _registrar_cambio(mensaje) 
    # que imprima un mensaje de log (simulado con print)
    # cada vez que se cambie el modo debug. 
    # Este método debe ser llamado internamente por activar_modo_debug 
    # y desactivar_modo_debug.

    def _registrar_cambio(self, mensaje):
        print(f'Mensaje al log: {mensaje}')



# Intenta que no sea posible modificar la __api_key directamente 
# desde fuera una vez creada la instancia.

# configuracion_key = ConfiguracionSistema('asd')
# configuracion_key2 = ConfiguracionSistema('asdfg')
# print(configuracion_key.get_api_key_ofuscada())
# print(configuracion_key2.get_api_key_ofuscada())
# configuracion_debug = ConfiguracionSistema('asdfg',True)
# print('Consultando debug:')
# configuracion_debug.esta_en_modo_debug()
# configuracion_debug.desactivar_modo_debug()
# print('Consultando debug:')
# configuracion_debug.esta_en_modo_debug()
# configuracion_modifica_key = ConfiguracionSistema('asdf ñlkjh')
# configuracion_modifica_key.__api_key = '12345667'
# print(configuracion_key2.get_api_key_ofuscada())

# Ejemplo de uso:
configuracion = ConfiguracionSistema('ESTA_ES_LA_API_KEY_SECRETA')
print(f"API Key Ofuscada: {configuracion.get_api_key_ofuscada()}")

print(f"¿Está en modo debug? {configuracion.esta_en_modo_debug()}")
configuracion.activar_modo_debug()
print(f"¿Está en modo debug? {configuracion.esta_en_modo_debug()}")
configuracion.desactivar_modo_debug()
print(f"¿Está en modo debug? {configuracion.esta_en_modo_debug()}")

configuracion_corta = ConfiguracionSistema('ABCD')
print(f"API Key Ofuscada (corta): {configuracion_corta.get_api_key_ofuscada()}")

configuracion_muy_corta = ConfiguracionSistema('ABC')
print(f"API Key Ofuscada (muy corta): {configuracion_muy_corta.get_api_key_ofuscada()}")

# Intentando acceder al atributo privado (esto no es la forma correcta)
# print(configuracion.__api_key) # Esto generará un AttributeError

# Intentando modificar el atributo privado (esto crea un nuevo atributo, no modifica el original)
configuracion.__api_key = 'NUEVA_KEY_PELIGROSA'
print(f"API Key Ofuscada (después del intento de modificación): {configuracion.get_api_key_ofuscada()}")
