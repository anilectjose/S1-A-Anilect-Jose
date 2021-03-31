def find(word):
    wl = []
    for n in word:
        wl.append((len(n), n))
    wl.sort()
    result = wl[-1][0], wl[-1][1]
    print("longest word: ", result[1])
    print("length of the longest word: ", result[0])


find(["hello", "I is going", "hi all welcomes you"])

# longest word:  hi all welcomes you
# length of the longest word:  19
