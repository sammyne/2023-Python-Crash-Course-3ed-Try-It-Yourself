# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'first-name: {self.first_name}, last-name: {self.last_name}, age: {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

    def show_privileges(self):
        print(f'privileges: {self.privileges}')

admin = Admin('alice','li',23,["can add post", "can delete post", "can ban user"])

admin.show_privileges()
admin.greet_user()
