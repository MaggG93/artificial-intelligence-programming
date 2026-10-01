# Ejercicio 7. Realizar una función, esPalindromo, que reciba una cadena de
# caracteres y devuelva True si es un palíndromo, o False en caso de que no lo
# sea. Un palíndromo es una palabra que se lee igual de derecha a izquierda que
# de izquierda a derecha. Por ejemplo, “reconocer”.

def esPalindromo(cadena):
    if cadena == cadena[::-1]:
        return True
    else:
        return False

cadena = input("Ingrese un palindromo: ")

print(esPalindromo(cadena))