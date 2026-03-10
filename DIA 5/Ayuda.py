dic = {'clave1':100,'clave2':500}

a = dic.popitem()
print(a)
print(dic)



#Remueve los caracteres a la izquierda de nuestro texto principal:
#    ,
#    :
#    %
#    _
#    #
#Utiliza el metodo lstrip(). Imprime el resultado en pantalla:

text = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
texto = text.lstrip(",:%_#")
print(texto)


#Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
fruit = frutas.insert(3,"naranja")
print(fruit)



#Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)