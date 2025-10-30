
# CLASE 2 
# Ejercicios


# 1a
numeros = list( range(1,11)) 
#print(f"\nEj.1a \nnumeros = {numeros}")
  
# 1b
meses = tuple( range(1,13))
#print(f"\nEj.1b \nmeses = {meses}")

# 1c
notas =  { "Ale": 9, "Juan": 6, "Ana": 8}
#print(f"\nEj.1c \nnotas = {notas}")

 # 1d
conjunto = [ 1,1,2,2,3,3,4]
numeros_unicos = frozenset( conjunto)
#print(f"\nEj.1d \n {conjunto} \n {numeros_unicos}")

print()


#2a. Modificar uno de los valores del diccionario notas
# (cambiar la nota de uno de los estudiantes).
notas =  { "Ale": 9, "Juan": 6, "Ana": 8}
print(f"\nEj.2a \nnotas = {notas}")
notas["Ale"] = 10
print(f"\nnotas = {notas}")


# 2b. Acceder a los elementos de la lista numeros y 
# 2c. mostrar todos los números pares utilizando un bucle.
numeros = list( range(1,11)) 
print("\nEj. 2b")
for i in numeros:
    if i % 2 == 0:
       print(f"par {i}")


# 2c. Acceder al primer mes de la tupla meses y al último mes. 
#     Mostrar ambos.
print("\nEj.2c \nprimero:", meses[0])
print("ultimo:", meses[-1])


# 3a. Definir una función normal llamada
# multiplicar_por_dos que tome un número y lo
# multiplique por 2. Utilizar esta función para crear una
# nueva lista llamada dobles , que contenga los dobles de
# los números en la lista numeros .

def multiplicar_por_dos(n):
    return n*2

numeros = list( range(1,11)) 
dobles = []
for i in range(1, len(numeros)+1):
    dobles.append( multiplicar_por_dos(i) )

print( "\nEj. 3a\n dobles = ", dobles)


# 3b. Definir una función lambda que haga lo mismo y
#  utilizarla para crear una nueva lista llamada
#  dobles_lambda , que contenga los dobles de los
# números en la lista numeros
 
#dobles_lambda = [x*2 for x in range(10)]
dobles_lambda = [x*2 for x in numeros]
print("\nEj. 3a\n dobles_lambda = ", dobles_lambda)



'''
Ej.4 - Comprehensions
a. Utilizar list comprehensions para crear una lista
llamada cuadrados que contenga los cuadrados de los
números en la lista numeros .
'''
cuadrados = [x*x for x in numeros]
print("\nEj 4a cuadrados =", cuadrados)


'''
Ej 4b. Utilizar dict comprehensions para crear un
diccionario llamado cubos que contenga los números
de la lista numeros como claves y sus cubos como
valores.
'''
cubos = {x: x*x*x for x in numeros}
print("\nEj 4b cubos = ", cubos)
print( type(cubos))


'''
Ej.5 - Comparación de resultados
5a. Mostrar las listas dobles , dobles_lambda y
cuadrados . Comparar sus resultados y argumentar cuál
es el mejor método.


Ej. 5b. Imprimir el diccionario cubos y comparar con la
creación de un diccionario usando un método
convencional.

'''



'''
--- RESUMEN ---
#Funciones Lambda
#Son funciones anónimas de código compacto
suma = lambda x, y: x + y

#List Comprehension
#Permite la creación de listas de manera concisa y eficiente
cuadrados = [x**2 for x in range(10)]


#Dict Comprehension
#Permiten la creación de diccionarios de forma compacta
cubos = {x: x**3 for x in range(10)}
'''
