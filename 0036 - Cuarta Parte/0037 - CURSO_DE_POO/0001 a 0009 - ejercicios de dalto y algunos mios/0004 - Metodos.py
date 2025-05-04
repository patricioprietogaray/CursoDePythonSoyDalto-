#  metodos de una clase

# los metodos en una clase son las acciones
# los metodos se definen como funciones
# self se autoreferencia a la clase dentro de la clase

class Celular:
    # Atributos de la clase
        # constructor
    def __init__(self, marca, modelo, camara):
        # cargo los atributos
        self.marca=marca
        self.modelo=modelo
        self.camara=camara

    # Métodos de la clase
    # usar como parametro self del objeto instanciado asi poder utilizar
    # el parámetro del punto 
    def llamar(self):
        print("Estas haciendo un llamado!")
    
    # (self) hace referencia a la propia clase 
    #               -debe estar self para funcionar-
    def cortar(self):
        print(f'Cortaste la llamada capo desde tu {self.modelo}')
        # {modelo}  --> no funciona asi. porque le paso self a cortar para que 
        #         haga referencia al objeto.
        # Solucion {self.modelo}
    
celu1 = Celular("Samsung", "S23", "48MPx")
celu2 = Celular("Apple", "Iphone 15 Pro", "96MPx")
print(f'La marca es {celu1.marca}, el modelo es {celu1.modelo} y su camara tiene {celu1.camara}.')
celu1.llamar()
celu1.cortar()
print(f'La marca es {celu2.marca}, el modelo es {celu2.modelo} y su camara tiene {celu2.camara}.')
celu2.llamar()
celu2.cortar()

