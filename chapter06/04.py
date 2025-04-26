# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    'string': 'a list a char',
    'number': 'a integer or floating point number',
    'list': 'an collection of data',
    'if': 'used for testing conditions',
    'len()': 'function get data length',
}

for k,v in glossary.items():
    print(f"{k}: {v}")

print("\nafter adding more")
glossary['c'] = "it's programming language"
for k,v in glossary.items():
    print(f"{k}: {v}")
