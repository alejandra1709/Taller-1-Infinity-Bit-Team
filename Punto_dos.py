primer_numero: float= input("ingrese un núnmero: ")
segundo_numero: float= input ("ingrese otro numero: ")
tercer_numero: float= input ("ingrese un tercer numero: ")
if primer_numero == segundo_numero and primer_numero == tercer_numero:
    print("Todos los numeros son iguales")
elif primer_numero > segundo_numero and primer_numero > tercer_numero:
    print("El primer numero es el mayor")
elif segundo_numero > primer_numero and segundo_numero> tercer_numero:
    print("El segundo número es el mayor")
else:
    print("El tercer numero es mayor")

