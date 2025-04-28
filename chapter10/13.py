# 10-13. User Dictionary: The remember_me.py example only stores one piece of
# information, the username. Expand this example by asking for two more pieces
# of information about the user, then store all the information you collect in a
# dictionary. Write this dictionary to a file using json.dumps(), and read it back
# in using json.loads(). Print a summary showing exactly what your program
# remembers about the user.

from pathlib import Path
import json

PATH = '/tmp/users.json'

users=[]
while True:
    print('Enter your name, age, gender(m/f). Enter "q" if you want to quit.')
    name = input('Name ')
    if name =='q':
        break

    age = input('Age ')
    if age =='q':
        break

    gender = input('Gender ')
    if gender=='q':
        break

    user = {'name': name, 'age': int(age), 'gender': gender}
    users.append(user)

encoded = json.dumps(users)
Path(PATH).write_text(encoded)

try:
    encoded = Path(PATH).read_text()
    users = json.loads(encoded)
    print('I remember all of')
    print(users)
except FileNotFoundError:
   print('file NOT FOUND')
