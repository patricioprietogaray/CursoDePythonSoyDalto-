# Los operadores de comparación son seis

# ==        es igual que
# (!=)      es distinto que (sin parentesis solo != )
# <         es menor que
# <=        es menor o igual que 
# >         es mayor que
# >=        es mayor o igual que 


# 1 HORA 20 MINUTOS

# = asignacion variable = valor  se asigna un valor a una variable
# == compara que sea igual un operador y otro  5 == 6  ¿cinco es igual a seis?
# devuelve true o false


igual_que = 5 == 6
print(f"5 es igual que 6: {igual_que}")
distinto_que = 5 != 6
print(f"5 es distinto que 6: {distinto_que}")
menor_que = 5 < 6
print(f"5 es menor que 6: {menor_que}")
menor_o_igual_que = 5 <= 6
print(f"5 es menor o igual que 6: {menor_o_igual_que}")
mayor_que = 5 > 6
print(f"5 es mayor que 6: {mayor_que}")
mayor_o_igual_que = 5 >= 6
print(f"5 es mayor o igual que 6: {mayor_o_igual_que}")

# calculos combinados
a=5
b=10
c=20

comparacion = a+b != c
print(comparacion)

# comparar usuarios
contraseña_almacenada="PatoMaestro"
usuario_logueado='''PatoMaestro'''
acceso=contraseña_almacenada==usuario_logueado
print(acceso)