# Ejercicio 4. Realizar un algoritmo que lea una cadena por teclado y convierta
# las mayúsculas a minúsculas y viceversa.

def convertir_cadena_mayus_minus(cadena_original):
    cadena_resultado = ""
    for caracter in cadena_original:
        if caracter.isupper():
            cadena_resultado += caracter.lower()
        elif caracter.islower():
            cadena_resultado += caracter.upper()
        else:
            cadena_resultado += caracter

    return cadena_resultado

cadena_original = input("Ingrese una cadena: ")

print(convertir_cadena_mayus_minus(cadena_original))

# o puedo usar...

print(cadena_original.swapcase())