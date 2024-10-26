# Definimos que el usuario es miembro
is_member = True
# Definimos la edad del usuario
age = 11

# Verificamos si es miembro
if is_member:
    # Si es miembro, verificamos si su edad es mayor o igual a 15
    if age >= 15:
        # Si la edad es suficiente, tiene acceso
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        # Si es menor de 15, no tiene acceso aunque sea miembro
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    # Si no es miembro, no tiene acceso
    print("No eres miembro y NO TIENES ACCESO")


# Definimos un valor para x
x = 5

# Verificamos si x es mayor que 5
if x > 5:
    print("X es mayor que 5")
# Si x no es mayor que 5, verificamos si es igual a 5
elif x == 5:
    print("X es igual que 5")
# Si ninguna de las anteriores es verdadera, entonces x es menor que 5
else:
    print("X es menor que 5")
# Imprimimos un mensaje fuera de las condiciones
print("afuera")


# Definimos valores para x y y
x = 15
y = 20

# Verificamos si x es mayor que 10 y y es mayor que 25 al mismo tiempo
if x > 10 and y > 25:
    # Si ambos son verdaderos, imprimimos el mensaje
    print("X es mayor que 10 y Y es mayor que 15")

# Verificamos si x es mayor que 10 o y es mayor que 25 (solo una de las dos debe cumplirse)
if x > 10 or y > 25:
    # Si al menos una es verdadera, imprimimos el mensaje
    print("X es mayor que 10 O Y es Mayor que 25")

# Usamos "not" para verificar si x NO es mayor que 10
if not x > 10:
    # Si x no es mayor que 10, imprimimos el mensaje
    print("X no es mayor que 10")
