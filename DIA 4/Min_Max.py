menor = min(58,96,21,64,47)
mayor = max(58,96,21,64,47)

print(menor)
print(mayor)

#---Otra forma de hacerlo---

lista = [58,96,21,64,47]

print(f'El menos es {min(lista)} y el mayor es {max(lista)}')


nombres = ['Juan','Pablo','Alicia','Carlos']

print(min(nombres)) #Muestra el nombre menos según el alfabeto (Alicia)
print(max(nombres)) #Muestra el nombre mayor según el alfabeto (Pablo)

nombre = "Carlos"
print(min(nombre)) #Aquí pasa lo mismo que en la anterior pero con cada una de las letras. OJO la función primero busca las letras mayúsculas y luego las minúsculas.
print(min(nombre.lower())) #Para que solo busque entre las letras minúsculas

dic = {'C1':45,'C2':11}
print(min(dic.values()))



#Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)



#Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
#Almacena dicho valor en una variable llamada edad_minima.
#También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)

print(f'La edad mínima es {edad_minima} y el último nombre alfabéticamente es {ultimo_nombre}')

