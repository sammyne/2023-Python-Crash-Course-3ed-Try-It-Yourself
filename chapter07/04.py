# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

PROMPT = '\nPlease add topping you like?\n(Enter "quit" when you are finished.) '

while True:
    reply = input(PROMPT)
    if reply=='quit':
        break
    print(f"I'll add {reply} to your pizza")
