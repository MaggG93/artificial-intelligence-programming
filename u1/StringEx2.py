# # Ejercicio 2. Algoritmo que pide una cadena y un carácter por teclado (valida
# # que sea un carácter) y muestra cuántas veces aparece el carácter en la
# # cadena.

def contar_caracteres(cadena, caracter):
    if len(cadena) == 0 or len(caracter) > 1:
        print("Ingrese una cadena y/o caracter válido")
    else:
        contador = cadena.count(caracter)
        print(contador)

cadena = input("Ingrese una cadena: ")
caracter = input("Ingrese una caracter: ")
contador = 0

contar_caracteres(cadena, caracter)