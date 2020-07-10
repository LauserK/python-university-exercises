personal = open('personal.txt')
mas_tarde_n = ''
mas_tarde_a = ''
hora_tarde = 0
min_tarde = 0
cant_re_manana = 0
cant_re_tarde = 0
menos_h = 0
menos_m = 0
menos_nombre = ''
menos_apellido = ''
salida = open('resultados.txt', 'w')

salida.write('A\n')
for linea in personal.readlines():
    datos = linea.split()
    cedula = datos[0]
    apellido = datos[1]
    nombre = datos[2]
    area = datos[3]
    h_llegada = int(datos[4])
    m_llegada = int(datos[5])
    h_salida = int(datos[6])
    m_salida = int(datos[7])
    turno = 'MANANA'
    retardo_h = 0
    retardo_m = 0
    h_trabajadas = 0
    m_trabajados = 0

    if h_llegada >= 14:
        turno = 'TARDE'

    if turno == 'MANANA':
        retardo_h = h_llegada - 8
        if m_llegada > 0 and h_llegada >= 8:
            retardo_m = m_llegada
    else:
        retardo_h = h_llegada - 15
        if m_llegada > 0 and h_llegada >= 15:
            retardo_m = m_llegada

    if retardo_m > 0 or retardo_h > 0:
        if turno == 'MANANA':
            cant_re_manana += 1
        else:
            cant_re_tarde += 1

        # B
        if retardo_m > min_tarde and retardo_h >= hora_tarde:
            min_tarde = retardo_m
            mas_tarde_n = nombre
            mas_tarde_a = apellido

        if retardo_h >= hora_tarde:
            hora_tarde = retardo_h
            mas_tarde_n = nombre
            mas_tarde_a = apellido

    # horas trabajadas
    #h_trabajadas = h_salida - h_llegada
    #if h_trabajadas > 4:
    #print(nombre, str(h_trabajadas), m_trabajados)
    linea_s = '{0} {1} {2} {3} {4} {5} \n'.format(area, apellido, nombre, turno, h_llegada, m_llegada)
    salida.write(linea_s)

# B
salida.write('B\n')
salida.write('{0} {1} {2} {3} \n'.format(mas_tarde_n, mas_tarde_a, hora_tarde, min_tarde))

# C
salida.write('C\n')
if cant_re_manana > cant_re_tarde:
    salida.write('MANANA CON {0} RETARDOS\n'.format(cant_re_tarde))
elif cant_re_tarde > cant_re_manana:
    salida.write('TARDE CON {0} RETARDOS\n'.format(cant_re_tarde))
else:
    salida.write('AMBOS TURNOS CON {0} RETARDOS\n'.format(cant_re_tarde))

salida.write('D\n')
salida.close();
personal.close();
print('Proceso realizado')
