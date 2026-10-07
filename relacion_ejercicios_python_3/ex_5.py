# Escribe una función llamada “búsqueda” que reciba como
# parámetros un dato y una lista, y devuelva la posición del dato en la lista si
# está. Si no está devolverá -1.

def busqueda1(dato, lista):
  if dato in lista:
    return lista.index(dato)
  else:
    return -1

def busqueda2(dato, lista):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1

dato = 4
lista = [1, 2, 3, 4]
print(busqueda1(dato, lista))
print(busqueda2(dato, lista))
