# Ejercicio 5. Realizar un algoritmo que compruebe si una cadena contiene una
# subcadena. Las dos cadenas se introducen por teclado.

def comprobar_subcadena_en_cadena(cadena):
    if subcadena in cadena:
        print(f"la cadena incluye {subcadena}")
    else:
        print(f"la cadena no incluye {subcadena}")

cadena = input("Ingrese una cadena: ")
subcadena = input("Ingrese una subcadena: ")

comprobar_subcadena_en_cadena(cadena)
