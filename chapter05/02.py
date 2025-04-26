# 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

# Tests for equality and inequality with strings
EXPECT = "hello world"
print(EXPECT == "hello", EXPECT == "hello world")

# Tests using the lower() method
EXPECT = "HELLO WORLD"
print(EXPECT.lower() == "hello world", EXPECT.lower() == "HELLO WORLD")

# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
v = 5
print(v==5,v==6)
print(v!=5,v!=6)
print(v>4,v>6)
print(v<4,v<6)
print(v>=4,v>=6)
print(v<=4,v<=6)

# Tests using the and keyword and the or keyword
EXPECT = "apple"
print(EXPECT == "apple" and len(EXPECT)>1, EXPECT == "orange" and len(EXPECT)>1)
print(EXPECT == "apple" or len(EXPECT)>1, EXPECT == "orange" or len(EXPECT)>1)

# Test whether an item is in a list
EXPECT = ["apple","orange"]
print("apple" in EXPECT, "grape" in EXPECT)

# Test whether an item is not in a list
EXPECT = ["apple","orange"]
print(not "apple" in EXPECT, not "grape" in EXPECT)
