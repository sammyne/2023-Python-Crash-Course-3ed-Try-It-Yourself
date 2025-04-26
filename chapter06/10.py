# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

numbers = {
    "alice": [1,10],
    "bob": [2,20],
    'carol': [3,30],
    'david': [4,40],
    'emma': [5,50],
}

for name, nums in numbers.items():
   print(f'{name} loves {nums}')
