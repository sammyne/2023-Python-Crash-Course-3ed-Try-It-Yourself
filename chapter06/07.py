# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionar-
# ies in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

people = [
   {
       'name': 'alice',
    "age": 45,
    "city": "Shanghai",
   },
   {
       'name':'bob',
       'age': 12,
       'city': 'Guangzhou'
   },
   {
       'name':'carol',
       'age': 30,
       'city': 'Beijing'
   }
]

for v in people:
    print('---')
    for field, value in v.items():
        print(f"- {field}: {value}")
