#1. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Usted es mayor de edad.")
# else:
#     print("Usted es menor de edad.")


#2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# import getpass

# password = "admin123"

# users = getpass.getpass("Escribe tu contraseña: ")

# while users != password:
#     print("Contraseña incorrecta")
#     users = getpass.getpass("Escribe tu contraseña: ")
# else:
#     print("Beinvenido.")
    

#3. Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# numero1 = float(input("Ingrese el primer númeo: "))

# numero2 = float(input("Ingrese el segundo númeo: "))

# resultado = numero1/numero2

# if numero2 == 0:
#     print("Error, no se puede dividir entre 0.")
# else:
#     print(Resultado)
