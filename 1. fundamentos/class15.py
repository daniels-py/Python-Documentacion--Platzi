# Ejemplo de manejo de excepciones en Python
# Este programa verifica una lista de datos, intenta convertir cada elemento en un número entero.
# Si no puede hacerlo, maneja la excepción usando try-except y `pass` en ciertos casos.

def process_data(data):
    """
    Toma una lista de datos y procesa cada elemento.
    Convierte cada dato en un entero, si no puede, ignora el error usando pass.
    :param data: list - Lista de elementos que se intentarán convertir a enteros.
    :return: list - Lista de enteros convertidos.
    """
    result = []
    for item in data:
        try:
            # Intentamos convertir el elemento a entero
            number = int(item)
            result.append(number)
        except ValueError:
            # Si el elemento no puede ser convertido, pasamos de él sin hacer nada.
            # Aquí `pass` ignora el error, permitiendo que el programa continúe sin interrupciones.
            pass
    return result


# Lista de datos para probar la función.
# Incluye valores que generarán errores, como cadenas y valores no numéricos.
data_list = ["123", "456", "abc", "789", "xyz"]

# Llamamos a la función para procesar los datos y mostramos el resultado.
processed_data = process_data(data_list)
print("Datos procesados:", processed_data)
