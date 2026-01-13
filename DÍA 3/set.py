mi_set = set([1,2,3,4,5]) #Elementos únicos - no acepta listas - no acepa diccionarios - ACEPTA TUPLES
print(type(mi_set))
print(mi_set)

#---Otra forma de crear set---
#oto_set = {1,2,3}
#print(type(oto_set))
#print(oto_set)

print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.remove(4)
print(s1)
s1.pop() #Aquí lo que hace es eliminar un número aleatorio
print(s1)
s1.clear()
print(s1)



#Une los siguientes sets en uno solo, llamado mi_set_3:

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

print(mi_set_3)


#Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

print(sorteo.pop())


#Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")

print(sorteo)