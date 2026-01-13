mi_tuple = (1,2,(10,20),3,4)
mi_tuple = list(mi_tuple) #pasar a tipo lista
mi_tuple = tuple(mi_tuple) #pasar a tipo tuple nuevamente
t = (1,2,3,1)

#x,y,z = t

print(type(mi_tuple))
print(mi_tuple[2][0])
#print(x,y,z)
print(len(t))
print(t.count(1)) #cuántas veces aparece el valor
print(t.index(2)) #en qué índice se encuentra el valor



#Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))


#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)


#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)