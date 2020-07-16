def primo(x):
  c = 0
  for i in range(1, x+1):
      if x % i == 0:
          c += 1

  if c == 2:
      return True
  else:
      return False

def vector(vector):
  for x in vector:
      print(x, end=' ')
  print('\n')

tamano = int(input('Tamano de los vectores '))
a = [0]*tamano
b = [0]*tamano
c = [0]*tamano


for i in range(tamano):
  a[i] = int(input('Cargue valor vector a en pos {0}: '.format(i)))

for i in range(tamano):
  b[i] = int(input('Cargue valor vector b en pos {0}: '.format(i)))

# generar c
i=0
while(i < tamano):    
  if i == 0:
    c[i] = a[i] + a[i+1]
  else:
    if i % 2 == 0:
      c[i] = a[i] + a[i+1]
    else:
      c[i] = b[i] + b[i-1]
  i+=1

# generar vector primo
primos = 0
for x in c:
  if primo(x):
    primos += 1

vectorprimo = [0]*primos
pos = 0
for x in c:
  if primo(x):
    vectorprimo[pos] = x
    pos +=1

print("A")
vector(a)
print("B")
vector(b)
print("C")
vector(c)
print("PRIMOS")
vector(vectorprimo)

for i in range(primos):
  for j in range(i+1,primos):
    if vectorprimo[i]>vectorprimo[j]:
      aux=vectorprimo[i]
      vectorprimo[i]=vectorprimo[j]
      vectorprimo[j]=aux

print("ORDENADO")
vector(vectorprimo)