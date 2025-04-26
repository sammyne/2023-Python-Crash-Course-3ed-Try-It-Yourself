# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

reply = input('How many people are there in your dinner group? ')
group_size = int(reply)

if group_size>8:
    print('You\'ll have to wait for a table')
else:
    print('Your table is ready')
