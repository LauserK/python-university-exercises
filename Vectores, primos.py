def get_tamano():
    size = int(raw_input('Tamano del vector (debe ser par y positivo):'))
    if (size <= 1 and size % 2 != 0):
        print('Error, tamno no aceptado, ingrese nuevamente')
        tamano()
    else:
        return size

def set_valores(nombre, size):
    vector = [0]*size

    for i in range(size):
        vector[i] = int(input('Inserte valor para {0}[{1}]: '.format(nombre, i)))

    return vector

def print_vector(vector, mensaje):
    print mensaje
    for x in vector:
        print x,
    print '\n'

def get_vector_c(a,b,size):
    size2 = size*2
    c = [0]*size2
    pos = 0
    contador = 0
    i = 0
    ladoA = True
    while i < size2:
        if ladoA:
            c[i] = a[pos]
        else:
            c[i] = b[pos]

        i+=1
        pos += 1
        contador += 1

        if contador == 2:
            pos -= 2
            contador = 0
            ladoA = not ladoA

            if ladoA == True:
                pos += 2

    return c

def primo(x):
    c = 0
    for i in range(1, x+1):
        if x % i == 0:
            c += 1

    if c == 2:
        return True
    else:
        return False

def get_vector_primo(vector):
    cantidad_primos = 0
    pos = 0
    for x in vector:
        if primo(x):
            cantidad_primos += 1

    p = [0]*cantidad_primos

    for x in vector:
        if primo(x):
            p[pos] = x
            pos+=1

    return p


size = get_tamano()
a = set_valores('a', size)
b = set_valores('b', size)
c = get_vector_c(a,b,size)
p = get_vector_primo(c)

print_vector(a, 'vector a: ')
print_vector(b, 'vector b: ')
print_vector(c, 'vector generado c: ')
print_vector(p, 'vector primo p: ')
