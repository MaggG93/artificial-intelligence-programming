# Ejercicio 3. Suponiendo que hemos introducido una cadena por teclado que
# representa una frase (palabras separadas por espacios), realiza un algoritmo
# que cuente cuántas palabras tiene.

def contar_palabras(cadena):
    return len(cadena.split())

cadena = input("Ingresa una cadena: ")
total = contar_palabras(cadena)

if total < 2:
    print("Debes introducir una frase")
else:
    print(f"La frase tiene {total} palabras")