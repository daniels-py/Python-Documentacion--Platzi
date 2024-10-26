# Creacion de la clase 
class Person: 

    # Contructor para definir los parametros clave de nuestra clase
    def __init__(self, name , age ):
        self.name = name
        self. age = age

    # esta funcion servira para hacer una interaccion con nuestra clase para que pueda hacer determinadas acciones en este caso un saludo
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")


# para hacer ejemplo en un punto mas en concreto asiganamos variables para que ejecuten la funcion del saludo
person1 = Person("Ana" ,30)
person2 = Person("Daniel",21)

person1.greet()
person2.greet()