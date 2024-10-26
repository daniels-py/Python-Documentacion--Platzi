# Solicita al usuario que ingrese su nombre
name = input("Ingrese su nombre: ")  
print(name)  # Imprime el nombre ingresado por el usuario
print(type(name))  # Imprime el tipo de datos de name (siempre será <class 'str'>, cadena de texto)

# Solicita al usuario que ingrese su edad y la convierte a entero
age = int(input("Ingrese su edad: "))  
print(type(age))  # Imprime el tipo de datos de age (será <class 'int'>, entero)

# Solicita al usuario que ingrese un número grande y lo convierte a flotante
number = float(input("Ingresa un número grande: "))  
print(type(number))  # Imprime el tipo de datos de number (será <class 'float'>, flotante)
