# 3-10. Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.

languages = ["Chinese", "English", "Cantonese"]

print(languages)
print(len(languages))
print(sorted(languages))

languages.reverse()
print(languages)

languages.sort(reverse=True)
print(languages)
