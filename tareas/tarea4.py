# 1.Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
def saludo():
    print("Hola")

saludo()


# 2.Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
def saludar():
    nombre = "Edgar"
    print(f"Hola {nombre}")

saludar()


# 3.Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El número debe ser entero positivo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5)) 
print(factorial(12))