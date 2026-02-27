n1 = "Kari"
n2 = "na"
print(n1 + n2)

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)
print("agua" in poema)
print("sol" in poema)
print(len(poema))


#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.

print("Repetición" * 15)


#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias

haiku = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in haiku)


#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.

palabra = "electroencefalografista"
print(len(palabra))