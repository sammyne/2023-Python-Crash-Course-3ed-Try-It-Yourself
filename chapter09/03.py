# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both meth-
# ods for each user.

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'first-name: {self.first_name}, last-name: {self.last_name}, age: {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')

users = [
    User('alice', 'li', 12),
    User('bob', 'zhao', 23),
    User('carol', 'qian', 34),
]

for user in users:
    user.describe_user()
    user.greet_user()
