texto = input("Ingrese un texto cualquiera: ")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("----Cantidad de Letras----")
cant_letras1 = texto.count(letras[0])
cant_letras2 = texto.count(letras[1])
cant_letras3 = texto.count(letras[2])

print("\n")
print(f"La letra '{letras[0]}' se repide {cant_letras1} veces")
print(f"La letra '{letras[1]}' se repide {cant_letras2} veces")
print(f"La letra '{letras[2]}' se repide {cant_letras3} veces")

print("\n")
cant_palabras = texto.split()
print(f"El texto tiene {len(cant_palabras)} palabras")

print("\n")
print("----Letras de Inicio y de Fin----")
print("\n")
letra_inicio = letras[0]
letra_fin = letras[-1]
print(f"La letra del Inicio es '{letra_inicio}' y la letra del Final es '{letra_fin}'")

print("\n")
print("----Texto Invertido----")
cant_palabras.reverse()
texto_invertido = ' '.join(cant_palabras)
print(f"Tu texto de forma inversa va a decir: {texto_invertido}")

print("\n")
print("----Buscar la palabra Python----")
busca_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra Python: {dic[busca_python]} se encuentra en el texto")