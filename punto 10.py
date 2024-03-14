distancia = float(input("Escribe una distancia en metros: "))
velocidad_luz:int= 300000000
velocidad_sonido:int=344
velocidad_bolt:float=11.6667
#teniendo en cuenta que el vehiculo comercial mas rapido es el Koenigsegg Jesko Absolut
velocidad_vehiculo:float=147.778
#tiempo=distancia/velocidad
op1:float= (float(distancia)/velocidad_luz)
op2:float= (float(distancia)/velocidad_sonido)
op3:float= (float (distancia)/velocidad_vehiculo)
op4:float= (float(distancia)/velocidad_bolt)
print ("El tiempo que le tomaria recorrer "+str(distancia) +" metros a la luz es de "+str(op1)+ " segundos")
print ("El tiempo que le tomaria recorrer "+str(distancia) +" metros al sonido es de "+str(op2)+ " segundos")
print ("El tiempo que le tomaria recorrer "+str(distancia) +" metros al vehiculo comercial mas rapido es de "+str(op3)+ " segundos")
print ("El tiempo que le tomaria recorrer "+str(distancia) +" metros a Usain Bolt es de "+str(op4)+ " segundos")