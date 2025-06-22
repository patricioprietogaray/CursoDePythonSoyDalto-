# # Fácil: Clase Libro

# Crea una clase llamada Libro.
# El constructor debe recibir titulo, autor y numero_paginas.
# Crea un método llamado descripcion que devuelva un string formateado 
# con el título y el autor del libro.
# Crea un método llamado es_largo que devuelva True si el libro tiene 
# más de 300 páginas, y False en caso contrario.
# Crea dos instancias de Libro y prueba sus métodos.

class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
    
    def descripcion(self):
        return f'Título: {self.titulo} - Autor: {self.autor}.'
    
    def es_largo(self):
        if self.numero_paginas > 300:
            return True
        else:
            return False

principito = Libro('El principito', 'Antoine de Saint-Exupéry', 92)
codigo_da_vinci = Libro('Codigo Da Vinci', 'Dan Brown', 624)

print(principito.descripcion())
print(principito.es_largo())

print(codigo_da_vinci.descripcion())
print(codigo_da_vinci.es_largo())