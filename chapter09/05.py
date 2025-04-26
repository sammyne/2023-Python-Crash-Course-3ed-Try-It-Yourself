# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'first-name: {self.first_name}, last-name: {self.last_name}, age: {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('alice','li',12)
print(f'login-attempts: {user.login_attempts}')

for i in range(1,5):
    user.increment_login_attempts()

print(f'login-attempts: {user.login_attempts}')

user.reset_login_attempts()
print(f'login-attempts: {user.login_attempts}')
