# Ejercicio 2: Dispositivo, SmartPhone y Tablet (Medio)

# Define una clase base llamada Dispositivo con atributos como marca y modelo, 
# y un método para mostrar la información básica del dispositivo. 
# Luego, crea dos clases hijas: SmartPhone con atributos adicionales 
# como sistema_operativo y tiene_camara, y Tablet con atributos como 
# tamaño_pantalla y tiene_teclado. Ambas clases hijas deben utilizar 
# super() en su inicialización y tener métodos específicos para sus 
# funcionalidades (por ejemplo, tomar_foto() para SmartPhone y escribir() para Tablet).

class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def informacion_basica(self):
        return f'La info básica del dispositivo es marca: {self.marca} - modelo: {self.modelo}'

class SmartPhone(Dispositivo):
    def __init__(self,marca, modelo, sistema_operativo,tiene_camara):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo
        self.tiene_camara = tiene_camara
    
    def tomar_foto(self):
        return f'Saque una foto con mi {self.marca}-{self.modelo}, \ncon una resolucion de {self.tiene_camara} y un sistema operativo: {self.sistema_operativo}'


class Tablet(Dispositivo):
    def __init__(self,marca, modelo, tamaño_pantalla,tiene_teclado):
        super().__init__(marca,modelo)
        self.tamaño_pantalla = tamaño_pantalla
        self.tiene_teclado = tiene_teclado
        
    def escribir(self):
        return f'Estoy tipeando con una resolucion de {self.tamaño_pantalla} en mi {self.marca}-{self.modelo}\nCon teclado en pantalla tipo {self.tiene_teclado}'


print('CeluPato')
celupato = SmartPhone('Apple','Iphone 15 Pro', 'MacOS', '48MP')
print(celupato.informacion_basica())
print(celupato.tomar_foto())


print('TabletPato')
tabletpato = Tablet('Gamin','G23','480x320','touch')
print(tabletpato.informacion_basica())
print(tabletpato.escribir())