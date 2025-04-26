# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for m in messages:
        print(m)

messages = ['hello', 'world']

show_messages(messages)
