import math
def determinar_x(radio, grados):
    operacion = radio*math.cos(grados)
    return operacion
def determinar_y(radio, grados):
    operacion = radio*math.sin(grados)
    return operacion

def procesoa():
    print("Ingresa coordenadas polares")
    radio = int(raw_input("Dame radio: "))
    angulo = int(raw_input("Dame angulo: "))
    x = determinar_x(radio, angulo)
    y = determinar_y(radio, angulo)
    print("El vector es ({0},{1}) en rectangulares".format(x,y))

procesoa()
procesoa()

def procesob():
    xa = int(raw_input("Dame X de A: "))*5
    ya = int(raw_input("Dame Y de A: "))*5
    xb = int(raw_input("Dame X de B: "))*3
    yb = int(raw_input("Dame Y de B: "))*3
    xc = int(raw_input("Dame X de C: "))
    yc = int(raw_input("Dame Y de C: "))
    xd = int(raw_input("Dame X de D: "))/3
    yd = int(raw_input("Dame Y de D: "))/3

    #5d-3a+c- b/3
    operacionx = xa-xb+xc-xb
    operaciony = ya-yb+yc-yb

    print("Resultado es ({0},{1})".format(operacionx, operaciony))
procesob()
