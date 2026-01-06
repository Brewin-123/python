texto = "Es es el texto de Brewin"

#resultado = texto.upper() #Todo en mayúscula
#resultado = texto.lower() #Todo en minúscula
#resultado = texto.split() #Texto separado
#resultado = texto.find("s") #Encontrar índice
#resultado = texto.replace("Brewin","todos") #Reemplaza textos o letras

print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])


#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())


#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.

lista_palabras = ["La","legibilidad","cuenta."]
separar = " ".join(lista_palabras)
print(separar)


#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:

#"difícil" --> "fácil"

#"mala" --> "buena"

#y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")

print(frase)