name = 'Daniel'  # Define la variable name con la cadena 'Daniel'
last_name = '   Ramirez     Saavedra  '  # Define la variable last_name con la cadena '   Ramirez     Saavedra  '

print(5 * name)  # Imprime la cadena 'Daniel' repetida 5 veces: 'DanielDanielDanielDanielDaniel'
print(name + ' ' + last_name)  # Imprime la concatenación de name, un espacio, y last_name: 'Daniel    Ramirez     Saavedra  '

print(len(name))  # Imprime la longitud de la cadena name (6 caracteres en 'Daniel')
print(len(last_name))  # Imprime la longitud de la cadena last_name (con los espacios incluidos)

print(name.lower())  # Imprime la cadena name en minúsculas: 'daniel'
print(name.upper())  # Imprime la cadena name en mayúsculas: 'DANIEL'

print(last_name.strip())  # Imprime la cadena last_name sin espacios al principio ni al final: 'Ramirez     Saavedra'
