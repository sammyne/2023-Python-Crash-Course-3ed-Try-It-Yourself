# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'name: {self.name}, cuisine_type: {self.cuisine_type}')

    def open_restaurant(self):
        print("open")

r1 = Restaurant('lakeke', 'spicy')
r2 = Restaurant('shidexi', 'sweet')
r3 = Restaurant('taotaoju', 'sweet')

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
