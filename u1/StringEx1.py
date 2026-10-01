# Ejercicio 1. Realizar un algoritmo que comprueba si una cadena leída por
# teclado comienza por una subcadena introducida por teclado.

def comprobar_subcadena_en_cadena(cadena):
    if cadena.startswith(subcadena) :
        print(f"la cadena empieza por {subcadena}")
    else:
        print(f"la cadena no empieza por {subcadena}")

cadena = input("Ingrese una cadena: ")
subcadena = input("Ingrese una subcadena: ")

comprobar_subcadena_en_cadena(cadena)
