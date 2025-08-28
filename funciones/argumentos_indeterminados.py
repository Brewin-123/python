def infinito(*args): #args para pasar todo tipo de argumentos, sin límite
    print(args)

infinito("Hola", 20, 10.4, [1,2,3])


def infinito(*args):
    for args in args: #Para recorrer cada argumento
        print(args)

infinito("Hola", 20, 10.4, [1,2,3])


def infinito(**kwargs): #Permite aplicar un clave a el argumento
    for kwarg in kwargs:
        print(kwarg, "-->", kwargs[kwarg])

infinito(a = "Hola", b = 15, c = ["María", "Pedro", "Jose"])