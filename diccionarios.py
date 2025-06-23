# Ejercicio 1
alumno = {
    "nombre": "Juan",
    "edad": 20,
    "curso": "Matemáticas"
}
print("Datos del alumno:")
for valor in alumno.values():
    print(valor)


# Ejercicio 2
estudiantes = {}
for i in range(3):
    nombre = input(">> Ingrese el nombre del estudiante: ")
    nota = float(input(f">> Ingrese la nota de {nombre}: "))
    print("----------------------------------------------------")
    estudiantes[nombre] = nota

promedio = sum(estudiantes.values()) / len(estudiantes)
print("Promedio general:", promedio)


# Ejercicio 3 
productos = {}

for i in range(2):
    nombre = (input("Ingrese el nombre del producto: "))
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    stock = int(input(f"Ingrese el stock disponible de {nombre}: "))
    productos[nombre] = {"precio": precio, "stock": stock}

nombres = list(productos.keys())

# Supongamos que tienes el diccionario productos ya cargado
stock1 = productos[nombres[0]]["stock"]
stock2 = productos[nombres[1]]["stock"]

if stock1 > stock2:
    print(f'El producto con más stock es: {nombres[0]}')
elif stock2 > stock1:
    print(f'El producto con más stock es: {nombres[1]}')
else:
    print("Ambos productos tienen el mismo stock.")
