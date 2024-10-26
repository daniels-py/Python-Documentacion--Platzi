# Crear un iterador para los números impares

# Límite superior para la secuencia de números impares
limit = 10

# Crear iterador para números impares desde 1 hasta el límite
odd_itter = iter(range(1, limit + 1, 2))

# Usar el iterador en un bucle for para imprimir cada número impar
for num in odd_itter:
    print(num)  # Imprime los números impares: 1, 3, 5, 7, 9


# Iterar en cadenas de texto

# Creando una cadena de texto
text = "Hola mundo"

# Creando un iterador para la cadena de texto
iter_text = iter(text)

# Usar el iterador en un bucle for para imprimir cada carácter de la cadena
for char in iter_text:
    print(char)  # Imprime cada carácter de la cadena "Hola mundo"


# Ejemplo de uso directo de un iterador

# Crear una lista
my_list = [1, 2, 3, 4]

# Obtener un iterador de la lista
my_iter = iter(my_list)

# Usar el iterador para obtener elementos uno por uno con next()
print(next(my_iter))  # Imprime el primer elemento de la lista: 1
print(next(my_iter))  # Imprime el segundo elemento de la lista: 2
print(next(my_iter))  # Imprime el tercer elemento de la lista: 3
print(next(my_iter))  # Imprime el cuarto elemento de la lista: 4

# Si se descomenta la siguiente línea, generará un error StopIteration porque ya no quedan elementos en el iterador
# print(next(my_iter))  



# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))

