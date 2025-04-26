# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'name: {self.name}, cuisine_type: {self.cuisine_type}')

    def open_restaurant(self):
        print("open")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print(f'we have flavors: {self.flavors}')

stand = IceCreamStand('mixuebingcheng', 'sweet', ['icy','plain'])
stand.print_flavors()
