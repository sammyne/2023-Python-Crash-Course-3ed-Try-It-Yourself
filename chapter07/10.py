# 7-10. Dream Vacation: Write a program that polls users about their dream vaca-
# tion. Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

PROMPT = 'If you could visit one place in the world, where would you go? '

dream_places = []

while True:
    repeat = input("Would you like to take the poll? (yes/no) ")
    if repeat.lower() == 'no':
        break

    reply = input(PROMPT)
    dream_places.append(reply)

print(f"Dream places are: {dream_places}")
