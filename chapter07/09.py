# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

none = 'pastrami'
sandwich_orders = ['ham',none,'chicken',none,'turkey',none]
finished_sandwiches = []

print(f'the deli has # run out of {none}')

while none in sandwich_orders:
    sandwich_orders.remove(none)

while sandwich_orders:
    o = sandwich_orders.pop()
    print(f'I made your {o} sandwich')
    finished_sandwiches.append(o)

print(f'We made: {finished_sandwiches}')
print(f'None of them is {none}: {none not in finished_sandwiches}')
