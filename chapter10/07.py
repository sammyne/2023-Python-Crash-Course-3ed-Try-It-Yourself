# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
# so the user can continue entering numbers, even if they make a mistake and
# enter text instead of a number.

from pathlib import Path

path = Path('/tmp/guest_book.txt')

content = ''
while True:
    n = input('Enter your name. (Enter "q" to quit.) ')
    if n =='q':
        break

    try:
        n = int(n)
    except ValueError:
        print(f'Invalid number {n} is skipped')
        continue

    content += str(n) + '\n'

content = content[:-1]
path.write_text(f'{content}\n')
