import random
def imprimir_matriz(matriz, n, m):
    for i in range(n):
        for j in range(m):
            print "{0:4}".format(matriz[i][j]), 
        print("\n")
def primo(x):
    c = 0
    for i in range(1, x+1):
        if x % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

n = int(input("Ingrese el numero de fila: "))
m = int(input("Ingrese el numero de columna: "))
matriz = [[0] * m for i in range(n)]
matriz_primos = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        matriz[i][j] = random.randint(2,1500)
        matriz_primos[i][j] = matriz[i][j] if primo(matriz[i][j]) else 0

print('Matriz')
imprimir_matriz(matriz, n, m)

print('Matriz primo')
imprimir_matriz(matriz_primos, n, m)