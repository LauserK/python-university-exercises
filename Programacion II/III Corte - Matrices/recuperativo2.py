import random

n = int(input("Ingrese el numero de matriz n*n: "))
Numero_serie = [[0] * n for i in range(n)]
suma_serie = [[0] * n for i in range(n)]
x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))
z = int(input("Ingrese z: ")) 

def calculo(numero):
  op = 0
  vz= 1
  vx = 2
  vn = 1
  for n in range(1, numero+1):
    if n == 1:
      op += (x/(y**n))
    else:
      op += ((z**vz) * (x**vx)) / (y**(n-vn))
      vz += 1      
      vx += 1
      vn += 1
    
  return op

for i in range(n):
  for j in range(n):
    Numero_serie[i][j] = random.randint(1,10)
    suma_serie[i][j] = calculo(Numero_serie[i][j])

print("Matriz Numero_serie")
for i in range(n):
  for j in range(n):
    print("{0:2}".format(Numero_serie[i][j]), end=" ")
  print("\n")

print("Matriz suma_serie")
for i in range(n):
  for j in range(n):
    print("{0:10.2f}".format(suma_serie[i][j]), end=" ")
  print("\n")