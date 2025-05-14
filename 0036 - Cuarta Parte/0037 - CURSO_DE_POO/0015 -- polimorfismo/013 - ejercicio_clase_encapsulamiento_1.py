class Termostato:
    def __init__(self, temp_actual=20.0, temp_min=15.0, temp_max=30.0):
        # atributo privado _ _
        self.__temp_actual = temp_actual
        # atibuto protegido _
        self._temp_min = temp_min
        self._temp_max = temp_max
        # llama al metodo protegido de uso interno
        self._validar_temperatura()
    
    # metodo protegido de uso interno: validar la temperatura
    def _validar_temperatura(self):
        # metodo protegido para uso interno
        print(f'\nValidación de temperatura (Min: {self._temp_min} - Max: {self._temp_max}.)')
        
        # si el termostato (temp_actual) esta por debajo de la temp minima
        # lo igualo a la temp minima
        if self.__temp_actual < self._temp_min:
            self.__temp_actual = self._temp_min
        # si el termostato (temp_actual) esta por encima de la temp maxima
        # lo igualo a la temp maxima
        elif self.__temp_actual > self._temp_max:
            self.__temp_actual = self._temp_max

    # metodo para mostrar la temperatura actual (atributo privado) fuera de la clase
    # getters
    def get_temperatura(self):
        return self.__temp_actual
    
    # metodo para configurar una temperatura específica 
    # setters
    def set_temperatura(self, temp):
    #    if self._temp_min <= temp <= self._temp_max:
    #        self.__temp_actual = temp
    #        print(f"Temperatura ajustada a: {self.__temp_actual}°C")
    #    else:
    #        print(f"Error: La temperatura debe estar entre {self._temp_min}°C y {self._temp_max}°C.")
        # que entre en juego la validacion directa
        self.__temp_actual = temp
        self._validar_temperatura()
        print(f"Temperatura ajustada a: {self.__temp_actual}°C")
    
    def subir_temperatura(self,grados_a_subir):
        self.__temp_actual += grados_a_subir
        self._validar_temperatura()
        print(f"Se subió la temperatura a: {self.__temp_actual}°C")
        
    
    def bajar_temperatura(self,grados_a_bajar):
        self.__temp_actual -= grados_a_bajar
        self._validar_temperatura()
        print(f"Se bajó la temperatura a: {self.__temp_actual}°C")



# Crear objeto
mi_termostato = Termostato(temp_min=15, temp_max=25)
print(f"Temperatura inicial: {mi_termostato.get_temperatura()}°C")
print(f"\nConfiguro la temperatura a 58.5°C")
mi_termostato.set_temperatura(58.5)
print(f"\nConfiguro la temperatura a 5.15°C")
mi_termostato.set_temperatura(5.15)
print(f"\nConfiguro la temperatura a 18.5°C")
mi_termostato.set_temperatura(18.5)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print(f"\nSubo la temperatura 5°C")
mi_termostato.subir_temperatura(5.0)
print('-------------------------------------')
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)
print(f"\nBajó la temperatura 5°C")
mi_termostato.bajar_temperatura(5.0)