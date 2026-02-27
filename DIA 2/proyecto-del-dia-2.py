#Empresa con ganancia por ventas, preguntar nombre del trabajador, cuánto hizo en ventas en el mes y sacar el 13% de las ventas para su ganancia.
#Preguntar nombre
#Cuánto vendió
#Y ganancia que es igual al 13% de lo que vendió

nombre = input("Cuál es tu nombre? ")
ventas = float(input("Cuánto vendiste en el mes? "))

ganancia = ventas * 13 / 100

print(f"Ok, {nombre}, según tu cantidad de ventas del mes de ${ventas}, has ganado ${ganancia}")