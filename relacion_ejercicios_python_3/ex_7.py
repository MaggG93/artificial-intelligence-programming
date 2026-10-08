# Escribe un programa en Python que acepte una lista de listas
# representando una matriz numérica y compute la suma de los elementos de la
# diagonal principal.
# Entrada: [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
# Salida: 20

a = [[1, 2], [3, 4]]
b = [[4, 5], [8, 9]]

c = []

for fila in range(len(a)):
    d = []
    for col in range(len(a[0])):
        suma = a[fila][col] + b[fila][col]
        d.append(suma)
    c.append(d)

print(c)

