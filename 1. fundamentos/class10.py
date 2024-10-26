# Definición de un diccionario donde claves son números y valores son sus nombres en español
numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers[2])  # Imprime el valor asociado a la clave 2: "dos"

# Definición de un diccionario con información personal
information = {"nombre": "Carla", 
               "Apellido": "Florida", 
               "Altura": 1.60, 
               "Edad": 29}

print(information)  # Imprime todo el diccionario information

# Eliminación de una clave y su valor del diccionario
del information["Edad"]  # Elimina la entrada con clave "Edad"
print(information)  # Imprime el diccionario information después de eliminar "Edad"

# Obtención de las claves del diccionario
claves = information.keys()
print(claves)  # Imprime todas las claves del diccionario information

# Obtención de los valores del diccionario
values = information.values()
print(values)  # Imprime todos los valores del diccionario information

# Obtención de pares clave-valor del diccionario
pairs = information.items()
print(pairs)  # Imprime todos los pares clave-valor del diccionario information

# Definición de un diccionario anidado (un diccionario dentro de otro)
contacts = {"Carla": {"Apellido": "Florida", 
                      "Altura": 1.60, 
                      "Edad": 29},

            "Daniel": {"Apellido": "Ramirez", 
                      "Altura": 1.70, 
                      "Edad": 20}}

# Acceso a un elemento específico dentro del diccionario anidado
print(contacts["Carla"])  # Imprime el diccionario asociado a la clave "Carla"
