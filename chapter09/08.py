# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'first-name: {self.first_name}, last-name: {self.last_name}, age: {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f'privileges: {self.privileges}')

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin = Admin('alice','li',23,privileges)

admin.privileges.show_privileges()
admin.greet_user()
