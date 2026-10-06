# Escribe una función llamada "eliminaDuplicados" que tome una lista
# y devuelva una nueva lista con los elementos únicos de la lista original. No
# tienen porqué estar en el mismo orden.

def eliminarDuplicados(lista):
    lista_sin_dup = set(lista)
    lista_sin_dup = list(lista_sin_dup)

    return lista_sin_dup

lista = [
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

print(eliminarDuplicados(lista))