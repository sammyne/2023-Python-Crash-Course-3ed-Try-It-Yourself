# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist,title,nsongs=None):
    out = {
        'artist': artist.title(),
        'title': title.title(),
    }

    if nsongs:
        out['#(song)'] = nsongs

    return out

while True:
    print("\nEnter album's info. Enter 'q' if you don't want to enter anymore.")
    artist = input("Enter artist's name. ")
    if artist=='q':
        break

    title = input("Enter title. ")
    if title=='q':
        break

    album = make_album(artist,title)
    print(f'You have made {album}')
