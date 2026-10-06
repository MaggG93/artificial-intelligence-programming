# FUNCION SUMA
def sumar():
    print("Has elegido sumar.")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    return num1 + num2

# FUNCION RESTA
def restar():
    print("Has elegido restar.")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    return num1 - num2

# FUNCION MULTIPLICACION
def multiplicar():
    print("Has elegido multiplicar.")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado = 0
    for i in range(int(abs(num2))):
        resultado += num1

    return resultado

# FUNCION DIVISION
def dividir():
    print("Has elegido dividir.")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if num1 < 0 or num2 < 0:

        print("Solo se admiten números positivos.")
        return None

    resultado = 0
    while num1 >= num2:
        num1 -= num2
        resultado += 1

    print(f"Cociente: {resultado}, resto: {num1}")
    return resultado

# MENU CALCULADORA
while True:
    operacion = input("Elige una operación (1. sumar, 2. restar, 3. multiplicar, 4. dividir, 5. salir): ")

    match operacion:
        case "1":
            resultado = sumar()
            print(f"Resultado: {resultado}")

        case "2":
            resultado = restar()
            print(f"Resultado: {resultado}")

        case "3":
            resultado = multiplicar()
            print(f"Resultado: {resultado}")

        case "4":
            resultado = dividir()
            print(f"Resultado: {resultado}")

        case "5":
            print("Saliendo de la calculadora.")
            break

        case _:
            print("Operación no válida")