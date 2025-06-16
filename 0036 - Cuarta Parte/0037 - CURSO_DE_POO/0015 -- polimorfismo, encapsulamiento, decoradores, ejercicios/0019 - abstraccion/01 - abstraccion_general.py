# abstraccion  --> MECANISMO DE ABSTRACCION DE POO

# manejar la complejidad ocultando todos los detalles innesesarios al programador 
# o al usuario y dandole solo las funcionalidades relevantes

# crear una interfaz simple que oculte la interfaz compleja
# asi como antes se mostro el encapsulamiento era una forma de trabajar con 
# abstraccion, porque eran metodos privados y al usuario le brindamos acceso
# por nombre, que se puede leer, modificar y eliminar (todo como si fuera un atributo)
# pero la complejidad interna es otra, estamos utilizando setters, getters, decoradores;
# y el usuario no lo ve porque le ocultamos la complejidad.
# nosotros le damos lo relevante para que lo use.
# no necesitamos saber como funciona internamente, solo se necesita saber como usarlo.
# por ejemplo para usar un celular solo necesitas saber que apretando un boton sube el volumen
# no sabes que hace internamente cuando subis el volumen.


class Automovil:
    def __init__(self):
        # atributo privado que no puedo acceder desde la instancia y si desde la propia clase
        self._estado = 'apagado'


    # ERROR QUE PUEDE OCURRIR OJO CON ESTO
                            # mi_auto = Automovil        SIN PARENTESIS
                            # mi_auto.encender(mi_auto)  TENGO QUE PASAR LA INSTANCIA COMO PARAMETRO
    # def encender(self):   #--> mi_auto.encender(mi_auto) para poder ejecutar el metodo
                            # porque al declarar la instancia no se agregaron () en la clase 
    
    
    def _encender(self):
        self._estado = 'encendido'
        print('El auto esta encendido.')

    def conducir(self):
        if self._estado == 'apagado':
            self._encender()
        print('conduciendo el automovil!.')
mi_auto = Automovil()
mi_auto.conducir()