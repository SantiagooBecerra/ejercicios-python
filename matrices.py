# Ejercicio 1
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for fila in matriz:
    print(fila)

# Ejercicio 
numeros = []
for _ in range(4):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

print([numeros[0], numeros[1]])
print([numeros[2], numeros[3]])

# Ejercicio 3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
suma = 0
for fila in matriz:
    suma += sum(fila)
print("Suma de los elementos:", suma)

# Ejercicio 4
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Diagonal principal:")
for i in range(3):
    print(matriz[i][i])