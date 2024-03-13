a : float = float(input("Ingrese primer numero: "))
b : float = float(input("Ingrese segundo numero: "))
c : float = float(input("Ingrese tercer numero: "))
if a>b and a>c :
  print("Primer numero es mayor que el segundo y tercer numero")
elif b>a and b>c :
  print("Segundo numero es mayor que el primer y tercer numero")
else :
  print("Tercer numero es mayor que el primer y segundo numero")