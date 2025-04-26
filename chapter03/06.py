# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

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
