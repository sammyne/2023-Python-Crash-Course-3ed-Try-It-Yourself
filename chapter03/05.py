# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.

guests = ["alice", "bob", "carol"]

print(f"Would you like to my dinner, {guests[0]}?")
print(f"Would you like to my dinner, {guests[1]}?")
print(f"Would you like to my dinner, {guests[2]}?")

unavailable = guests[1]
print(f"Sorry for {unavailable}'s unavailability :(")

guests[1] = "david"
print(f"Would you like to my dinner, {guests[0]}?")
print(f"Would you like to my dinner, {guests[1]}?")
print(f"Would you like to my dinner, {guests[2]}?")
