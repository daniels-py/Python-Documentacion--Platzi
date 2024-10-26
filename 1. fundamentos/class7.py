#listas

# Lista de tareas
to_do = ["Dirigirnos al hotel", "Ir a almorzar", "Visitar un museo", "Volver al hotel"]
print(to_do)  # Imprime la lista to_do

# Lista con diferentes tipos de elementos
numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers))  # Imprime el tipo de datos de la lista numbers (será <class 'list'>)

# Lista con elementos de diferentes tipos
mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)  # Imprime la lista mix
print(len(mix))  # Imprime la longitud de la lista mix (cantidad de elementos)

# Acceso a elementos de la lista
print("Primer elemento", mix[0])  # Imprime el primer elemento de mix: 'uno'
print("Segundo elemento", mix[1])  # Imprime el segundo elemento de mix: 2
print("Último elemento:", mix[-1])  # Imprime el último elemento de mix: [1, 2, 3]

# Operaciones con una cadena de texto
string = "Hola mundo"
print("Primer elemento", string[0])  # Imprime el primer carácter de string: 'H'
print("Segundo elemento", string[1])  # Imprime el segundo carácter de string: 'o'
print("Último elemento:", string[-1])  # Imprime el último carácter de string: 'o'

# Slicing de la lista mix
print(mix[2:-2])  # Imprime los elementos de mix desde el índice 2 hasta el penúltimo: [3.14]

# Modificación de la lista mix
print(mix)  # Imprime la lista mix original
mix.append(False)  # Agrega el valor False al final de mix
print(mix)  # Imprime la lista mix después de agregar False
mix.append(["a", "b"])  # Agrega la lista ["a", "b"] al final de mix
print(mix)  # Imprime la lista mix después de agregar ["a", "b"]
mix.insert(1, ["a", "b"])  # Inserta la lista ["a", "b"] en el índice 1 de mix
print(mix)  # Imprime la lista mix después de insertar ["a", "b"] en la posición 1
print(mix.index(["a", "b"]))  # Imprime el índice de la primera aparición de ["a", "b"] en mix

# Operaciones con una lista de números
numbers = [1, 2, 100.01, 90.45, 3, 4, 5]
print(numbers)  # Imprime la lista numbers
print("Mayor:", max(numbers))  # Imprime el mayor valor en la lista numbers: 100.01
print("Menor:", min(numbers))  # Imprime el menor valor en la lista numbers: 1

# Eliminación de elementos de la lista
del numbers[-1]  # Elimina el último elemento de la lista numbers
print(numbers)  # Imprime la lista numbers después de eliminar el último elemento
del numbers[:2]  # Elimina los primeros dos elementos de la lista numbers
print(numbers)  # Imprime la lista numbers después de eliminar los primeros dos elementos
del numbers  # Elimina completamente la lista numbers

# La siguiente línea está comentada porque numbers ya no existe
# print(numbers)
