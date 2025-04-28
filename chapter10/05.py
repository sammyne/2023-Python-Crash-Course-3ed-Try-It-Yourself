# 10-5. Guest Book: Write a while loop that prompts users for their name. Collect
# all the names that are entered, and then write these names to a file called
# guest_book.txt. Make sure each entry appears on a new line in the file.

from pathlib import Path

path = Path('/tmp/guest_book.txt')

content = ''
while True:
    name = input('Enter your name. (Enter "q" to quit.) ')
    if name =='q':
        break

    content += name + '\n'

content = content[:-1]
path.write_text(f'{content}\n')
