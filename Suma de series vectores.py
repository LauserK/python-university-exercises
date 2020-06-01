def get_n():
    n = int(raw_input('Meta n:'))
    if (n < 1):
        print('Error, debe ser positivo')
        get_n()
    else:
        return n

def get_value(nombre):
    return int(raw_input('Meta valor de {0}:'.format(nombre)))

def print_vector(vector, mensaje):
    print mensaje
    for x in vector:
        print x,
    print '\n'

n = get_n()
x = get_value('x')
y = get_value('y')
z = get_value('z')
ss = 0
contador = 0
repetido = 0
t = [0]*(n+1)

for i in range(1, n+1):
    numerador = (x**i)*(z**i-1)
    deominador = float

    if i==0:
        denominador = y**n
    else:
        if repetido == 2:
            repetido = 0
            contador += 1

        denominador = y**(n-contador)

        repetido += 1

    operacion = numerador/denominador
    t[i-1] = operacion

t[n]=((z**(n-1))*(x**n))

for x in t:
    ss += x

print('Suma d ela serie: {0}'.format(ss))
print_vector(t, 'Vector terminos: ')
