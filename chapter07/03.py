# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

reply = input('Give me a number. ')
num = int(reply)
print(f'Is your number a multiple of 10? {num%10==0}')
