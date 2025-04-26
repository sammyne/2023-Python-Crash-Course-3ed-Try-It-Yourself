# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing, to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for v in my_foods:
    print(v)

print("\nMy friend's favorite foods are:")
for v in friend_foods:
    print(v)
