# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

EXPECT = 5

guess = 1
print("Too small? I predict True")
print(guess < EXPECT)

guess = 100
print("Too small? I predict False")
print(guess < EXPECT)

guess = 50
print("Too small? I predict False")
print(guess < EXPECT)

guess = 25
print("Too small? I predict False")
print(guess < EXPECT)

guess = 2
print("Too small? I predict True")
print(guess < EXPECT)

guess = 10
print("Too small? I predict True")
print(guess < EXPECT)

guess = 8
print("Too small? I predict True")
print(guess < EXPECT)

guess = 3
print("Too small? I predict True")
print(guess < EXPECT)

guess = 4
print("Too small? I predict True")
print(guess < EXPECT)

guess = 0
print("Too small? I predict True")
print(guess < EXPECT)

guess = 6
print("Too small? I predict True")
print(guess < EXPECT)
