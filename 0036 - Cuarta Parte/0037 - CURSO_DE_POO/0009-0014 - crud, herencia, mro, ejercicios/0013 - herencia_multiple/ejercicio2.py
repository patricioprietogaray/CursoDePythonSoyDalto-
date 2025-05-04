# ¡Excelente! Vamos con un ejercicio de herencia múltiple. 
# Aquí tienes uno que combina habilidades de diferentes "trabajadores":

# **Ejercicio de Herencia Múltiple: Trabajador Polivalente**

# **Describe las clases necesarias para modelar un "Trabajador Polivalente". 
# Este trabajador tiene habilidades de:**

# 1.  **Un "Empleado de Oficina"**: Puede realizar tareas administrativas y usar software de oficina.
# 2.  **Un "Manitas"**: Puede realizar reparaciones básicas y trabajos manuales.

# **Piensa en las siguientes características y cómo podrías distribuirlas entre las clases:**

# * **Clase `EmpleadoDeOficina`**:
#     * Atributos: `nombre`, `departamento`, `software_dominado` (lista de strings).
#     * Métodos: `enviar_correo(destinatario, asunto, cuerpo)`, `generar_informe(formato)`.

# * **Clase `Manitas`**:
#     * Atributos: `nombre`, `herramientas_poseidas` (lista de strings), `experiencia_en_años` (int).
#     * Métodos: `reparar(objeto)`, `instalar(dispositivo)`.

# **Tu tarea es:**

# 1.  **Define las clases `EmpleadoDeOficina` y `Manitas` con sus respectivos atributos y métodos.**

class EmpleadoDeOficina:
    def __init__(self, nombre,software,departamento):
        self.nombre = nombre
        self.departamento = departamento
        self.software_dominado = software
    
    def enviar_correo(self, destinatario,asunto,cuerpo):
        print(f'El empleado ({self.nombre})\nenvió un correo: TO: {destinatario}.\nSubject: {asunto}.\nBody: {cuerpo}.')
    
    def generar_informe(self, formato):
        print(f'El empleado ({self.nombre}), generó un reporte en formato: {formato}')


class Manitas:
    def __init__(self, nombre,herramientas,experiencia):
        self.nombre = nombre
        self.herramientas = herramientas
        self.experiencia = experiencia
        
    def reparar(self, objeto):
        print(f'Manitas ({self.nombre}) reparó {objeto}.')
        
    def instalar(self, dispositivo):
        print(f'Manitas ({self.nombre}) instaló {dispositivo}')




# 2.  **Crea una clase llamada `TrabajadorPolivalente` 
# que herede de ambas clases (`EmpleadoDeOficina` y `Manitas`).**

class TrabajadorPolivalente(EmpleadoDeOficina, Manitas):

# 3.  **Define el constructor (`__init__`) de la clase `TrabajadorPolivalente`.** 
# Este constructor deberá recibir argumentos para inicializar los atributos 
# de ambas clases padre (nombre, departamento, software_dominado, herramientas_poseidas, experiencia_en_años). 
# Recuerda cómo llamar a los constructores de las clases padre en herencia múltiple.

    def __init__(self, nombre, software, departamento, herramientas, experiencia):
        EmpleadoDeOficina.__init__(self, nombre, software, departamento)
        Manitas.__init__(self, nombre,herramientas,experiencia)
        

# 4.  **Crea un método en `TrabajadorPolivalente` llamado `realizar_tarea(tarea, *args)` 
# que pueda realizar las siguientes acciones según el valor de `tarea`:**
    
#     def realizar_tarea(self, tarea, *args):
        
# #     * Si `tarea` es `'enviar_correo'`, llamará al método `enviar_correo` de la clase `EmpleadoDeOficina` 
# # con los argumentos necesarios (`destinatario`, `asunto`, `cuerpo`).
#         if tarea == 'enviar_correo':
#             # destructurar args en destino, asunto y cuerpo
#             destino, asunto, cuerpo = args
#             # self hace referencia a EmpleadoDeOficina
#             self.enviar_correo(destino,asunto,cuerpo)
#             print(f'Envio de correo a {destino}.\nAsunto: {asunto}.\nCuerpo: {cuerpo}.')
# #     * Si `tarea` es `'generar_informe'`, llamará al método `generar_informe` de la clase `EmpleadoDeOficina` con el argumento `formato`.
#         elif tarea == 'generar_informe':
#             informe_formato = args
#             self.generar_informe(informe_formato)
# #     * Si `tarea` es `'reparar'`, llamará al método `reparar` de la clase `Manitas` con el argumento `objeto`.
#         elif tarea == 'reparar':
#             objeto = args
#             self.reparar(objeto)
# #     * Si `tarea` es `'instalar'`, llamará al método `instalar` de la clase `Manitas` con el argumento `dispositivo`.
#         elif tarea == 'instalar':
#             dispositivo = args
#             self.instalar(dispositivo)
# #     * Si la `tarea` no coincide con ninguna de las anteriores, deberá imprimir un mensaje indicando que la tarea no es reconocida.
#         else:
#             print(f'{self.nombre} no puede realizar {tarea} {args}')

