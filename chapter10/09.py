# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

from pathlib import Path

def show(file_path):
        content = Path(file_path).read_text()
        print(f'{file_path} has')
        print(content)

for p in ['data/cats.txt', 'data/dogs1.txt']:
    try:
        show(p)
    except FileNotFoundError:
        pass
