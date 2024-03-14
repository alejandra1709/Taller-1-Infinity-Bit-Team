a : float = float(input("Ingrese primer numero: "))
b : float = float(input("Ingrese segundo numero: "))
c : float = float(input("Ingrese tercer numero: "))
if a==b and a==c:
  print("Los tres números son iguales")
elif a>=b and a>=c :
  print("El número mayor es ",a)
elif b>=a and b>=c :
  print("El número mayor es ",b)
else :
  print("El número mayor es ",c)
