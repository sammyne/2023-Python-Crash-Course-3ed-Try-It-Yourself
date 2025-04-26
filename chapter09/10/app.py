from restaurant import Restaurant

r = Restaurant('lakeke','spicy')

print(f'number-served: {r.number_served}')

r.number_served = 123
print(f'number-served: {r.number_served}')

r.set_number_served(200)
print(f'number-served: {r.number_served}')

r.increment_number_served(1)
print(f'number-served: {r.number_served}')
