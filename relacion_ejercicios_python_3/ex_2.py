# Implementa una función que tome una lista de números y devuelva
# la suma acumulada, es decir, una nueva lista donde el primer elemento es el
# mismo, el segundo elemento es la suma del primero con el segundo, el tercer
# elemento es la suma del resultado anterior con el siguiente elemento y así
# sucesivamente. Por ejemplo, la suma acumulada de [1, 2, 3] es [1, 3, 6].

def obtener_lista_suma_acumulada(lista):
    nueva_lista = []
    suma = 0

    for num in lista:
        suma += num
        nueva_lista.append(suma)

    return nueva_lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(obtener_lista_suma_acumulada(lista))