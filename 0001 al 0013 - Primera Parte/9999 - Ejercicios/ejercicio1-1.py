#  Ejercicios prácticos

# El timing para ver estos conceptos en python en un curso de corrido es de 
# 2,5 hs de corrido como mínimo, 7 hs como máximo y 4 hs en promedio, este 
# curso lo logró en 1,5 hs.
# a) cuanta diferencia en porcentajes hay: 
#     - entre el mas rapidos de los cursos (2,5) y este curso (1.5)
#     - el mas lento de los otros cursos (7)
#     - el promedio de los cursos (4)
    
# b) teniendo en cuenta que el promedio de crudo es de 5 hs y con edicion lo convierten
#     en 4 horas y el crudo de este video fue de 3,5 hs y se redujo a 1,5 hs
#     - que porecentaje se reduce en
#         * el promedio de los cursos
#         * este curso

# c) Ver 10 hs de este curso sería equivalente a ver... cuantas horas de los otros cursos?
#     y ver 10 hs de otros cursos cuantas horas equivalen para este curso?


otros_cursos_min = 2.5
otros_cursos_max = 7.0
otros_cursos_prom = 4.0
este_curso = 1.5

print('Ejercicio 1 - Resoluciones')
# round(numero,2) --> redondea el valor a dos digitos no se usa porque si da un 
# numero redondo ej: 60  -> 60.0% y necesito 60.00%
# Con el uso de   :.2f   , te aseguras de que los números 
# se muestren siempre con dos decimales, incluso si son enteros.
print(f'''a) Mostrar el porcentaje del curso más rapido con este curso:
        Este curso es el {100 - (este_curso * 100.0)/otros_cursos_min:.2f}% más rapido que el curso de menor duración de otros.
        Este curso es el {100 - (este_curso * 100.0)/otros_cursos_prom:.2f}% más rapido que el curso promedio en duración de otros.
        Este curso es el {100 - (este_curso * 100.0)/otros_cursos_max:.2f}% más rapido que el curso de mayor duración de otros.
        ''')
# formula       otroCurso --- 100%
#               esteCurso --- x%         esteCurso*100/otroCurso = 60%
#                               para saber cuan rápido es 100 - 60 = 40% más rápido
# otra forma de redondear sin redondear con :.2f es
# 100 - (este_curso * 1000.0)//otros_cursos_min/10.0

print({100 - (este_curso * 10000.0)//otros_cursos_prom/100.0})

crudo_media=5.0
edicion_media=4.0
crudo_dalto=3.5
edicion_dalto=1.5

print(f'''b) Mostrar el porcentaje de reducción del video en crudo al video editado:
        El promedio de los cursos eliminó un {(100-(edicion_media * 100.0)/crudo_media):.2f}% de material vacío.
        Este curso eliminó un {(100-(edicion_dalto * 100.0)/crudo_dalto):.2f}% de material vacío.
        ''')

print(f'''c) 1 - Ver 10 horas del curso de Dalto equivale a ver:
        10 hs. del curso de dalto equivale a ver {10.0/este_curso:.2f} veces.
        El curso mínimo {(10.0/otros_cursos_min)*(10.0/este_curso):.2f} horas.
        El curso promedio {(10.0/otros_cursos_prom)*(10.0/este_curso):.2f} horas.
        El curso maximo {(10.0/otros_cursos_max)*(10.0/este_curso):.2f} horas. 
        ''')

# El curso promedio {(otros_cursos_prom * 100 // este_curso/10):.2f} horas.
print(f'El curso promedio {(otros_cursos_prom * 100 // este_curso/10):.2f} horas.')

print(f'''c) 2 - Ver diez hs de otros cursos es lo mismo que ver:
      Un curso mínimo equivale a ver {(10.0/otros_cursos_min)*este_curso:.2f}hs de cursos de Dalto.
      Un curso promedio equivale a ver {(10.0/otros_cursos_prom)*este_curso:.2f}hs de cursos de Dalto.
      Un curso máximo equivale a ver {(10.0/otros_cursos_max*este_curso):.2f}hs de cursos de Dalto.
      ''')



# 2:50:00 realizar primero los ejercicios y luego continuar