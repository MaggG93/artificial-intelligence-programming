# Ejercicio 6. Realizar un algoritmo que dada una cadena de caracteres, genere
# otra cadena resultado de invertir la primera.

def invertir_cadena(cadena):
    return cadena[::-1]

cadena = input("Ingrese una cadena: ")
cadena_invertida = invertir_cadena(cadena)

print(cadena_invertida)