# Ejercicio 3 (Alternativo): CuentaBancaria, CuentaCorriente y CuentaAhorro (Medio-Complejo)

# Crea una clase base llamada CuentaBancaria con atributos como titular y saldo, y métodos 
# para depositar y retirar dinero (con validaciones básicas para no permitir retiros 
# mayores al saldo). Luego, crea dos clases hijas: CuentaCorriente que herede de 
# CuentaBancaria y tenga un atributo adicional limite_sobregiro, permitiendo retiros 
# que excedan el saldo hasta ese límite. También debe tener un método para mostrar 
# el límite de sobregiro. La segunda clase hija es CuentaAhorro, que hereda de 
# CuentaBancaria y tiene un atributo adicional tasa_interes y un método para calcular_interes() 
# que aumente el saldo según la tasa. Asegúrate de utilizar super() en los métodos de 
# inicialización de las clases hijas y considera cómo los métodos retirar se comportarán de 
# manera diferente en cada subclase.




## con atributos como titular y saldo, y métodos 
# para depositar y retirar dinero (con validaciones básicas para no permitir retiros 
# mayores al saldo).

class CuentaBancaria:
    def __init__(self, nombre, saldo=0.00):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, dinero):
        self.saldo += dinero

    def extraer(self, dinero):
        self.saldo -= dinero

    def retorna_saldo(self):
        return f'El saldo de la cuenta es ${self.saldo:.2f}'

    def retorna_informacion(self):
        return f'La cuenta bancaria pertenece a {self.nombre}\nSu saldo es de ${self.saldo:.2f}\n'
    
    def control_extraccion(self, dinero):
        if self.saldo > dinero:
            self.extraer(dinero)
        else:
            print(f'El saldo es insuficiente para la extracción que planea hacer.\nEsta operación queda cancelada.\n\n')


class Validar:
    def validar_monto(self, importe_a_validar=None, mensaje='Ingrese un monto: '):
        while True:
            try:
                # si no se paso un importe se lo pide al usuario
                if importe_a_validar == None:
                    importe_a_validar = input(mensaje)
                importe_a_validar = float(importe_a_validar)
                
                if importe_a_validar >= 0.00:
                    return importe_a_validar
                else:
                    print('El monto no puede ser negativo.')
            except ValueError:
                print('Entrada inválida, debe ingresar un número válido (por ejemplo 10.5).')

# Luego, crea dos clases hijas: y tenga un atributo adicional limite_sobregiro, permitiendo retiros 
# que excedan el saldo hasta ese límite. También debe tener un método para mostrar 
# el límite de sobregiro.
# Asegúrate de utilizar super() en los métodos de 
# inicialización de las clases hijas y considera cómo los métodos retirar se comportarán de 
# manera diferente en cada subclase.

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, sobregiro):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro
    
    def control_extraccion(self, dinero):
        print(f'El saldo de la cc es ${self.saldo}')
        saldosobregiro = self.saldo + self.sobregiro
        
        if self.saldo > dinero:
            super().extraer(dinero)
        elif saldosobregiro > dinero:
            print('Extracción con sobre giro')
            super().extraer(dinero)
        else:
            print(f'El saldo es insuficiente para la extracción que planea hacer.\nEsta operación queda cancelada.\n\n')

    
    
    # def extraer(self, dinero):
    #     if dinero <= self.saldo:
    #         self.saldo -= dinero
    #         return f'Cta. Corriente: Extrajo ${dinero} y su saldo es de ${self.saldo}.'
    #     elif self.saldo < dinero <= (self.saldo + self.sobregiro):
    #         self.saldo -= dinero
    #         return f'Cta. Corriente con sobre giro: Extrajo ${dinero} y su saldo es de ${self.saldo}.'
    #     else:
    #         return f'Cta. Corriente: Saldo insuficiente'
        

# y tiene un atributo adicional tasa_interes y 
# un método para calcular_interes() 
# que aumente el saldo según la tasa.
# Asegúrate de utilizar super() en los métodos de 
# inicialización de las clases hijas y considera cómo los métodos retirar se comportarán de 
# manera diferente en cada subclase.

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre, saldo, tasa_interes):
        super().__init__(nombre, saldo)
        self.tasa_interes = tasa_interes
    
    def calcular_interes(self,interes):
        # por cada operacion aumenta
        # el interes diario
        self.capital = self.saldo
        self.tiempo = 1.00/365
        self.interes_anual = interes
        return (self.capital * (1 + self.interes_anual) ** self.tiempo) - self.capital
        
        
        


