mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5)
result = mi_texto.rindex("a")
print(resultado)
print(result)


#Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

palabra = "ordenador"
print(palabra[4])


#Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))


#Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))