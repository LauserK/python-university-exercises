import random;

def convertir_numero_base(numero, base):
    """
    numero - int: es el numero al cual se quiere cambiar de base
    base - int(1 - 16): es la base a la cual se cambiara el @numero

    Convierte un numero a otra base dada 
    """    
    # verificamos si la base esta dentro de los parametros
    if (base >= 1 and base <= 16):
        resultado = ''
        # usamos un vector para determinar el valor a agregar
        # usado mas que todo por los valores en base 16 (HEXADECIMAL)
        vectorElemento = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
        # mientras el cociente sea distinto a 0
        while ((numero // base) != 0):
            # obtenemos el residuo
            op = numero % base    
            # generamos resultado siempre poniendo el valor a la izquierda del 
            # anterior    
            resultado = "{0}{1}".format(vectorElemento[op], resultado)
            # se reduce el numero
            numero //= base
        # retorna el numero convertido a la nueva base
        return "{0}{1}".format(numero, resultado)
    else:
        # si no esta en los parametros retorna un valor vacio
        return ""

def imprimir_matriz(matriz, n, m):
    for i in range(n):
        for j in range(m):
            print "{0:10}".format(matriz[i][j]), 
        print("\n")

n = int(input("Ingrese el numero de fila: "))
m = int(input("Ingrese el numero de columna: "))
matriz = [[0] * m for i in range(n)]
matriz_bin = [[0] * m for i in range(n)]
matriz_octal = [[0] * m for i in range(n)]
matriz_hex = [[0] * m for i in range(n)]


for i in range(n):
    for j in range(m):
        matriz[i][j] = random.randint(50,999)
        matriz_bin[i][j] = convertir_numero_base(matriz[i][j], 2)
        matriz_octal[i][j] = convertir_numero_base(matriz[i][j], 8)
        matriz_hex[i][j] = convertir_numero_base(matriz[i][j], 16)

print('Matriz Decimal')
imprimir_matriz(matriz, n, m)

print('Matriz Binaria')
imprimir_matriz(matriz_bin, n, m)

print('Matriz Octal')
imprimir_matriz(matriz_octal, n, m)

print('Matriz Hexa')
imprimir_matriz(matriz_hex, n, m)