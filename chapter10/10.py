# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org) and find
# a few texts you’d like to analyze. Download the text files for these works, or
# copy the raw text from your browser into a text file on your computer.
#   You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# 3
# >>> line.lower().count('row')
#   Notice that converting the string to lowercase using lower() catches all
# appearances of the word you’re looking for, regardless of how it’s formatted.
#   Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text. This will be
# an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the ', with a space in the string, and see how much lower your
# count is.

from pathlib import Path

n = Path('data/pg75976.txt').read_text().lower().count('the')
print(f'#(the)={n}')
