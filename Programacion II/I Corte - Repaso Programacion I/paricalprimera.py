"""
1.- Elabore un programa en Python que permita. Poder realizar elecciones presidenciales de los diferentes colegios profesionales que existan. Ejemplo de colegios (Abogados, Ingeniero, Medico, Administración, Arquitectos). En el evento siempre van a competir tres candidatos ejemplo candidatos (A, B, C). Para poder ejercer el voto el profesional debe estar solvente. Por cada colegio determine:
Mostrar el nombre del colegio que está realizando las elecciones en ese momento
Quién gano con cuantos votos y que porcentaje
Porcentaje de votos nulos. Voto nulo es una opción diferente a los candidatos
Cuantos Profesionales están morosos, moroso es el que debe
Porcentaje de mujeres que votaron por el candidato A.
Cuantos hombres están morosos

Nota es un ciclo anidado uno controla los colegios, el usuario decide le permanencia o no, y el otro ciclo controla los “N” profesionales que pueden votar.
"""
mantener = True
while(mantener):
	nombre_colegio = input('Ingrese el nombre del colegio: ')
	print("------------------------------------------------------------------------")
	print('Bienvenido a las elecciones presidenciales del colegio de', nombre_colegio)
	print("------------------------------------------------------------------------")

	votos_a = 0
	votos_b = 0
	votos_c = 0
	votos_nulos = 0
	morosos = 0	
	mujeres_a = 0
	mujeres = 0
	hombres_morosos = 0
	cantidad_profesionales = int(input("¿Cuantos profesionales van a votar?: "))

	for profesional in range(0, cantidad_profesionales):
		print('Bienvenido profesional en votar #', profesional)

		# SEXO
		sexo = int(input('Seleccione su sexo, 1 para Hombre | 2 para mujer: '))
		if sexo != 1 and sexo != 2:
			print('Seleccione un sexo correcto')
			sexo = int(input('Seleccione su sexo, 1 para Hombre | 2 para mujer: '))

		#MOROSIDAD
		morosodidad = int(input('¿Tiene usted deuda con el colegio?, 1 para SI | 2 para NO: '))
		if morosodidad != 1 and morosodidad != 2:
			print('Seleccione una opcion correcta')
			morosodidad = int(input('¿Tiene usted deuda con el colegio?, 1 para SI | 2 para NO: '))

		if morosodidad == 2:					
			# proceso de votación
			print('Ingrese la opción para realizar su voto')
			opcion = int(input('1 para candidato A | 2 para candidato B | 3 para candidato C: '))
			if opcion == 1:
				votos_a += 1
				if sexo == 2:
					mujeres_a += 1
			elif opcion == 2:
				votos_b += 1
			elif opcion == 3:
				votos_c += 1			
			else:
				print('Voto nulo')
				votos_nulos += 1				

			if sexo == 2:
				mujeres += 1
		else:
			print('No puedes votar por no estar solvente')
			morosos += 1

			if sexo == 1:
				hombres_morosos += 1

	# Calculos
	ganador = ''
	votos_ganador = 0
	if votos_a > votos_b and votos_a > votos_c:
		ganador = "A"
		votos_ganador = votos_a
	elif votos_b > votos_a and votos_b > votos_c:
		ganador = "B"
		votos_ganador = votos_b
	elif votos_c > votos_b and votos_c > votos_a:
		ganador = "c"
		votos_ganador = votos_c
	else:
		ganador = 'EMPATE'

	porcentaje = (votos_ganador * 100)/(cantidad_profesionales-morosos)
	porcentaje_nulos = (votos_nulos * 100)/(cantidad_profesionales-morosos)
	porcentaje_mujeres = 0
	if mujeres != 0:
		porcentaje_mujeres = (mujeres_a * 100)/mujeres

	print('Elecciones presidenciales del colegio de', nombre_colegio)
	if ganador != 'EMPATE':
		print('El candidato ganador es '+ ganador + ' con ' + str(votos_a) + ' votos representando un porcentaje del ' + str(porcentaje) + '%')
	else:
		print('Hubo un empate!')
	print('Votos nulos: '+ str(votos_nulos) + ' porcentaje: ' + str(porcentaje_nulos) + '%')
	print('Cantidad de profesionales morosos: ' + str(morosos))
	print('Porcentaje de mujeres que votaron por la opcion A: ' + str(porcentaje_mujeres) + '%')
	print('Cantidad de hombres morosos: ' + str(hombres_morosos))

	# Usuario decide permanencia el el ciclo primario
	print('¿Desea realizar elecciones para otro colegio?')
	pregunta = int(input('Ingrese cualquier numero para Si, Ingrese 2 para No: '))
	if pregunta == 2:
		mantener = False