# -*- coding: utf-8 -*-
"""
En la actualidad la Organización Mundial de la Salud (OMS), tiene activada una alerta de pandemia por el
brote del virus de fiebre porcina, que a partir del 30 de abril de 2009 es llamado virus gripal A (H1N1).
Considerando que ya tenemos casos confirmados en el país, el Ministerio del Poder Popular para la Salud
activará un plan de detección de sospechosos de portadores del virus gripal A(H1N1), para lo cual se registra
en el archivo de datos fiebre.txt, la siguiente información correspondiente a todos los pacientes en las
instituciones de salud del país:
Nombre del Paciente, Nombre de la Institución Asistencial, Temperatura del Paciente, Hemoglobina y
Cantidad de Glóbulos Blancos.
Desarrolle un programa en python que procese la información antes mencionada y genere 2 archivos
llamados sospechosos.txt y nosospechosos.txt, en donde se almacenen los datos de los pacientes
sospechosos y no sospechosos respectivamente.
Además determine e imprima por pantalla:
.Porcentaje de pacientes no sospechosos.
. Nombre del paciente e institución donde se localiza el paciente con mayor cantidad de glóbulos blancos.
Consideraciones:
Se considera que un paciente es sospechoso de ser portador del virus gripal A(H1N1), si su valores son los
siguientes: la temperatura es mayor de 38 °C, la hemoglobina está por debajo de 10 mg/dl y que la cantidad
de glóbulos blancos esté por debajo de 4.000
"""

archivo = open('fiebre.txt')
sospechosos = open('sospechosos.txt', 'w')
no_sospechosos = open('nosospechosos.txt', 'w')
cantidad_pacientes = 0
cant_sospechosos = 0
porcentaje = 0
nombre_sospechoso = ""
institucion_sospechoso = ""
mayor_globulos = 0

for registro in archivo:
    campos = registro.split(',')
    nombre = campos[0]
    institucion = campos[1]
    temperatura = float(campos[2])
    hemoblogina = float(campos[3])
    globulos = int(campos[4])
    cantidad_pacientes += 1

    if temperatura > 38 and hemoblogina < 10 and globulos < 4000:
        cant_sospechosos += 1
        sospechosos.write(registro)

        if globulos > mayor_globulos:
            nombre_sospechoso = nombre
            institucion_sospechoso = institucion
            mayor_globulos = globulos

    else:
        no_sospechosos.write(registro)

if cantidad_pacientes != 0:
    porcentaje = (cant_sospechosos * 100) / cantidad_pacientes

print('Porcentaje de pacientes no sospechosos: {0}%'.format(porcentaje))
print('Nombre del paciente e institución donde se localiza el paciente con mayor cantidad de glóbulos blancos: {0} - {1}'.format(nombre_sospechoso, institucion_sospechoso)) 