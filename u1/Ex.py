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



# Ejercicio 6. Algoritmo que lea un número entero (altura) y a partir de él cree una
# escalera invertida de asteriscos con esa altura. Deberá quedar así, si ponemos
# una altura de 5.

altura = int(input("Introduce la altura: "))

for i in range(altura, 0, -1):
    print("*" * i)

# Ejercicio 7. Algoritmo que dado un año, nos diga si es bisiesto o no. Un año es
# bisiesto bajo las siguientes condiciones:
# Un año divisible por 4 es bisiesto, salvo si es divisible entre 100. Si un año es
# divisible entre 100 y además es divisible entre 400, también resulta bisiesto.

def anno_bisiesto(n):
    if n % 4 ==0 and n % 100 !=0 or n % 400 == 0:
        return True
    else:
        return False
print(anno_bisiesto(2023))

# Ejercicio 8. Algoritmo que lea un número y diga si es primo o no.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

num = 35
print(es_primo(num))

# Ejercicio 9. Teniendo en cuenta que la clave es “eureka”, escribir un algoritmo
# que nos pida una clave. Solo tenemos 3 intentos para acertar, si fallamos los 3
# intentos nos mostrara un mensaje indicándonos que hemos agotado esos 3
# intentos. (Recomiendo utilizar un interruptor). Si acertamos la clave, saldremos
# directamente del programa. Nota: Obligatorio usar un while.

password = "eureka"
intentos = 0
acertado = False

while intentos < 3 and not acertado:
    clave = input("Introduce la contraseña: ")
    if clave == password:
        acertado = True
        print("Contraseña correcta")
    else:
        intentos += 1
        print("Clave incorrecta. Te quedan", 3 - intentos, "intentos")







