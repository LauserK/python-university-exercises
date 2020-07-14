"""
Nombre: Kildare Lauser
Escuela: Computacion
"""

"""
Embotelladora  la Botellita C.A,  es una empresa que se encarga de fabricar y 
embotellar bebidas gaseosas y posteriormente distribuirlas a nivel nacional. 
Para su distribución posee en su flota un total de Cuatro (4) camiones los 
cuales están identificados por placas. La empresa dentro de su línea de producción, 
fabrica cinco (5) tipos distinto de gaseosas. Para controlar la cantidad de botellas
 que se despachan se ha diseñado una matriz denominada Despacho, la cual controla
  por el lado de las filas controla a los cuatro (4) camiones que poseen en su 
  flota y por el lado de las columnas cada uno de los cinco (5) tipos distinto 
  de gaseosas. Cada elemento de la Matriz contiene el total de cajas de gaseosas
   que ha despachado cada camión de cada tipo de refresco. Adicionalmente se posee 
   un vector denominado Precios el cual contiene el precio por caja de refresco y 
   otro vector denominado Refresco el cual contiene el total de unidades de refresco
    que hay en una caja según el tipo de gaseosa. Por último se posee un vector denominado
     Placas el cual contiene la placa de cada uno de los camiones de la flota. A partir de 
     esta información se pide:
- Total de despacho por tipo de gaseosas
- Cuál es la placa del camión en donde se despacharon más cajas de gaseosas y cuantos
repartieron esa misma cantidad
- Un vector que contenga el total de bolívares despachado por tipo de gaseosa
- Cuantas botellas se despacharon entre los camiones 2 y 3
- Un vector que almacene el total de botellas despachada por camión.
- Cual tipo de gaseosa tuvo más demanda en despacho
"""
import random

placas = [0]*4
precios = [0]*5
refresco = [0]*5
despacho = [[0]*5 for f in range(4)]
total_despacho = [0]*5
vector_despacho_total_camion = [0]*4
vector_bolivares = [0] * 5

mayor_cantidad = 0
pos_mas_cantidad = 0
mismos_mas_cantidad = 0
total_camion_2_3 = 0
mayor_gaseosa = 0
pos_mayor_gaseosa = 0

# set placas
placas[0] = "AX2 34G"
placas[1] = "W2F 22C"
placas[2] = "22C 17A"
placas[3] = "1W2 13J"

# precios aleatorios
for i in range(5):
	precios[i] = random.randint(4, 10) * 10000

# cantidad de empaque
for i in range(5):
	refresco[i] = random.randint(1,4)*6 # numero aleatorio multiplo de 6

# cargar cantidad de cajas despachadas
for f in range(4):
    for c in range(5):
        despacho[f][c] = random.randint(2, 100)
"""
print('Matriz despacho')
for f in range(4):
    for c in range(5):
        print("{:2}".format(despacho[f][c]), end=' ')
    print()
"""

# total despachos por gaseosa
for c in range(5):
	for f in range(4):
		total_despacho[c] = total_despacho[c] + despacho[f][c]

for x in range(5):
	print('Despacho de gaseosa #{0}:{1} cajas'.format(x, total_despacho[x]))

"""
- Cuál es la placa del camión en donde se despacharon más cajas de gaseosas y cuantos
repartieron esa misma cantidad
"""
for f in range(4):
	for c in range(5):
		vector_despacho_total_camion[f] = vector_despacho_total_camion[f] + despacho[f][c]

mayor_cantidad = vector_despacho_total_camion[0]
for i in range(4):	
	if vector_despacho_total_camion[i] > mayor_cantidad:
		mayor_cantidad = vector_despacho_total_camion[i]
		pos_mas_cantidad = i		

for i in range(4):
	if vector_despacho_total_camion[i] == mayor_cantidad:
		mismos_mas_cantidad += 1					

print('\nEl camion con mas cajas despachadas fue el de placa: {0} y en total: {1} camiones reparieron la misma cantidad'.format(placas[pos_mas_cantidad], mismos_mas_cantidad))		

#- Un vector que contenga el total de bolívares despachado por tipo de gaseosa
for f in range(4):
	for c in range(5):
		vector_bolivares[c] = vector_bolivares[c] + (precios[c]*despacho[f][c])

print('\nVector total de bolivares despachado por gaseosa:')
for x in range(5):
	print("{0}".format(vector_bolivares[x]), end=' ')	

#- Cuantas botellas se despacharon entre los camiones 2 y 3
for f in range(1,2+1):
	for c in range(5):
		total_camion_2_3 += (despacho[f][c] * refresco[c])

print('\n\nEl total despachado de botellas entre los camiones 2 y 3 es de {0}unds'.format(total_camion_2_3))

#- Un vector que almacene el total de botellas despachada por camión.
total_botellas_camion = [0]*4
print('\n\nVector total de botellas despachada por camion')
for f in range(4):
	for c in range(5):
		total_botellas_camion[f] = total_botellas_camion[f] + (despacho[f][c] * refresco[c])
	# imprimir vector total botellas
	print(total_botellas_camion[f], end=" ")
print()
	

# Cual tipo de gaseosa tuvo más demanda en despacho
for i in range(5):
	if total_despacho[i] > mayor_gaseosa:
		mayor_gaseosa = total_despacho[i]
		pos_mayor_gaseosa = i

print('\n\nEl tipo de gaseosa que tuvo mas demanda en el despacho fue la gaseosa #{0} con {1} cajas vendidas'.format(pos_mayor_gaseosa, mayor_gaseosa))