# Ejercicio 8. Ampliación: Modificar la función anterior para que sea capaz de
# comprobar si una frase es un palíndromo. Por ejemplo, “yo hago yoga hoy”.

def esPalindromo(cadena):
    cadena_limpia = "".join(cadena.split()).lower()
    if cadena_limpia == cadena_limpia[::-1]:
        return True
    else:
        return False

cadena = input("Ingrese una frase que incluya palindromos: ")

print(esPalindromo(cadena))