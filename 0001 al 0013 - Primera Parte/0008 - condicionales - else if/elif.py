print('condicional solo if, if-else')

ingreso_mensual_dolares=14800
print(f'Tu ingreso de bolsillo es u$s{ingreso_mensual_dolares} y los gastos te los paga dios!')

if ingreso_mensual_dolares >= 1000:
    print(f'Estás bien economicamente en latinoamérica - u$s {ingreso_mensual_dolares} mensuales')
if ingreso_mensual_dolares >= 10000:
    print(f'Estás bien económicamente en cualquier parte del planeta tierra - u$s {ingreso_mensual_dolares} mensuales')
else:
    print(f'Sos pobre en el resto del mundo - u$s {ingreso_mensual_dolares} mensuales')  
    
# como puedo modificarlo para que me muestre solo un texto????
# en el texto anterior si ganas 2000 dólares muestra que estoy bien en latinoamérica 
# y que soy pobre

# el concepto 'else if' existe en python
# pero no existe dicha sintaxis
# en python se utiliza 'elif'

print('condicional if-elif-else')
print('Solo Ingresos: comparativa mundial')
# ingreso_mensual_dolares=5000

if ingreso_mensual_dolares > 100000:
    print(f'Estás bien económicamente en cualquier parte del planeta tierra - u$s {ingreso_mensual_dolares} mensuales')
elif ingreso_mensual_dolares > 1000:
    print(f'Estás bien economicamente en latinoamérica - u$s {ingreso_mensual_dolares} mensuales')
else:
    print('Sos pobre')  
    
#  1:30 hs copiar los ejemplos de los paises
print('Comparativa de tu sueldo a nivel de paises')
print('Ingresos - Gastos: comparativa mundial')
gasto_mensual_dolares=110

if ingreso_mensual_dolares >= 10000:
    if ingreso_mensual_dolares - gasto_mensual_dolares < 0:
        print(f'Estás en dificit! - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
    elif ingreso_mensual_dolares - gasto_mensual_dolares > 3000:
        print(f'Estás bien! - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
    else:
        print(f'Estas gastando mucho, puede que no te alcance! - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
elif ingreso_mensual_dolares - gasto_mensual_dolares > 1000:
    print(f'Estás bien en latinoamérica - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
elif ingreso_mensual_dolares - gasto_mensual_dolares > 500:
    print(f'Sobrevivís en Argentina - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
elif ingreso_mensual_dolares - gasto_mensual_dolares > 300:
    print(f'Sobrevivís en Venezuela - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
elif ingreso_mensual_dolares - gasto_mensual_dolares > 0 and ingreso_mensual_dolares - gasto_mensual_dolares <= 300:
    print(f'Sos indigente - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')
else:
    print(f'Estas en deficit - u$s {ingreso_mensual_dolares - gasto_mensual_dolares}')