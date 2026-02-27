v1 = True
v2 = False

print(type(v1))
print(v1)

numero = 5 == 2+3
print(type(numero))
print(numero)

#Es lo mismo
numero = bool(5 == 2+3)
print(type(numero))
print(numero)

lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)



#Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable llamada prueba

prueba = 5 != 6
print(prueba)


#Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()

prueba = 17834/34 > 87*56
print(prueba)


#Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()

prueba = 25**0.5 == 5
print(prueba)