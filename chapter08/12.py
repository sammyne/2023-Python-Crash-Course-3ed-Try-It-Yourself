# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

def make_sandwich(*items):
    print(f"Your sandwich will be made with {items}")

make_sandwich('apple','orange')
make_sandwich('apple','orange','banana')
make_sandwich('apple','orange','grape','salt')
