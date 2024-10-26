# Operadores numéricos
a = 10  # Asigna el valor 10 a la variable a
b = 10  # Asigna el valor 10 a la variable b

print("Suma:", a + b)  # Imprime la suma de a y b: 20
print("Resta:", a - b)  # Imprime la resta de a y b: 0
print("Multiplicación:", a * b)  # Imprime la multiplicación de a y b: 100
print("Potenciación:", a ** b)  # Imprime a elevado a la potencia de b: 10^10 = 10000000000
print("División:", a / b)  # Imprime la división de a entre b: 1.0
print("Parte entera de la división:", a // b)  # Imprime la parte entera de la división de a entre b: 1
print("Módulo:", a % b)  # Imprime el resto de la división de a entre b: 0

a /= 2  # Divide a entre 2 y asigna el resultado a a (a ahora es 5.0)
print(a)  # Imprime el valor actualizado de a: 5.0

operation_1  = 2 + 3 * 4  # Realiza la multiplicación 3 * 4 y luego suma 2: el resultado es 14
operation_2  = (2 + 3) * 4  # Suma 2 + 3 primero (dentro de paréntesis) y luego multiplica por 4: el resultado es 20

print(operation_1)  # Imprime el resultado de operation_1: 14
print(operation_2)  # Imprime el resultado de operation_2: 20

operation_3 = (2 + 3) * (4 ** 2) / 8 - 1  # Realiza operaciones combinadas: 5 * 16 / 8 - 1 = 10 - 1 = 9.0
print(operation_3)  # Imprime el resultado de operation_3: 9.0
