# 10-4. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

from pathlib import Path

path = Path('/tmp/guest.txt')

name = input('Enter your name. ')
path.write_text(name)
