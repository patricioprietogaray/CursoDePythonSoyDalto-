#  escribir la serie de fibonacci hasta un numero especifico de terminos

# def suma(a, b):
#     return a + b

# def fibonacci(inicio, final):
#     lista_fibonacci = [0,1]  # ultimo elemento -1     anteultimo elemento -2
#     lista_fibonacci_retorno = []
#     while True:
#         lista_fibonacci.append(suma(lista_fibonacci[-2],lista_fibonacci[-1]))
#         if lista_fibonacci[-1] > final:
#             break
#         if lista_fibonacci[-1] > inicio and lista_fibonacci[-1] < final:
#             lista_fibonacci_retorno.append(lista_fibonacci[-1])
            
#         # if final > lista_fibonacci[-1]: break
#     # return lista_fibonacci_retorno    
#     return lista_fibonacci, lista_fibonacci_retorno


# lista_fibonacci, lista_fibonacci_retorno = fibonacci(10,50)
# print(f'''La lista de fibonacci de control es {lista_fibonacci} 
#         y la lista de fibonacci resultado es {lista_fibonacci_retorno}''')
# # print(fibonacci(10,50))
    
    
    
#     # lista_fibonacci.append(suma(a,b))
#     # suma(a,b)


# resolucion de Dalto
def fibonacci(num):
    # a=0 y b=1
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            # mientras esta en el bucle
            # a=b y b=b+a
            a,b = b, b + a  

resultado = fibonacci(33)
print(f'La serie de Fibonacci desde 0 a 34 es: {resultado}')