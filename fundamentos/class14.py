# Definición de la función factorial
def factorial(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    else:
        # Caso recursivo: n * factorial de n-1
        return n * factorial(n-1)

# Llamada a la función factorial con el argumento 5
# La función calcula el factorial de 5 de manera recursiva
# y luego el resultado se imprime.
factorial_5 = print(factorial(5))
