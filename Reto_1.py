from datetime import datetime

nombre = input("Ingresa tu nombre:")
edad = int(input("Ingresa tu edad:"))
fecha = datetime.now()
hora = format(fecha.hour)

if (edad < 18 and hora >= '18'):print(nombre + " tienes que ir a dormir!!")
elif (edad < 18 and hora <= '18'):print(nombre + " tienes que hacer tu tarea!!")
else:print(nombre + " no estas obligado hacer nada!!")
