import math

def get_component(v1,v2):
	"""
	Obtener componente de un vector
	"""
	return v2-v1

def get_module_radio(x,y):
	"""
	Obtener modulo de un vector 
	Tambien se puede obtener radio
	"""
	return math.sqrt((x**2) + (y**2))

def get_angulo(x,y):
	if x == 0:
		return 0
	return math.atan(y/x)

def vector_to_polar(x,y,vector_name):
	angulo = get_angulo(x,y)
	radio = get_module_radio(x,y)
	print(vector_name + '(' + str(x) + ',' + str(y) + ') a cordenadas polares (' + str(radio) +',' + str(angulo) +'°)')

def vector():
	""""
	Dados los siguientes puntos A=(x1, y1) y B(x2, y2) 
	Hallar los componentes  y módulo de ese vector  AB=(x, y)
	Si pido otro d=(x1, y1) y E(x2, y2)    
	Hallar los componentes  y módulo de ese vector  DE=(x, y)
	HALLAR 2AB + 4DE
	DE AB=(x, y)  Y DE=(x, y) DETERMINA CORDENADAS POLARES
	"""
	print('Ingrese datos del punto A')
	x1 = int(input('x: '))
	y1 = int(input('y: '))
	print('Ingrese datos del punto B')
	x2 = int(input('x: '))
	y2 = int(input('y: '))

	xAB = get_component(x1,x2)
	yAB = get_component(y1,y2)
	moduleAB = get_module_radio(xAB, yAB)

	print('Componentes del vector AB=('+str(xAB)+','+str(yAB)+')')
	print('Modulo del vector |AB|=' + str(moduleAB))

	print('Ingrese datos del punto D')
	x3 = int(input('x: '))
	y3 = int(input('y: '))
	print('Ingrese datos del punto E')
	x4 = int(input('x: '))
	y4 = int(input('y: '))

	xDE = get_component(x3,x4)
	yDE = get_component(y3,y4)
	moduleDE = get_module_radio(xDE, yDE)

	print('Componentes del vector DE=('+str(xDE)+','+str(yDE)+')')
	print('Modulo del vector |DE|=' + str(moduleDE))

	# 2AB + 4DE
	xN = 2*xAB + 4*xDE
	yN = 2*yAB + 4*yDE

	print('el vector 2AB + 4DE = ('+str(xN)+','+str(yN)+')')	

	vector_to_polar(xAB, yAB, 'AB')
	vector_to_polar(xDE, yDE, 'DE')

def primo(numero):
	prime = True
	for i in range(2,numero):
		if (numero % i) == 0:
			prime = False
			break
	return prime


def desglose(numero):
	"""
	OTRA FUNCION QUE DESGLOSE UJN NUMERO DE CUALQUIER CIFRA Y DETERMINE
	SI EL NUMERO ES PRIMO
	PROPORCION DE DIGITOS IGUAL A 2
	SUMA DE GITITOS PRIMOS
	MAYOR DIGITO PAR
	MENOR DIGITO IMPAR
	"""

	# primo?
	if primo(numero):
		print('El numero',numero,'es primo')
	else:
		print('El numero',numero,'no es primo')
	sumprimos=0
	mayor =0
	menor=0
	digitos2 = 0
	num = str(numero)
	for x in num:		
		char = int(x)
		if char % 2 == 0 and char > mayor:
			mayor = char

		if char % 2 == 1 and char < menor:
			menor = char

		if char == 2:
			digitos2 += 1

		if primo(char):
			sumprimos += char

	proporcion = digitos2*100/len(num)
	print('Suma de digitos primos: ', sumprimos)
	print('mayor digito par: ', mayor)
	print('menor digito impar', menor)
	print('proporcion de digitos 2 es de: ', str(proporcion) + "%")

vector()

numero = int(input('ingrese numero a desglosar: '))
desglose(numero)