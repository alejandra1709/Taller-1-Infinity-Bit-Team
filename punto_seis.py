#Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
letra:str=input("escriba una letra: ")
a=ord(letra)
if (a==65 or a==69 or a==73 or a==79 or a==85 or a==97 or a==101 or a==105 or a==111 or a==117):
    print("La letra " , letra , " es una vocal ")
else:
    print("La letra " , letra , " es una consonante ")