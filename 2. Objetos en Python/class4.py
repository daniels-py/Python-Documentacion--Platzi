class Car:
    """
    Clase que representa un coche con atributos básicos.
    
    Atributos:
        - brand (str): Marca del coche.
        - model (str): Modelo del coche.
        - price (float): Precio del coche.
        - is_available (bool): Estado de disponibilidad del coche.
    """

    def __init__(self, brand, model, price):
        """
        Constructor de la clase Car que inicializa los atributos del coche.
        
        Parámetros:
            - brand (str): Marca del coche.
            - model (str): Modelo del coche.
            - price (float): Precio del coche.
        """
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True  # Por defecto, el coche está disponible.

    def sell(self):
        """
        Marca el coche como no disponible si está disponible.
        Muestra un mensaje indicando si el coche ha sido vendido o si ya estaba vendido.
        """
        if self.is_available:
            self.is_available = False
            print(f"El coche {self.brand} {self.model} ha sido vendido.")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible.")

    def check_availability(self):
        """
        Verifica la disponibilidad del coche.
        
        Retorna:
            bool: True si el coche está disponible, False si no.
        """
        return self.is_available

    def get_price(self):
        """
        Obtiene el precio del coche.
        
        Retorna:
            float: Precio del coche.
        """
        return self.price


class Customer:
    """
    Clase que representa un cliente que puede comprar coches.
    
    Atributos:
        - name (str): Nombre del cliente.
        - cars_purchased (list): Lista de coches que el cliente ha comprado.
    """

    def __init__(self, name):
        """
        Constructor de la clase Customer que inicializa el nombre del cliente.
        
        Parámetros:
            - name (str): Nombre del cliente.
        """
        self.name = name
        self.cars_purchased = []  # Lista vacía de coches comprados.

    def buy_car(self, car):
        """
        Permite al cliente comprar un coche si está disponible.
        Marca el coche como vendido y lo añade a la lista de coches comprados.
        
        Parámetros:
            - car (Car): Instancia del coche que el cliente desea comprar.
        """
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Lo siento, {car.brand} {car.model} no está disponible.")

    def inquire_car(self, car):
        """
        Permite al cliente consultar la disponibilidad y precio de un coche.
        
        Parámetros:
            - car (Car): Instancia del coche a consultar.
        """
        availability = "disponible" if car.check_availability() else "no disponible"
        print(f"El coche {car.brand} {car.model} está {availability} y cuesta {car.get_price()}.")


class Dealership:
    """
    Clase que representa una concesionaria que gestiona coches y clientes.
    
    Atributos:
        - inventory (list): Lista de coches disponibles en la concesionaria.
        - customers (list): Lista de clientes registrados en la concesionaria.
    """

    def __init__(self):
        """
        Constructor de la clase Dealership que inicializa el inventario de coches y la lista de clientes.
        """
        self.inventory = []  # Lista vacía de coches en inventario.
        self.customers = []  # Lista vacía de clientes registrados.

    def add_car(self, car):
        """
        Añade un coche al inventario de la concesionaria.
        
        Parámetros:
            - car (Car): Instancia del coche a añadir.
        """
        self.inventory.append(car)
        print(f"El coche {car.brand} {car.model} ha sido añadido al inventario.")

    def register_customer(self, customer):
        """
        Registra un cliente en la concesionaria.
        
        Parámetros:
            - customer (Customer): Instancia del cliente a registrar.
        """
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la concesionaria.")

    def show_available_cars(self):
        """
        Muestra los coches disponibles en el inventario de la concesionaria.
        """
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_availability():
                print(f"- {car.brand} {car.model} por {car.get_price()}")


# Crear instancias de coches
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

# Crear instancia de cliente
customer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar coches y clientes
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.register_customer(customer1)

# Mostrar coches disponibles
dealership.show_available_cars()

# Cliente consulta un coche
customer1.inquire_car(car1)

# Cliente compra un coche
customer1.buy_car(car1)

# Mostrar coches disponibles nuevamente
dealership.show_available_cars()

# Cliente intenta comprar un coche ya vendido
customer1.buy_car(car1)
