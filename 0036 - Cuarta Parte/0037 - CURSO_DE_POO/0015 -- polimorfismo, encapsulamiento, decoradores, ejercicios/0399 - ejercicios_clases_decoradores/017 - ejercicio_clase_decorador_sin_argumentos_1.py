class ClaseSaludo:
    # def __init__(se_llama_a_si_mismo_no_es_parametro, parametro_nombre_de_quien_voy_a_saludar):
    #     se_llama_a_si_mismo_no_es_parametro.atributo_nombre = parametro_nombre_de_quien_voy_a_saludar
    def __init__(self, nomb):
        self.nombre = nomb
        print('002 - asigno el atributo nombre desde el parámetro del constructor de la clase')
    
    # def metodo_saludar(otra_vez_se_llama_a_si_mismo_no_es_parametro):
    #     print(f'¡Hola, {otra_vez_se_llama_a_si_mismo_no_es_parametro.atributo_nombre}!')
    def saludo(self):
        print('004 - ejecuto el método saludo(self) de la clase')
        print(f'005 - muestro el mensaje -> ¡Hola, {self.nombre}!')
        
        

    
# seccion principal (main)

# instanciar la clase
print('001 - instancia_de_la_clase = ClaseSaludo("Nehuen")')
saludar_nehuen = ClaseSaludo('Nehuen')

# cuando voy a llamar a la clase lo hago por su instancia
# instancia_de_la_clase.metodo_saludar() #no cargar el parametro a si mismo
print('003 - llamo al metodo saludo() dentro de la instancia')
saludar_nehuen.saludo()

# acceder a un atributo publico en este caso el atributo nombre es publico
# print(instancia_de_la_clase.atributo_nombre)
print(saludar_nehuen.nombre)



# decorador de una funcion

# decorar la funcion

# la funcion 'mi_decorador' es el decorador y toma la funcion que se decorará
# como argumento 'funcion_a_decorar' 
def mi_decorador(funcion_a_decorar):
    # la funcion 'funcion_envolvente' es una funcion interna
    # que envuelve a la funcion original, los parámetros 
    # (*args, **kwargs) permite que la 'funcion_envolvente' acepte cualquier
    # numero de argumentos posicionales y de palabra clave que la funcion 
    # original pueda recibir
    print('2. Se va a ejecutar la funcion envolvente')
    def funcion_envolvente(*args, **kwargs):
        print('6. Estoy dentro de la funcion envolvente')
        # hacer antes de llamar a la funcion
        print('7. Se va a ejecutar la funcion original')
        resultado = funcion_a_decorar(*args, **kwargs)
        # hacer despues de llamar a la funcion original
        print('9. Ya se ejecutó la funcion original y retorno el resultado')
        return resultado
    # fin de la funcion envolvente
    print('3. Ya se ejecutó la funcion envolvente y retorno la funcion sin paréntesis')
    print('4. Finalmente, el decorador devuelve la funcion_envolvente.')
    return funcion_envolvente


# decoradores
# para aplicar un decorador a una funcion utilizar el simbolo @
print('1. Decoro una funcion para luego llamarla.. (@mi_decorador)')

# def decorador(funcio_a_decorar) -> @decorador
#   # def func_para_decorar()  
#       -> funcion que se pasa como argumentos a la funcion decorador
@mi_decorador
def la_funcion_a_ser_decorada():
    print('8. Soy la función original!!!!')
    
# cuando llamamos a 'la_funcion_a_ser_decorada()' 
# en realidad se esta ejecutando
# la funcion envolvente del 
# decorador 'mi_decorador()' -> def mi_decorador(funcion_a_decorar):
print('5. llamo a la funcion decorada desde el terminal')
la_funcion_a_ser_decorada()




