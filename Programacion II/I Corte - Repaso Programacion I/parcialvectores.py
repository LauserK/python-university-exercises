import math

def obtener_numero(mensaje):
    return int(raw_input(mensaje))

def modulo(x,y):
    return (x**2 + y**2)**0.5

def obtener_vector(a,b):
    return b-a

def calcular_tita(x,y):
    tita = 0
    if x != 0:
        tita = math.atan(y/x)
    return tita
        
def calculo():
    print('a(x1, y1) b(x2, y2) c(x1, y1) d(x2, y2)')

    # obtener valores
    x1 = obtener_numero('Ingresa x1: ')    
    y1 = obtener_numero('Ingresa y1: ')
    x2 = obtener_numero('Ingresa x2: ')    
    y2 = obtener_numero('Ingresa y2: ')    

    # componentes
    abx = obtener_vector(x1,x2)
    aby = obtener_vector(y1,y2)
    cdx = obtener_vector(x1,x2)
    cdy = obtener_vector(y1,y2)
    
    # modulo
    mab = modulo(abx, aby)
    mcd = modulo(cdx, cdy)

    #2AB + 4CD
    multiplicacionx = abx*2 + cdx*4
    multiplicaciony = aby*2 + cdy*4

    # polares
    r1 = modulo(abx, aby)
    tita1 = calcular_tita(abx, aby)

    r2 = modulo(cdx, cdy)
    tita2 = calcular_tita(cdx, cdy)

    print("\n\nRESULTADOS")
    #puntos
    print("a({0}, {1}) y b({2}, {3}), c({4}, {5}) y  d({6}, {7})".format(x1,y1,x2,y2,x1,y1,x2,y2))

    #componentes
    print("AB=({}, {}) y CD=({}, {})".format(abx, aby, cdx, cdy))

    #multi
    print("2AB + 4CD = ({0}, {1})".format(multiplicacionx, multiplicaciony))
    
    #polares
    print("AB polar, r={0}, angulo = {1}".format(r1, tita1))
    print("CD polar, r={0}, angulo = {1}".format(r2, tita2))


calculo()