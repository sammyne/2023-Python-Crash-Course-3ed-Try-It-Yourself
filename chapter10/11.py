# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message “I know your favorite
# number! It’s _____.”

from pathlib import Path
import json

PATH = '/tmp/hell-world.txt'

try:
    n = input('Enter your favorite number. ')
    n = int(n)

    out = json.dumps(n)
    Path(PATH).write_text(out)
except ValueError:
    print("parse input as int")

try:
    encoded = Path(PATH).read_text()
    n = json.loads(encoded)
    print(f"I know your favorite # number! It's {n}.")
except FileNotFoundError:
    print('file not found')
