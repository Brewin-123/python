mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
mi_lista3 = mi_lista + mi_lista2
#otra_lista = ['hola',55,6.1]
#mi_lista3[0] = 'alfa'
mi_lista3.append('g')
mi_lista3.pop(0)

print(mi_lista)
print(mi_lista2)
resultado = len(mi_lista)


print(type(mi_lista))
print(resultado)
print(mi_lista3)

lista = ['g','o','b','m','c']
#list.sort()
print(lista)


#Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista = ['hola','10','4.2','a','3']
print(mi_lista)


#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:

#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')
print(medios_transporte)


#Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.

#manzana
#banana
#mango
#cereza
#sandía

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

print(frutas)