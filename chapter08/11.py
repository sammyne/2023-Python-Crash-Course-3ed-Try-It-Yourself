# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
# tion send_messages() with a copy of the list of messages. After calling the func-
# tion, print both of your lists to show that the original list has retained its messages.

def send_messages(messages,sent_messages):
    while messages:
        m = messages.pop(0)
        print(m)
        sent_messages.append(m)


messages = ['hello', 'world']
sent_messages = []

send_messages(messages[:],sent_messages)

print('\nafter sending')
print(f'messages: {messages}')
print(f'sent-messages: {sent_messages}')
