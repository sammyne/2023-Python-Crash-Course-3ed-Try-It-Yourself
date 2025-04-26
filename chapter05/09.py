# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# - If the list is empty, print the message We need to find some users!
# - Remove all of the usernames from your list, and make sure the correct mes-
# sage is printed.

users = ["admin","alice","bob","carol","david","emma"]

if not users:
    print("We need to find some users!")

users = []

print("check again")
if not users:
    print("We need to find some users!")