# funciones fuera de la clase que simplifica el llamado de las mismas

def operaciones_clase_bancaria(nombre,saldo):
    cb = CuentaBancaria(nombre,saldo)
    valida_importe = Validar()
    while True:
        ingreso_egreso_saldo_info = input(
        '''
        OPERACIONES DIRECTAMENTE EN LA CUENTA BANCARIA
        
        ¿Qué opercación desea realizar?
        
        (D)epósito de dinero
        (E)xtracción de dinero
        (S)aldo
        (I)nformación de la cuenta bancaria
        (Z) -> Salir de la aplicación
        Elija una opción (D-E-S-I-Z): ''').lower()
        if ingreso_egreso_saldo_info == 'z':
            print('Gracias por utilizar nuestros servicios, vuelva pronto!\n')
            return
        elif ingreso_egreso_saldo_info == 'd':
            quiere_depositar = input('Usted va a hacer un depósito, ¿confirma la operación? (S/N): ').lower()
            if quiere_depositar == 's':
                dinero_a_depositar = input('Ingrese un monto a depositar: $')
                dinero_a_depositar = valida_importe.validar_monto(dinero_a_depositar,'')
                cb.depositar(dinero_a_depositar)
                # print(cb.retorna_saldo())
                print(cb.retorna_saldo())
        elif ingreso_egreso_saldo_info == 'e':
            quiere_extraer = input('Usted va a hacer una extracción, ¿confirma la operación? (S/N): ').lower()
            if quiere_extraer == 's':
                dinero_a_extraer = input('Ingrese un monto a extraer: $')
                dinero_a_extraer = valida_importe.validar_monto(dinero_a_extraer,'')
                # funcion para extraer dinero
                cb.control_extraccion(dinero_a_extraer)
                print(cb.retorna_saldo())
                # print(cb.retorna_saldo())
        elif ingreso_egreso_saldo_info == 's':
            saldo_a_validar = valida_importe.validar_monto(cb.saldo,'')
            print(f'Su saldo es de ${saldo_a_validar:.2f}')
        elif ingreso_egreso_saldo_info == 'i':
            print(cb.retorna_informacion())
        # print(cb.retorna_saldo())
            

def operaciones_clase_cta_corriente(nombre,saldo):
    sobre_giro = float(input('''
                             El sobre giro de una cuenta es el monto que podrá
                             operar aún con saldo negativo. El banco le presta
                             ese dinero de sobregiro y luego el pago se hara
                             con intereses del 0%.
                             Ingrese el monto del sobre giro: $'''))
    
    valida_saldo_cc = Validar()
    valida_sobre_giro_cc = Validar()
    valida_importe_cc = Validar()
    saldo = valida_saldo_cc.validar_monto(saldo,'Ingrese el saldo de la cuenta corriente: $')
    sobre_giro = valida_sobre_giro_cc.validar_monto(sobre_giro,'')
    
    cc = CuentaCorriente(nombre,saldo,sobre_giro)
    
    while True:
        ingreso_egreso_saldo_info_cc = input(
        '''
        OPERACIONES EN LA CUENTA CORRIENTE
        
        ¿Qué opercación desea realizar?
        
        (D)epósito de dinero
        (E)xtracción de dinero
        (S)aldo
        (I)nformación de la cuenta corriente
        (Z) -> Salir de la aplicación
        Elija una opción (D-E-S-I-Z): ''').lower()
        if ingreso_egreso_saldo_info_cc == 'z':
            print('Gracias por utilizar nuestros servicios de cuenta corriente!\n')
            return
        elif ingreso_egreso_saldo_info_cc == 'd':
            quiere_depositar_cc = input('Usted va a hacer un depósito, ¿confirma la operación? (S/N): ').lower()
            if quiere_depositar_cc == 's':
                dinero_a_depositar_cc = input('Ingrese un monto a depositar en la cuenta corriente: $')
                dinero_a_depositar_cc = valida_importe_cc.validar_monto(dinero_a_depositar_cc,'')
                cc.depositar(dinero_a_depositar_cc)
                # print(cb.retorna_saldo())
                print(cc.retorna_saldo())
        elif ingreso_egreso_saldo_info_cc == 'e':
            quiere_extraer_cc = input('Usted va a hacer una extracción de la cuenta corriente, ¿confirma la operación? (S/N): ').lower()
            if quiere_extraer_cc == 's':
                dinero_a_extraer_cc = input('Ingrese un monto a extraer: $')
                dinero_a_extraer_cc = valida_importe_cc.validar_monto(dinero_a_extraer_cc,'')
                # funcion para extraer dinero
                cc.control_extraccion(dinero_a_extraer_cc)
                print(cc.retorna_saldo())
                # print(cb.retorna_saldo())
        elif ingreso_egreso_saldo_info_cc == 's':
            saldo_a_validar_cc = valida_saldo_cc.validar_monto(saldo,'')
            print(f'Su saldo es de ${saldo_a_validar_cc:.2f}')
        elif ingreso_egreso_saldo_info_cc == 'i':
            print(cc.retorna_informacion())
        # print(cb.retorna_saldo())


