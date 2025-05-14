# Complejo: Clase CuentaBancaria

# Crea una clase llamada CuentaBancaria.
# El constructor debe recibir numero_cuenta (string), titular (string) 
# y saldo_inicial (float, por defecto 0).

# Crea un método depositar(cantidad) que sume la cantidad al saldo. 
# La cantidad debe ser positiva.

# Crea un método retirar(cantidad) que reste la cantidad del saldo. 
# La cantidad debe ser positiva y no puede superar el saldo disponible.

# Crea un método consultar_saldo() que devuelva el saldo actual.

# Crea un método transferir(otra_cuenta, cantidad) 
# que permita transferir dinero a otra instancia de CuentaBancaria. 
# Debe verificar que la cantidad sea positiva y que haya saldo suficiente.


# Crea al menos dos cuentas y prueba todas las operaciones, incluyendo transferencias entre ellas.


class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial = 0.00):
        self.numero_cuenta = str(numero_cuenta)
        self.titular = str(titular)
        self.saldo_inicial = float(saldo_inicial)
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo_inicial += cantidad
        return self.saldo_inicial
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo_inicial >= cantidad:
                self.saldo_inicial -= cantidad
        return self.saldo_inicial
    
    def consultar_saldo(self):
        return self.saldo_inicial
    
    # soy un capo lo hice de una!!!!
    # otra cuenta es la instancia de la cuenta destino!!!!!
    def transferir(self, otra_cuenta, cantidad):
        if self.saldo_inicial >= cantidad and cantidad > 0:
            self.retirar(cantidad)
            # self.otra_cuenta = otra_cuenta    OJO NO ESTA DECLARADA EN LA CLASE
            otra_cuenta.depositar = cantidad
            return True
        else:
            print('No se pudo realizar la transferencia!')
            return False
        

cuenta1 = CuentaBancaria('1000/1', 'Pepe')
cuenta2 = CuentaBancaria('2000/1', 'Lolo', 45.00)


print(f'En la cuenta 1, el saldo es {cuenta1.consultar_saldo()}.')
print('En la cuenta 1, deposito 100')
cuenta1.depositar(100)
print(f'En la cuenta 1, el saldo es {cuenta1.consultar_saldo()}.')

print(f'En la cuenta 2, el saldo es {cuenta2.consultar_saldo()}.')
print('En la cuenta 2, deposito 100')
cuenta2.depositar(100)
print(f'En la cuenta 2, el saldo es {cuenta2.consultar_saldo()}.')

print('En la cuenta 2, se retiró 10.50')
cuenta2.retirar(10.50)
print(f'En la cuenta 2, el saldo es {cuenta2.consultar_saldo()}.')

print('En la cuenta 1, se transfiere a la cuenta 2 $1000')
cuenta1.transferir(cuenta2,1000)
print(f'En la cuenta 1, el saldo es {cuenta1.consultar_saldo()}.')
print(f'En la cuenta 2, el saldo es {cuenta2.consultar_saldo()}.')


