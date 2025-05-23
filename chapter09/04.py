# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
#     Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
#     Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'name: {self.name}, cuisine_type: {self.cuisine_type}')

    def open_restaurant(self):
        print("open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

r = Restaurant('lakeke','spicy')

print(f'number-served: {r.number_served}')

r.number_served = 123
print(f'number-served: {r.number_served}')

r.set_number_served(200)
print(f'number-served: {r.number_served}')

r.increment_number_served(1)
print(f'number-served: {r.number_served}')
