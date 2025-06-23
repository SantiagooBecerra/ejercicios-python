# Ejercicio 1
numeros = [1,3,10,12]
print("El mayor es:", max(numeros))
print("--------------------------------------------------------------------------")


# Ejercicio 2
nombres = []
for i in range(4):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
print("--------------------------------------------------------------------------")
print("Nombres en orden inverso:")
for nombre in reversed(nombres):
    print(">>",nombre)

# Ejercicio 3
total = 0
for i in range(3):
    nombre = input("Ingrese el nombre de un producto: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    total += precio
print("Total a pagar:", total)
