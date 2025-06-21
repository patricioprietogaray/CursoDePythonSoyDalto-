# Fácil: Transporte

# Crea una clase base Transporte 
# con un método moverse() que simplemente imprima "Moviéndose..."

class Transporte:
    def moverse(self):
        print('Moviéndose...')

# Crea dos clases derivadas: Coche y Bicicleta.
# Sobrescribe el método moverse() en cada clase derivada para que 
# impriman "El coche se mueve por la carretera" y 
# "La bicicleta se mueve por la ciclovía", respectivamente.
class Coche(Transporte):
    def moverse(self):
        return 'El coche se mueve por la carretera'

class Bicicleta(Transporte):
    def moverse(self):
        return 'La bicicleta se mueve por la ciclovía'


# Crea una lista con un objeto Coche y un objeto Bicicleta. Itera sobre la lista y llama al método moverse() de cada objeto.
auto = Coche()
print(auto.moverse())

bici = Bicicleta()
print(bici.moverse())
