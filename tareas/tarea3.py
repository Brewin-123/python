asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

#1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

#print(asignaturas)


#2. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

# for asignaturas in asignaturas:
#     print(f"Yo estudio {asignaturas}")


#3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# notas = {}

# for asignatura in asignaturas:
#     nota = input(float(f"¿Qué nota sacaste en {asignatura}? "))
#     notas[asignatura] = nota

# print("Resumen de notas:")
# for asignatura in asignaturas:
#     print(f"En {asignatura} has sacado {notas[asignatura]}")
