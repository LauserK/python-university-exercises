# -*- coding: utf-8 -*-
"""
ENUNCIADO Dado un archivo de datos llamado NOTAS.TXT (El archivo de datos .TXT de entrada, debe crearlo
utilizando un editor de texto, como por ejemplo bloc de notas), que contiene las notas de todos los estudiantes
de una sección y, por cada línea en el archivo, se tiene la información de cada estudiante:
CEDULA1, NOMBRE1, NOTA1, NOTA2, NOTA3
…
…
CEDULAn, NOMBREn, NOTA1, NOTA2, NOTA3
Elabore un programa en Python que permita determinar e imprimir en un archivo de datos llamado
REPORTE.TXT, lo siguiente:

1. Cédula, Nombre y Nota Final de los estudiantes aprobados, sabiendo que la nota final es el promedio de las
tres evaluaciones.
2. Promedio de Nota Final de la sección.
3. Cédula y Nombre del estudiante con mayor Nota Final.
4. Porcentaje de estudiantes aprobados por cada Evaluación.
"""
notas = open('NOTAS.txt')
suma_notas = 0
lineas = 0
promedio = 0
cedula_mayor = ""
nombre_mayor = ""
nota_mayor = 0
porcentaje_1 = 0
cant_1 = 0
porcentaje_2 = 0
cant_2 = 0
porcentaje_3 = 0
cant_3 = 0

# Creamos el reporte con el flag w para indicar que se va a escribir
reporte = open('REPORTE.txt', 'w')

for registro in notas:
    # creamos array de datos de la linea
    campos = registro.split(',')
    cedula = campos[0]
    nombre = campos[1]
    nota_1 = int(campos[2])
    nota_2 = int(campos[3])
    nota_3 = int(campos[4])
    nota_final = (nota_1 + nota_2 + nota_3) / 3

    suma_notas += nota_final
    lineas += 1

    if nota_final > nota_mayor:
        nombre_mayor = nombre
        cedula_mayor = cedula
        nota_mayor = nota_final

    # Si aprobo el curso escribir en el archivo reporte
    if nota_final >= 10:
        reporte.write('{0},{1},{2}\n'.format(cedula, nombre, nota_final))

    if nota_1 >= 10:
        cant_1 += 1

    if nota_2 >= 10:
        cant_2 += 1

    if nota_3 >= 10:
        cant_3 += 1


if lineas != 0:
    promedio = suma_notas / lineas

if lineas != 0:
    porcentaje_1 = (cant_1 * 100) / lineas
    porcentaje_2 = (cant_2 * 100) / lineas
    porcentaje_3 = (cant_3 * 100) / lineas

# escribir demas peticiones en el archivo de texto
reporte.write('PROMEDIO FINAL SECCION: {0}\n'.format(promedio))
reporte.write('{0},{1}\n'.format(cedula_mayor, nombre_mayor))
reporte.write('{0}%,{1}%,{2}%\n'.format(porcentaje_1, porcentaje_2, porcentaje_3))
reporte.close();