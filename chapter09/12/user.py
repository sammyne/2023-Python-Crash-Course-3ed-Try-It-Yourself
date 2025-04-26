class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'first-name: {self.first_name}, last-name: {self.last_name}, age: {self.age}')

    def greet_user(self):
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')