# CORRECCION PARA QUE LE CODIGO SEA MAS ROBUSTO
    def realizar_tarea(self, tarea, *args):
        if tarea == 'enviar_correo':
            if len(args) == 3:
                destino, asunto, cuerpo = args
                self.enviar_correo(destino, asunto, cuerpo)
                print(f'Envio de correo a {destino}.\nAsunto: {asunto}.\nCuerpo: {cuerpo}.')
            else:
                print(f'Error: Se necesitan 3 argumentos para {tarea}.')
        elif tarea == 'generar_informe':
            if args:
                formato = args[0]
                self.generar_informe(formato)
            else:
                print(f'Error: Se necesita el formato para {tarea}.')
        elif tarea == 'reparar':
            if args:
                objeto = args[0]
                self.reparar(objeto)
            else:
                print(f'Error: Se necesita el objeto a {tarea}.')
        elif tarea == 'instalar':
            if args:
                dispositivo = args[0]
                self.instalar(dispositivo)
            else:
                print(f'Error: Se necesita el dispositivo a {tarea}.')
        else:
            print(f'{self.nombre} no puede realizar {tarea} {args}')





# 5.  **Crea una instancia de la clase `TrabajadorPolivalente` y prueba su método `realizar_tarea()` con diferentes tipos de tareas.**



# Cambios realizados: 
# Verificación de la cantidad de argumentos: Para enviar_correo, 
# ahora se verifica que se hayan pasado exactamente 3 argumentos.
# 
# Acceso al primer elemento de args: Para generar_informe, 
# reparar e instalar, se accede al primer elemento de la tupla 
# args (args[0]) para obtener el argumento necesario.
# 
# Mensajes de error: Se agregaron mensajes de error si no 
# se proporcionan los argumentos esperados para cada tarea.
# 
# Si bien tu código funcionaba para los casos que probaste, 
# esta pequeña modificación lo hace más robusto al verificar 
# la cantidad esperada de argumentos.



# ¡Este ejercicio te permitirá practicar la definición de clases base, la herencia múltiple y cómo delegar acciones a los métodos de las clases padre desde la clase hija! ¡Mucha suerte y a programar! ¡Estoy aquí para ayudarte si tienes alguna pregunta!


nombre_empl_oficina = 'Juan'
software_dominado = ['computadora','Augusta','Navegador','ofimática']
departamento = 'administración'

# instanciar

empl = EmpleadoDeOficina(nombre_empl_oficina, software_dominado, departamento)
empl.enviar_correo('pepe@argento.com.ar','Pedido de Informe','Que ha ocurrido con el oficio del 12/12/2012?')
empl.generar_informe('PDF')

# Atributos: `nombre`, `herramientas_poseidas` (lista de strings), `experiencia_en_años` (int).

nombre_manitas = 'Jose'
herramientas_poseidas = ['destornillador', 'pinza', 'buscapolo']
experiencia = 5

mani = Manitas(nombre_manitas, herramientas_poseidas, experiencia)
mani.instalar('el aire acondicionado')
mani.reparar('el calefactor')

# nombre_poli = 'Pepe'
# software_dominado_poli = ['computadora','Augusta','Navegador','ofimática']
# departamento_poli = 'administración'
# herramientas_poseidas_poli = ['destornillador', 'pinza', 'buscapolo']
# experiencia_poli = 5

# poli = TrabajadorPolivalente(nombre_poli,software_dominado_poli,departamento_poli,herramientas_poseidas_poli,experiencia_poli)
poli = TrabajadorPolivalente(
    nombre='Pepe',
    software=['Excel', 'Word'],
    departamento='Administración',
    herramientas=['destornillador', 'alicate'],
    experiencia=4
)
poli.realizar_tarea('enviar_correo', 'ana@q.com','Informe mensual','Adjunto archivo')
# poli.realizar_tarea('enviar_correo','p@p','titulo','cuerpo')
# poli.realizar_tarea('enviar_correo', 'ana@correo.com', 'Informe mensual', 'Adjunto el archivo del mes.')
poli.realizar_tarea('generar_informe','PDF')
poli.realizar_tarea('reparar', 'el calefactor')
poli.realizar_tarea('instalar','el aire acondicionado')
poli.realizar_tarea('apagar','las luces')