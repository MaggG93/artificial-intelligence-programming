# Implementa una función en Python que acepte una lista de valores
# numéricos y obtenga su valor máximo sin utilizar la función «built-in» max().
# Nota: Recorrer todas las posiciones de la lista buscando el máximo.
# Entrada: [6, 3, 9, 2, 10, 31, 15, 7]
# Salida: 31

def obtener_max(lista):
    max = lista[0]

    for num in lista:
        if num > max:
            max = num

    return max

lista = [6, 3, 9, 2, 10, 31, 15, 7]
print(obtener_max(lista))