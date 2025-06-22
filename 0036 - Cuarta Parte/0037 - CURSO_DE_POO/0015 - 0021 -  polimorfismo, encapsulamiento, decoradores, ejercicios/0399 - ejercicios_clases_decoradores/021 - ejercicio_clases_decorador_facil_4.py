import math

# Fácil: @property para un círculo

# Crea una clase Circulo 
# con un atributo "privado" __radio.
class Circulo:
    def __init__(self, radio):
        self._radio = radio
        

# Usa el decorador @radio.setter 
# para crear un setter para radio 
# que solo permita valores positivos.
    @property
    def func_radio(self):
        return self._radio
    
    @func_radio.setter
    def func_radio(self, radio):
        if radio >= 0.0:
            self._radio = radio
    
# Usa el decorador @property para crear 
# una propiedad calculada area 
# que devuelva el área del círculo 
# ($ \pi \cdot radio^2 $).
    @property
    def calc_area(self):
        return math.pi * self._radio ** 2




# Esta propiedad no debe tener un setter 
# (será de solo lectura).

# Prueba creando un círculo, cambiando su radio (con valores válidos e inválidos) y consultando su área.
mi_circulo = Circulo(0)
print(f'Valor del radio de un ciculo: {mi_circulo._radio}')
print('Asigno 2.5 como valor al radio ...')
mi_circulo.func_radio = 2.5 
print(f'valor asignado al radio: {mi_circulo._radio}')
print(f'Valor del area de un ciculo: {mi_circulo.calc_area}')

