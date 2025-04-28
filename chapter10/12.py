# 10-12. Favorite Number Remembered: Combine the two programs you wrote in
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message “I know your favorite
# number! It’s _____.”

from pathlib import Path
import json

PATH = '/tmp/hell-world.txt'

try:
    encoded = Path(PATH).read_text()
    n = json.loads(encoded)
    print(f"I know your favorite # number! It's {n}.")
except FileNotFoundError:
    try:
        n = input('Enter your favorite number. ')
        n = int(n)

        out = json.dumps(n)
        Path(PATH).write_text(out)
    except ValueError:
        print("parse input as int")
