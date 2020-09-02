"""
La Ujap ofrece en verano  para sus alumnos las siguientes materias: 
Matematicas, Programacion II y Fisica, los costos por unidad creditos 
son como siguen en orden  10000 Bs, 15000 Bs. Y 16000 Bs. Y la cantidad
de unidades credito son en orden: 5, 4, 6. El alumno podra inscribir 
hasta 2 materias, en el caso de inscribir 1 materia no hay problema, 
pero para poder inscribir 2 materias  debe tener un promedio de notas
del semestre anterior superior a 16. Nota el alumno  debe estar Solvente
para inscribirse y no puede inscribir 3 materias. 

	Por alumnos Imprimir: su Nombre, Promedio nota semestre anterior, 
    Cuantas materias Inscribio, Cuales son las Materias inscritas y 
    cuanto pagara en total
Reporte General:
Cantidad y porcentajes de inscritos por materia
Porcentaje de mujeres inscritas en programacion II
Porcentajes de alumnos morosos. Moroso es la persona que debe
En cual materia hubo mas inscritos
Total de bolivares recaudados por la universidad
Determine si se inscribieron mas hombres que mujeres o viceversa
"""

#inicio
nombre=materia=""
promedio=mti=total_pagar=mtia=mtib=mtic=0
solv=respuesta="S"
tmo=tta=tti=ttrunive=0
ttia=ttib=ttic=0
pro1=pro2=pro3=prom=prommuje=0
tmuj=tmujc=0
precio1=10000*5
precio2=15000*4
precio3=16000*6

#proceso
while(respuesta=="S"):
    promedio=mti=total_pagar=mtia=mtib=mtic=0
    nombre=m=""
    solv = raw_input("Esta solvente el alumno? s/n: ").upper()
    if (solv!="S" and solv!="N"):
        solv = raw_input("Esta solvente el alumno? s/n: ").upper()
    if (solv=="S"):
        nombre=raw_input("Nombre alumno: ").upper()
        promedio = float(raw_input("Promedio semestre anterior: "))
        sexo = raw_input('Ingrese sexo f/m: ').upper()
        if sexo != "F" and sexo != "M":
            sexo = raw_input('Ingrese sexo f/m: ').upper()

        while(mti!=2):
            if (mti==1 and promedio>16) or (mti==0):
                print("Que materia quieres inscribir?")
                materia = raw_input("Escriba a para Matematicas, b para Programacion II y c para Fisica: ").upper()

                if (materia=="A"):
                    if mtia==0:
                        mtia=1
                        mti+=1
                        total_pagar+=precio1
                    else:
                        print("Materia ya inscrita")
                elif (materia=="B"):
                    if mtib==0:
                        mtib=1
                        mti+=1
                        total_pagar+=precio2

                        if sexo=="F":
                            tmuj+=1
                            tmujc+=1
                    else:
                        print("Materia ya inscrita")
                elif (m=="C"):
                    if mtic==0:
                        mtic=1
                        mti+=1
                        total_pagar+=precio3
                    else:
                        print("Materia ya inscrita")
            else:
                print("Alumno con promedio inferior para inscribir otra materia")
                break

        ttia+=mtia
        ttib+=mtib
        ttic+=mtic
        ttrunive+=total_pagar
        tti+=1

        print("\nAlumno: {0}".format(nombre))
        print("Promedio semestre anterior: {0}".format(promedio))
        print("Materias inscritas: {0}".format(mti))

        if (mtia==1):
            print("Materia matematica inscrita")

        if (mtib==1):
            print("Materia Progra 2 inscrita")

        if (mtic==1):
            print("Materia Fisica inscrita")

        print("Total a pagar: Bs {0}".format(total_pagar))

    else:
        tmo+=1
        print('\nMoroso no puede inscribir')

    tta+=1
    respuesta = raw_input("Otro alumno? s/n: ").upper()

pro1 = (ttia * 100)/tti
pro2 = (ttib * 100)/tti
pro3 = (ttic * 100)/tti
prom = (tmo * 100)/tta
if tmujc != 0:
    prommuje= (tmujc*100)/tmuj

print("\nReporte general")
print("Total inscritos en matematica {0} : {1}%".format(ttia, pro1))
print("Total inscritos en progra 2 {0} : {1}%".format(ttib, pro2))
print("Total inscritos en fisica {0} : {1}%".format(ttic, pro3))
print("Total mujeres inscritas en Programacion 2 {0} : {1}%".format(tmujc, prommuje))
print("Total morosos {0} : {1}%".format(tmo, prom))

if (ttia>ttib and ttia>ttic):
    print("Matematicas tuvo mas inscritos")
elif (ttib>ttia and ttib>ttic):
    print("Programacion 2 tuvo mas inscritos")
elif (ttic>ttia and ttic>ttia):
    print("Fisica tuvo mas inscritos")

print("Total Bolivares recaudados: BS {0}".format(ttrunive))
if (tmuj > (tti-tmuj)):
    print("Mas mujeres se inscribieron")
else:
    print("Mas hombres se inscribieron")