a = [1, 2, 3, 4, 5]  # Crea una lista y la asigna a la variable a
b = a  # Asigna la referencia de la lista a la variable b (b apunta a la misma lista que a)

print(a)  # Imprime la lista a: [1, 2, 3, 4, 5]
print(b)  # Imprime la lista b, que es la misma que a: [1, 2, 3, 4, 5]

del a[0]  # Elimina el primer elemento de la lista a
print(a)  # Imprime la lista a después de eliminar el primer elemento: [2, 3, 4, 5]
print(b)  # Imprime la lista b; b también refleja el cambio porque b y a son la misma lista: [2, 3, 4, 5]

print(id(a))  # Imprime el ID de la lista a (una especie de "dirección" en la memoria)
print(id(b))  # Imprime el ID de la lista b (debe ser igual al ID de a, porque apuntan a la misma lista)

c = a[:]  # Crea una copia superficial de la lista a y la asigna a c (c es una lista nueva)
print(id(a))  # Imprime el ID de la lista a (sin cambios)
print(id(b))  # Imprime el ID de la lista b (sin cambios)
print(id(c))  # Imprime el ID de la lista c (debe ser diferente porque c es una copia independiente)

a.append(6)  # Agrega el número 6 al final de la lista a
print(a)  # Imprime la lista a después de agregar 6: [2, 3, 4, 5, 6]
print(b)  # Imprime la lista b; b también refleja el cambio porque sigue siendo la misma lista que a: [2, 3, 4, 5, 6]
print(c)  # Imprime la lista c; c no cambia porque es una copia independiente: [2, 3, 4, 5]


#ejemplo 

lista1=[1,2,3,4,5]
lista2=lista1.copy()

lista2.append(6)

print(lista1)
print(lista2)