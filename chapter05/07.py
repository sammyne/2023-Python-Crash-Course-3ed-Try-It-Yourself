# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

favorite_fruits = ["apple", "banana", "orange"]

fruit = "apple"
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")

fruit = "grape"
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")

fruit = "cherry"
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")

fruit = "banana"
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")

fruit = "pitaya"
if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
