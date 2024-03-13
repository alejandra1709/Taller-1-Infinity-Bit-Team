Hz = float(input("Ingrese frecuencia de una honda en Hz: "))
if Hz>30.0e18 :
    print("La onda se encuentra en: rayos gamma")
elif Hz>30.0e15:
    print("La onda se encuentra en: rayos X")
elif Hz> 1.5e15 :
    print("La onda se encuentra en: Ultravioleta extremo")
elif Hz>7.89e14 :
    print("La onda se encuentra en: Ultravioleta cercano")
elif Hz>384e12:
    print("La onda se encuentra en: Espectro Visible")
elif Hz>120e12 :
    print("La onda se encuentra en: Infrarrojo cercano")
elif Hz>6.00e12 :
    print("La onda se encuentra en: Infrarrojo medio	")
elif Hz>300e9 :
    print("La onda se encuentra en: Infrarrojo lejano")
elif Hz>3e8 :
    print("La onda se encuentra en: Microondas") 
else :
    print("La onda se encuentra en: Radio")