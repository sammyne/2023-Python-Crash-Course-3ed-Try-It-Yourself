# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

## v1
PROMPT = '\nHow old are you?\nEnter "quit" if you do\'t want to answer anymore. '

reply = input(PROMPT)
while reply!='quit':
    age = int(reply)

    if age<3:
        print('Your ticket is free')
    elif age<=12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')

    reply = input('\nHow old are you?\nEnter "quit" if you do\'t want to answer anymore. ')

## v2
active = True
while active:
    reply = input('\nHow old are you?\nEnter "quit" if you do\'t want to answer anymore. ')
    active = reply!='quit'
    if not active:
        break

    age = int(reply)
    if age<3:
        print('Your ticket is free')
    elif age<=12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')

## v3
while True:
    reply = input('\nHow old are you?\nEnter "quit" if you do\'t want to answer anymore. ')
    if reply == 'quit':
        break

    age = int(reply)
    if age<3:
        print('Your ticket is free')
    elif age<=12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
