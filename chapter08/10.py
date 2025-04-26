# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

def send_messages(messages,sent_messages):
    while messages:
        m = messages.pop(0)
        print(m)
        sent_messages.append(m)


messages = ['hello', 'world']
sent_messages = []

send_messages(messages,sent_messages)

print('\nafter sending')
print(f'messages: {messages}')
print(f'sent-messages: {sent_messages}')
