# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pets = [
    {
        'owner': 'alice',
        'kind':'cat',
    },
    {
        'owner':'bob',
        'kind':'dog',
    }
]

for pet in pets:
    print('---')
    for field,value in pet.items():
        print(f'- {field}: {value}')
