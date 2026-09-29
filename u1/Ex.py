# Ejercicio 1. Algoritmo que lea tres números y los muestre ordenados por pantalla.

nums = [22, 4, 13]

print(sorted(nums))

# Ejercicio 2. Algoritmo que lea un número y diga si es par o no.

num = 6

if num % 2 == 0:
    print(num, "es par")
else:
    print(num, "es impar")

# Ejercicio 3. Algoritmo que lea un número y calcule su factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(6))

# Ejercicio 4. Algoritmo que muestre todos los números pares que hay entre 0 y
# un número leído por teclado. Mostrar también la suma de los números pares
# justo después de la lista de números.

num = int(input("Ingrese un número: "))
suma = 0

for n in range(0, num + 1):
    if n % 2 == 0:
        print(n)
        suma += n

print("Suma de los pares:", suma)

# Ejercicio 5. Dada una secuencia de números leídos por teclado, que acabe con
# un –1, por ejemplo: 5,3,0,2,4,4,20,16,2,3,6,0,……,-1; Realizar el algoritmo que
# calcule la media aritmética. Suponemos que el usuario no insertara números
# negativos.





