#inicio
nombre=m=""
pna=mti=totp=mtia=mtib=mtic=0
solv=rp="S"
tmo=tta=tti=ttrunive=0
ttia=ttib=ttic=0
pro1=pro2=pro3=prom=prommuje=0
tmuj=tmujc=0
p1=10000*5
p2=15000*4
p3=16000*6

#proceso
while(rp=="S"):
    pna=mti=totp=mtia=mtib=mtic=0
    nombre=m=""
    solv = raw_input("Esta solvente el alumno? s/n: ").upper()
    if (solv!="S" and solv!="N"):
        solv = raw_input("Esta solvente el alumno? s/n: ").upper()
    if (solv=="S"):
        nombre=raw_input("Nombre alumno: ").upper()
        pna = float(raw_input("Promedio semestre anterior: "))
        sexo = raw_input('Ingrese sexo f/m: ').upper()
        if sexo != "F" and sexo != "M":
            sexo = raw_input('Ingrese sexo f/m: ').upper()

        while(mti!=2):
            if (mti==1 and pna>16) or (mti==0):
                print("Que materia quieres inscribir?")
                m = raw_input("Escriba a para Matematicas, b para Prora 2 y c para Fisica: ").upper()

                if (m=="A"):
                    if mtia==0:
                        mtia=1
                        mti+=1
                        totp+=p1
                    else:
                        print("Materia ya inscrita")
                elif (m=="B"):
                    if mtib==0:
                        mtib=1
                        mti+=1
                        totp+=p2

                        if sexo=="F":
                            tmuj+=1
                            tmujc+=1
                    else:
                        print("Materia ya inscrita")
                elif (m=="C"):
                    if mtic==0:
                        mtic=1
                        mti+=1
                        totp+=p3
                    else:
                        print("Materia ya inscrita")
            else:
                print("Alumno con promedio inferior para inscribir otra materia")
                break

        ttia+=mtia
        ttib+=mtib
        ttic+=mtic
        ttrunive+=totp
        tti+=1

        print("\nAlumno: {0}".format(nombre))
        print("Promedio semestre anterior: {0}".format(pna))
        print("Materias inscritas: {0}".format(mti))

        if (mtia==1):
            print("Materia matematica inscrita")

        if (mtib==1):
            print("Materia Progra 2 inscrita")

        if (mtic==1):
            print("Materia Fisica inscrita")

        print("Total a pagar: Bs {0}".format(totp))

    else:
        tmo+=1
        print('\nMoroso no puede inscribir')

    tta+=1
    rp = raw_input("Otro alumno? s/n: ").upper()

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
print("Total muejeres inscritas en programacion {0} : {1}%".format(tmujc, prommuje))
print("Total morosos {0} : {1}%".format(tmo, prom))

if (ttia>ttib and ttia>ttic):
    print("Matematicas tuvo mas inscritos")
elif (ttib>ttia and ttib>ttic):
    print("Progra 2 tuvo mas inscritos")
elif (ttic>ttia and ttic>ttia):
    print("Fisica tuvo mas inscritos")

print("Total Bolivares recaudados: BS {0}".format(ttrunive))
if (tmuj > (tti-tmuj)):
    print("Mas mujeres se inscribieron")
else:
    print("Mas hombres se inscribieron")
