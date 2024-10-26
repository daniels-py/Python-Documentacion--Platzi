# Clase base que representa un Vehículo
class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulación de los atributos de marca, modelo y precio
        self.brand = brand
        self.model = model
        self.price = price
        # Atributo de disponibilidad; inicialmente, todos los vehículos están disponibles
        self.is_available = True

    def sell(self):
        # Método para vender el vehículo si está disponible
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} no está disponible")

    # Abstracción: método para verificar la disponibilidad del vehículo
    def check_available(self):
        return self.is_available

    # Abstracción: método para obtener el precio del vehículo
    def get_price(self):
        return self.price

    # Método abstracto para arrancar el motor, a implementar en subclases
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    # Método abstracto para detener el motor, a implementar en subclases
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clase que representa un coche y hereda de Vehicle
class Car(Vehicle):
    # Implementación del método abstracto start_engine (polimorfismo)
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"

    # Implementación del método abstracto stop_engine (polimorfismo)
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"

# Clase que representa una bicicleta y hereda de Vehicle
class Bike(Vehicle):
    # Implementación específica de start_engine para Bike
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"

    # Implementación específica de stop_engine para Bike
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"

# Clase que representa un camión y hereda de Vehicle
class Truck(Vehicle):
    # Implementación específica de start_engine para Truck
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"

    # Implementación específica de stop_engine para Truck
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"

# Clase que representa un cliente
class Customer:
    def __init__(self, name):
        self.name = name  # Nombre del cliente
        self.purchased_vehicles = []  # Lista de vehículos comprados por el cliente

    # Método para comprar un vehículo
    def buy_vehicle(self, vehicle: Vehicle):
        # Verifica disponibilidad antes de realizar la compra
        if vehicle.check_available():
            vehicle.sell()  # Marca el vehículo como vendido
            self.purchased_vehicles.append(vehicle)  # Añade a la lista de compras
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible")

    # Método para consultar la disponibilidad y el precio de un vehículo
    def inquire_vehicle(self, vehicle: Vehicle):
        availability = "Disponible" if vehicle.check_available() else "No disponible"
        print(f"El {vehicle.brand} está {availability} y cuesta {vehicle.get_price()}")

# Clase que representa una concesionaria
class Dealership:
    def __init__(self):
        self.inventory = []  # Lista de vehículos en el inventario
        self.customers = []  # Lista de clientes registrados

    # Método para añadir vehículos al inventario
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    # Método para registrar nuevos clientes en la concesionaria
    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    # Método para mostrar todos los vehículos disponibles en el inventario
    def show_available_vehicle(self):
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

# Crear instancias de vehículos específicos
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

# Crear instancia de cliente
customer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar vehículos y clientes
dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Mostrar los vehículos disponibles
dealership.show_available_vehicle()

# Cliente consulta la disponibilidad y precio de un vehículo
customer1.inquire_vehicle(car1)

# Cliente compra un vehículo
customer1.buy_vehicle(car1)

# Mostrar nuevamente los vehículos disponibles
dealership.show_available_vehicle()
