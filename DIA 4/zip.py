nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Bogotá','Madrid']

combinados = list(zip(nombres,edades,ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")



#Muestra en pantalla frases como la del siguiente ejemplo:
#La capital de Alemania es Berlín
#Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(capitales,paises))

for capital,pais in combinados:
    print(f"La capital de {pais} es {capital}")


#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.

marcas = ['Adidas','Rolex','Shaft']
productos = ['Zapatos','Reloj','Casco']

mi_zip = zip(marcas,productos)
print(mi_zip)


#Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros

a = ['uno','dos','tres','cuatro','cinco']
b = ['um','dois','três','quatro','cinco']
c = ['one','two','three','four','five']

numeros = list(zip(a,b,c))
print(numeros)