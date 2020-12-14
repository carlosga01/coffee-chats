import random

history = {
    "Adam": ["Victor", "Aastha", "Juan", "Joseph"],
    "Victor": ["Aastha", "Adam", "Hau", "Kyle"],
    "Aastha": ["Adam", "Victor", "Evan", "McKensey"],
    "Hau": ["Matthew", "McKensey", "Kyle", "Victor"],
    "Matthew": ["Hau", "McKensey", "Tae", "Wendy"],
    "McKensey": ["Hau", "Matthew", "Evan", "Aastha"],
    "Cristina": ["Joseph", "Tae", "Carlos", "Nick"],
    "Joseph": ["Cristina", "Tae", "Juan", "Adam"],
    "Tae": ["Cristina", "Joseph", "Wendy", "Matthew"],
    "Wendy": ["Kyle", "Carlos", "Tae", "Matthew"],
    "Kyle": ["Carlos", "Wendy", "Victor", "Hau"],
    "Carlos": ["Wendy", "Kyle", "Cristina", "Nick"],
    "Nick": ["Juan", "Evan", "Carlos", "Cristina"],
    "Juan": ["Nick", "Evan", "Adam", "Joseph"],
    "Evan": ["Nick", "Juan", "Aastha", "McKensey"]
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
