import random

history = {
    "Adam": ["Carlos", "Tae"],
    "Victor": ["Evan", "Joseph", "McKensey"],
    "Aastha": ["Cristina", "Kyle"],
    "Hau": ["Nick", "Wendy"],
    "McKensey": ["Joseph", "Victor", "Evan"],
    "Cristina": ["Aastha", "Kyle"],
    "Joseph": ["Evan", "Victor", "McKensey"],
    "Tae": ["Carlos", "Adam"],
    "Wendy": ["Nick", "Hau"],
    "Kyle": ["Cristina", "Aastha"],
    "Carlos": ["Adam", "Tae"],
    "Nick": ["Wendy", "Hau"],
    "Evan": ["Victor", "Jospeh", "McKensey"],
    "Ethan": []
}

members = list(history.keys())

while True:
    success = False;
    random.shuffle(members)

    pairs = []

    for i in range(0, int(len(members)) - 2, 3):
        member_1 = members[i]
        member_2 = members[i + 1]
        member_3 = members[i + 2]

        if member_1 in history[member_2] or member_1 in history[member_3] or member_2 in history[member_3]:
            success = False
            break
        else:
            pairs.append([member_1, member_2, member_3])
            success = True

    if success:
        print(pairs)
        break
