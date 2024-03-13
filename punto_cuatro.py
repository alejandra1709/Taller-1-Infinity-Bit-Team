#Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
x: float = input ("ingrese un número real: ")
y: float = input ("ingrese otro número real: ")
if (float(x)%float(y) == 0):
    print ("el número " , x , " es múltiplo de " , y)
else:
    print ("el número " , x , " no es múltiplo de " , y)