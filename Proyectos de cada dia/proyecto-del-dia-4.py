from random import *

nombre = input("Ingrese su nombre: ")
print(f"Bueno, {nombre}, he pensado en un número entre 1 y 100, y tienes ocho intentos para adivinar cuál es el número")

num = randint(1,100)
print(num)

for intentos in range(8):
    numero = int(input("Ingresa un número del 1 al 100: "))

    if numero < 1 or numero > 100:
        print("Fuera de límites")
        continue

    if numero ==  num:
        print("EL NÚMERO ES CORRECTO!")
        break
    elif numero < num:
        print("El número que ingresaste es menor al correcto")
    else:
        print("El número que ingresaste es mayor al correcto")
else:
    print("SE ACABARON LOS INTENTOS")