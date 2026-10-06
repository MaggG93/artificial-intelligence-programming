# A - Escribe una función llamada "duplicado" que tome una lista y devuelva True
# si tiene algún elemento duplicado. La función no debe modificar la lista.
# B - Crear una función que genere una lista de 23 números aleatorios del 1 al
# 100 y comprobar con la función anterior si existen elementos duplicados.

from collections import Counter
import random

def duplicado(lista):
    contador = Counter(lista)

    for num in contador:
        if contador[num] > 1:

            return True
        else:

            return False

lista1 = [
    "python",
    "java",
    "javascript",
    "python",
    "html",
    "css",
    "java",
    "python",
    "docker",
    "html",
    "react",
    "css",
    "angular",
    "docker"
]
lista2 = [
    "python",
    "java",
    "javascript",
    "html",
    "css",
    "docker",
    "react",
    "angular",
    "typescript",
    "mysql",
    "git",
    "linux",
    "kubernetes",
    "node",
    "php"
]
lista_num_random = [random.randint(1, 100) for i in range(23)]

# A
print(duplicado(lista2))
print (duplicado(lista1))

# B
print(duplicado(lista_num_random))