def operaciones_clase_cta_ahorro(nombre,saldo):
    interes = float(input('Ingrese el interes anual (0.01 es el 1% y 1.00 es el 100%): '))
    
    valida_saldo_ca = Validar()
    valida_tasa_interes_ca = Validar()
    valida_monto_ca = Validar()
    tasa_validada = valida_tasa_interes_ca.validar_monto(interes)    
    ca = CuentaAhorro(nombre,saldo,tasa_validada)
    
    while True:
        ingreso_egreso_saldo_info_ca = input(
        '''
        OPERACIONES EN LA CUENTA DE AHORRO
        
        ¿Qué opercación desea realizar?
        
        (D)epósito de dinero
        (E)xtracción de dinero
        (S)aldo
        (I)nformación de la cuenta corriente
        (T)asa de interes
        (Z) -> Salir de la aplicación
        Elija una opción (D-E-S-I-Z): ''').lower()
        if ingreso_egreso_saldo_info_ca == 'z':
            print('Gracias por utilizar nuestros servicios de cuenta ahorro!\n')
            return
        elif ingreso_egreso_saldo_info_ca == 'd':
            quiere_depositar_ca = input('Usted va a hacer un depósito, ¿confirma la operación? (S/N): ').lower()
            if quiere_depositar_ca == 's':
                dinero_a_depositar_ca = input('Ingrese un monto a depositar en la cuenta de ahorro: $')
                dinero_a_depositar_ca = valida_monto_ca.validar_monto(dinero_a_depositar_ca,'')
                ca.depositar(dinero_a_depositar_ca)
                print(ca.retorna_saldo())
        elif ingreso_egreso_saldo_info_ca == 'e':
            quiere_extraer_ca = input('Usted va a hacer una extracción de la cuenta de ahorro, ¿confirma la operación? (S/N): ').lower()
            if quiere_extraer_ca == 's':
                dinero_a_extraer_ca = input('Ingrese un monto a extraer: $')
                dinero_a_extraer_ca = valida_monto_ca.validar_monto(dinero_a_extraer_ca,'')
                ca.control_extraccion(dinero_a_extraer_ca)
                print(ca.retorna_saldo())
                # print(cb.retorna_saldo())
        elif ingreso_egreso_saldo_info_ca == 's':
            saldo_a_validar_ca = valida_saldo_ca.validar_monto(ca.saldo,'')
            print(f'Su saldo es de ${saldo_a_validar_ca:.2f}')
        elif ingreso_egreso_saldo_info_ca == 'i':
            print(ca.retorna_informacion())
        elif ingreso_egreso_saldo_info_ca == 't':
            print(f'Antes del interes, su saldo es de ${ca.retorna_saldo()}')
            intereses = ca.calcular_interes(interes)
            print(f'El interes es de ${intereses}')
            saldo_con_interes = ca.saldo + intereses
            ca.saldo = saldo_con_interes
            print(f'Luego del interes, su saldo es de ${ca.saldo:.2f}')
            
        # print(cb.retorna_saldo())

# # PROGRAMA
nombre = input('Bienvenido a nuestro banco, ¿Cuál es su nombre?: ').capitalize()
v_saldo = Validar()
saldo = 0
saldo_validado = v_saldo.validar_monto(saldo,'')
print(f"Gracias por estar con nosotros {nombre}!!\nSu saldo es de ${saldo_validado:.2f}\n\n")

# trabajando sobre la clase CuentaBancaria (superclase o padre)

# operaciones_clase_bancaria(nombre, saldo_validado)

# operaciones_clase_cta_corriente(nombre,saldo)

operaciones_clase_cta_ahorro(nombre,saldo)


