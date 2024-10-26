# Definición de una lista de números
numeber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bucle for para iterar sobre cada elemento de la lista 'numeber'
for i in numeber:
    # Imprime cada número de la lista incrementado en 1
    print(i + 1)

# Bucle for utilizando la función range para iterar desde el número 3 hasta el 9
for i in range(3, 10):
    # Imprime cada número en el rango de 3 a 9 (10 no se incluye)
    print(i)


# Definición de una lista de frutas
fruits = ["mannzana", "pera", "fresa"]

# Bucle for para iterar sobre cada elemento de la lista 'fruits'
for fruit in fruits:
    print(fruit)  # Imprime cada fruta
    # Si la fruta es "fresa", imprime un mensaje adicional
    if fruit == "fresa":
        print("La fruta se encuentra en la tienda")


# Definición de una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Bucle for para iterar sobre cada elemento de la lista 'numbers'
for i in numbers:
    # Imprime el valor de i incrementado en 1
    print("Aquí i es igual a:", i + 1)

# Otro bucle for utilizando la función range para iterar desde 3 hasta 9
for i in range(3, 10):
    # Imprime cada número en el rango de 3 a 9 (10 no se incluye)
    print(i)

# Definición de una lista de frutas
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]

# Bucle for para iterar sobre cada elemento de la lista 'fruits'
for fruit in fruits:
    print(fruit)  # Imprime cada fruta
    # Si la fruta es "Naranja", imprime un mensaje adicional
    if fruit == "Naranja":
        print("Naranja encontrada")


# Inicialización de una variable x con valor 0
x = 0

# Bucle while que se ejecuta mientras x sea menor que 5
while x < 5:
    # Si x es igual a 3, interrumpe el bucle con 'break'
    if x == 3:
        break
    # Imprime el valor actual de x
    print(x)
    # Incrementa x en 1 en cada iteración
    x += 1


# Definición de una lista de números
numbers = [1, 2, 3, 4, 5, 6]

# Bucle for para iterar sobre cada elemento de la lista 'numbers'
for i in numbers:
    # Si i es igual a 3, interrumpe el bucle con 'break'
    if i == 3:
        break
    # Imprime el valor actual de i
    print("Aquí i es igual a:", i)
