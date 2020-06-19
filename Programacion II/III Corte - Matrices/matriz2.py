"""
Suma de matrices
"""

import random

n = int(input("Ingrese el numero de fila: "))
m = int(input("Ingrese el numero de columna: "))
matriz = [[0] * m for i in range(n)]
matriz1 = [[0] * m for i in range(n)]
matriz2 = [[0] * m for i in range(n)]
sfila = [0]*n

for i in range(n):
    for j in range(m):
        matriz[i][j] = random.randint(1,8)
        matriz1[i][j] = random.uniform(1,8)
        matriz2[i][j] = matriz[i][j] + matriz1[i][j]
        sfila[i] = sfila[i] + matriz2[i][j]

print "Matriz cargada"
for i in range(n):
    for j in range(m):
        print matriz[i][j],
    print "\n"

print "Matriz 1 cargada"
for i in range(n):
    for j in range(m):
        print "{0:2.2f}".format(matriz1[i][j]),
    print "\n"

print "Matriz suma"
for i in range(n):
    for j in range(m):
        print "{0:2.2f}".format(matriz2[i][j]),
    print "\n"
    print "{0:2.2f}".format(sfila[i])
