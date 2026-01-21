lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra: {letra}, posición {numero_letra}')


list = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']

for nombre in list:
    if nombre.startswith('L'): #startswitch() sirve para buscar las palabras que empiecen con la letra de elección
        print(nombre)
    else:
        print('No comienza con L')


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor)


palabra = 'python'

for letra in palabra:
    print(letra)


for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)


dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for elemento in dic.items():
    print(elemento)

for elemento in dic.values():
    print(elemento)



#Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumnos in alumnos_clase:
    print("Hola " + alumnos)


#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    print("suma_numeros")


#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero%2 == 0:
        suma_pares = suma_pares + numero
        print(suma_pares)
    elif numero%2 == 1:
        suma_impares = suma_impares + numero
        print(suma_impares)

