# Escribe una función llamada “búsquedaBinaria” que reciba como
# parámetros un dato y una lista, y devuelva la posición del dato en la lista si
# está. Si no está devolverá -1.

def busquedaBinaria(dato, lista):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        # Si el dato está en el medio, devolvemos su posición
        if lista[medio] == dato:
            return medio

        # Si el dato es menor, descartamos la mitad derecha
        elif lista[medio] > dato:
            derecha = medio - 1

        # Si el dato es mayor, descartamos la mitad izquierda
        else:
            izquierda = medio + 1

    # Si no se encontró el dato, devolvemos -1
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dato = int(input("Inserte un valor: "))
print(busquedaBinaria(dato, lista))
