class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f'nombre = {self.nombre}: (fuerza = {self.fuerza}, velocidad = {self.velocidad})'
    

# menu
def menu():
    while True:
        print('1. Crear un personaje')
        print('2. Mostrar un personaje')
        print('3. Fusionar dos personajes')
        print('4. Salir')
        opcion = seleccionar_opcion()
        if opcion == 1:
            print()
            print('Seleccionó la creacion de un personaje')
            nombre = input('Ingrese un nombre para el nuevo personaje: ')
            
            fuerza = 0
            while True:
                fuerza = validar('fuerza')
                if fuerza != -1:
                    # print('Saliendo del programa. Bye bye!')    
                    break
            
            velocidad = 0
            while True:
                velocidad = validar('velocidad')
                if velocidad != -1:
                    # print('Saliendo del programa. Bye bye!')    
                    break
            
            # agregar un personaje
            personajito = Personaje(nombre, fuerza, velocidad)
            personajes.append(personajito)

        elif opcion == 2:
            print()
            print('Seleccionó la opción mostrar los personajes')
            for p in personajes:
                print(p)
        elif opcion == 3:
            nombre_fusion = ''
            fuerza_fusion = 0
            velocidad_fusion = 0
            print()
            print('Seleccionó la fucion de dos personajes')
            for p in personajes:
                nombre_fusion += p.nombre
                fuerza_fusion = round((fuerza_fusion + p.fuerza) / 2)
                velocidad_fusion = round((velocidad_fusion + p.velocidad) / 2)

            print(f'El producto final: Nombre: {nombre_fusion}: (fuerza: {fuerza_fusion}, velocidad: {velocidad_fusion})')
            print()

        elif opcion == 4:
            print()
            print('Saliendo de la aplicación...')
            # del personajes
            break
        else:
            continue

# elegir una opcion
def seleccionar_opcion():
    opc = input('Ingrese una opcion válida: (1 - 4): ')
    try:
        numero_opcion = int(opc)         
        return numero_opcion
    except ValueError:
        # si no es un numero
        print('Debe seleccionar un número del 1 al 4!')
        return -1

# validar las entradas: nombre no se valida
#                       fuerza o velocidad se deben validar a int - 
def validar(atributo):
    try:
        retorno = int(input(f'Ingrese un valor en {atributo} (0 - 100): '))
        if retorno > 0 and retorno <= 100:
            return retorno
        else:
            print(f'El valor de {atributo} debe ser desde 0 hasta 100.')
            return -1
    except ValueError:
        print(f'{atributo} debe ser un numero entero.')
        return -1
    
    
    


# terminal

# crear una lista de personas
personajes = []
menu()



# 2.54.20

# crear una lista de personas


# chacer un bucle 