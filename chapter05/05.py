# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
# else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

for alien_color in ["green", "yellow", "red"]:
    if alien_color == "green":
        print(f"You just earned 5 points for {alien_color}.")
    elif alien_color =="yellow":
        print(f"You just earned 10 points for {alien_color}.")
    else:
        print(f"You just earned 15 points for {alien_color}.")
