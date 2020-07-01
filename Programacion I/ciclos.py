"""
Desarolle un programa en Python para registrar ventas de una tienda
de repuestos de todo tipo, Determinar:
1- Monto total de repuestos vendidos
2- Cantidad total de repuestos vendidos
3- Cantidad total de repuestos del ano 2019
4- Monto total del repuesto de marca ford
"""
import random

# Definicion de variables
monto_total_vendido = 0
cantidad_repuestos = 0
cantidad_repuestos_2019 = 0
monto_total_ford = 0
precio_1 = 0
precio_2 = 0
precio_3 = 0
precio_4 = 0
pregunta = True

# Proceso
print('Bienvenido a Auto repuestos 2020 C.A.')
while pregunta:
    print("""Repuestos dispoibles:\n
    1- Amortiguador, 2- Caja de cambios, 3- Disco de freno, 4- Bateria\n
    5- Camara, 6- Retrovisor\n""")

    repuesto = int(input('Ingrese cod del repuesto: '))
    if repuesto > 0 and repuesto <= 6:
        ano_repuesto = int(input('Ingrese ano del repuesto requerido (Ej: 2020): '))

        if ano_repuesto >= 1980 and ano_repuesto <= 2020:
            # precio random
            precio_1 = random.randint(10, 1000)
            for marca in range(0,5):
                if marca == 2:
                    precio_2 = precio_1 * 1.5
                elif marca == 3:
                    precio_3 = precio_1 * 1.1
                elif marca == 4:
                    precio_4 = precio_1 * 0.9

            print('Marcas disponibles: 1- Mitsubishi ${0}, 2- Toyota ${1}, 3- Ford ${2}, 4- Mazda ${3}'.format(precio_1, precio_2, precio_3, precio_4))
            marca = int(input('Ingrese codigo de marca: '))
            if marca > 0 and marca <= 4:
                cant = int(input('Ingrese la cantidad de repuesto deseada: '))

                if cant > 0:
                    monto = 0

                    if marca == 1:
                        monto = precio_1 * cant
                    elif marca == 2:
                        monto = precio_2 * cant
                    elif marca == 3:
                        monto = precio_3 * cant
                    else:
                        monto = precio_4 * cant

                    # requerimientos
                    if ano_repuesto == 2019:
                        cantidad_repuestos_2019 += cant

                    if marca == 3:
                        monto_total_ford += monto

                    monto_total_vendido += monto
                    cantidad_repuestos += cant

                else:
                    print('Cantidad invalida')
            else:
                print('Marca inexistente')
        else:
            print('Error ano inexistente')
    else:
        print('Error codigo de repuesto no existe')

    print('Posees en cuenta ${0} pendientes por cancelar'.format(monto_total_vendido))

    # Condicion del ciclo
    s = int(input('Desea comprar otro repuesto? Ingrese 1 para Si, 2 para No: '))
    if s == 2:
        pregunta = False

# Imprimir requerimientos
print('\nTotales:')
print('Monto total de repuestos vendidos: ${0}'.format(monto_total_vendido))
print('Cantidad total de repuestos vendidos: {0}'.format(cantidad_repuestos))
print('Cantidad total de repuestos del ano 2019: {0}'.format(cantidad_repuestos_2019))
print('Monto total del repuesto de marca ford: ${0}'.format(monto_total_ford))
