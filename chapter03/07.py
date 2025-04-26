# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

guests = ["alice", "bob", "carol"]

print(f"Would you like to my dinner, {guests[0]}?")
print(f"Would you like to my dinner, {guests[1]}?")
print(f"Would you like to my dinner, {guests[2]}?")

david = "david"
emma = "emma"
frank = "frank"

print(f"I found a bigger table. Would you like to come, {david}, {emma}, {frank}")

guests.insert(0, david)
guests.insert(2, emma)
guests.append(frank)

print(f"Would you like to my dinner, {guests[0]}?")
print(f"Would you like to my dinner, {guests[1]}?")
print(f"Would you like to my dinner, {guests[2]}?")
print(f"Would you like to my dinner, {guests[3]}?")
print(f"Would you like to my dinner, {guests[4]}?")
print(f"Would you like to my dinner, {guests[5]}?")

cancelled = guests.pop()
print(f"Sorry for cancel, {cancelled}")
cancelled = guests.pop()
print(f"Sorry for cancel, {cancelled}")
cancelled = guests.pop()
print(f"Sorry for cancel, {cancelled}")
cancelled = guests.pop()
print(f"Sorry for cancel, {cancelled}")

print(f"Would you still like to my dinner, {guests[0]}?")
print(f"Would you still like to my dinner, {guests[1]}?")

del guests[0]
del guests[0]
print(f"I should miss {len(guests)} guests?")
