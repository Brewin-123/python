for numero in range(1,5): #(5): de 0 a 5 -- (1,10,2): de 1 a 10 cada 2 pasos
    print(numero)


lista = list(range(1,101))
print(lista)



#Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.

mi_lista = list(range(2500,2586))
print(mi_lista)


#Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.

mi_lista = list(range(3,301,3))
print(mi_lista)


#Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.

#Para ello:
#Crea un rango de valores que puedas recorrer en un loop
#Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
#Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.

suma_cuadrados = 0

for numero in range (1,16):
    cuadrado = numero**2
    suma_cuadrados += cuadrado

print(suma_cuadrados)


#Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)
print(rango)


