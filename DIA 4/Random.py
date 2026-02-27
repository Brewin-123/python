from random import *

aleatorio = randint(0,50)
print(aleatorio)

aleatorio2 = uniform(1,5) #Muestra un número aleatorio en el rango establecido pero con muchos decimales.
print(aleatorio2)

aleatorio3 = round(uniform(1,5),1) ##Muestra un número aleatorio en el rango establecido pero con un solo decimal.
print(aleatorio3)

aleatorio4 = random() #Muestra la fracción de un entero, en este caso en un rango de 0 a 1
print(aleatorio4)

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores) #Función para elegir un elemento de una lista de forma aleatoria
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros) #Esta función va a mezclar la lista anteriormente definida y le dará un orden aleatorio a los elementos.
print(numeros)



#Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio

from random import randint

aleatorio = randint(1,10)
print(aleatorio)


#Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio}

from random import *

aleatorio = random()
print(aleatorio)


#Utiliza el metodo choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

from random import *

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)
print(sorteo)