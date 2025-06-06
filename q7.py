class Car:
    def __init__(self, make, model, year):            #Using __init__ to assign initial values to object properties
        self.make = make
        self.model = model
        self.year = year
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def describe_car(self):                           #Object method describe_car()
        print(self.make, self.model, self.year)       #Printing object properties


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

c1 = Car("Toyota", "Corolla", 2020)    #Create instance of Car class c1
c1.describe_car()                                        #Calling describe_car method
