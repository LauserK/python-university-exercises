"""
Elabore un programa que cargue una matriz cuadrada de 4*4 de manera
aleatoria y que calcule y muestre la matriz el mayor y menor de la
matriz con su posicion, un vector principal que guarde elementos de la
diagonal principal y secundaria y de ese vector muestre la suma de todo
los digitos y cantidad de digitos pares
"""

import random
columnas = 4
filas = 4
matriz = [[0] * columnas for i in range(filas)] # declaracion M4*4
vector_diagonal_principal = [0]*columnas
vector_diagonal_secundaria = [0]*columnas
vector_diagonal_resultante = [0]*columnas
mayor = 0
menor = 0
pos_fila_mayor = 0
pos_fila_menor = 0
pos_columna_mayor = 0
pos_columna_menor = 0
suma_digitos = 0
cantidad_pares = 0

#carga de la matriz
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(10, 70)

# set valores iniciales
mayor = matriz[0][0]
menor = matriz[0][0]

# calculo
for i in range(filas):
    for j in range(columnas):
        if i == j:
            # si el indice pertenece a un miembro de la diagonal p
            # la guardamos en el vector
            vector_diagonal_principal[i] = matriz[i][j]

        if i+j == columnas - 1:
            # si el indice pertenece a un miembro de la diagonal s
            # la guardamos en el vector
            vector_diagonal_secundaria[i] = matriz[i][j]
        # Suma del vector principal con el vector secundario
        op = vector_diagonal_principal[i] + vector_diagonal_secundaria[i]
        vector_diagonal_resultante[i] = op

        # Calcular numero mayor
        if matriz[i][j] > mayor:
            mayor = matriz[i][j] # asignamos valor como mayor
            pos_fila_mayor = i # asignamos la posicion en la fila
            pos_columna_mayor = j # asignamos la posicion en la columna

        # Calcular numero menor
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_fila_menor = i # asignamos la posicion en la fila
            pos_columna_menor = j # asignamos la posicion en la columna

# calcular cantidad pares y suma de digitos
for i in range(filas):
    # ya que se va a modificar el numero usamos una variable auxiliar
    aux = vector_diagonal_resultante[i]
    while aux != 0:
        dig = aux % 10
        suma_digitos += dig # suma de digitos del numero
        if dig % 2 == 0:
            cantidad_pares += 1
        aux //= 10


print('Resultados')
for i in range(filas):
    for j in range(columnas):
        print matriz[i][j],
    print "\n"

print("El mayor de la matriz es {0} y esta en la posicion {1},{2}".format(mayor, pos_fila_mayor, pos_fila_mayor))
print("El menor de la matriz es {0} y esta en la posicion {1},{2}".format(menor, pos_fila_menor, pos_fila_menor))

print('Vector Diagonal principal')
for j in range(columnas):
    print vector_diagonal_principal[j],
print("\n")

print('Vector Diagonal secundaria')
for j in range(columnas):
    print vector_diagonal_secundaria[j],
print("\n")


print('Vector resutante')
for j in range(columnas):
    print vector_diagonal_resultante[j],
print("\n")
