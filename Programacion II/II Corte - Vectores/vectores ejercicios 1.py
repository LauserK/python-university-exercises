def vectora():
    # Carga de vector de tamano 3
    vector = [0]*3

    for i in range(3):
        valor = int(input('Cargue valor vector[{0}]: '.format(i)))
        vector[i] = valor

    # imprimir vector
    print 'Vector'
    for x in vector:
        print x,


def vector2():
    size = int(input('Ingrese tamano del vector a: '))
    a = [0]*size

    for i in range(size):
        valor = int(input('Cargue valor vector[{0}]: '.format(i)))
        a[i] = valor

    #imprimir
    print 'Vector a'
    for x in a:
        print x,

def vectorc():
    size = int(input('Ingrese tamano del vector a: '))
    a = [0]*size
    b = [0]*size
    c = [0]*size
    bigger = 0
    pos = 0

    # datos a
    for i in range(size):
        valor = int(input('Cargue valor a[{0}]: '.format(i)))
        a[i] = valor

    #datos b
    for i in range(size):
        valor = int(input('Cargue valor b[{0}]: '.format(i)))
        b[i] = valor

    for i in range(size):
        c[i] = a[i]+b[i]

        if c[i] > bigger:
            bigger = c[i]
            pos = i

    # mostrar c
    print('vector resultante de a+b')
    for x in c:
        print x,

    print('mayor es {0} en la posicion {1}'.format(bigger, pos))

def vectoresd():
    size = 6
    a = [0]*size
    b = [0]*size
    c = [0]*size

    # datos a
    for i in range(size):
        valor = int(input('Cargue valor a[{0}]: '.format(i)))
        a[i] = valor

    #datos b
    for i in range(size):
        valor = int(input('Cargue valor b[{0}]: '.format(i)))
        b[i] = valor

    #calcular 6
    for i in range(size):
        if i%2 == 0:
            c[i+1] = a[i]+b[i]
        else:
            c[i-1] = a[i]-b[i]

    # mostrar c
    print('vector resultante de a+b')
    for x in c:
        print x,

def vectorese():
    size = 6
    nombre = [0]*6
    notas = [0]*6
    promedio = 0
    mayor = 0
    menor = 0
    notasum = 0
    possup = 0
    posmeno = 0
    aprobadas = 0
    reprobadas = 0

    # datos a
    for i in range(size):
        valor = raw_input('Cargue valor nombre[{0}]: '.format(i))
        nombre[i] = valor

    #datos b
    for i in range(size):
        valor = int(input('Cargue valor nota[{0}]: '.format(i)))
        notas[i] = valor
        notasum += notas[i]

        if i == 0:
            menor = notas[i]
            posmeno = i

        if notas[i] > mayor:
            mayor = notas[i]
            possup = i

        if notas[i] < menor:
            menor = notas[i]
            posmeno = i

        if notas[i] >= 10:
            aprobadas += 1

        if notas[i] < 10:
            reprobadas += 1

    print()

    # mostrar nombre
    print('Vector Nombre')
    for x in nombre:
        print x,

    # mostrar notas
    print('\nVector Notas')
    for x in notas:
        print x,

    promedio = notasum/size

    print('\nPromedio del curso: {0} pts'.format(promedio))
    print('Aprobados: {0} Reprobados: {1}'.format(aprobadas, reprobadas))
    print('Mayor nota: {0} del estudiante: {1} posicion: {2}'.format(mayor, nombre[possup], possup))
    print('Menor nota: {0} del estudiante: {1} posicion: {2}'.format(menor, nombre[posmeno], posmeno))


