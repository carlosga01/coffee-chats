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

def create_groups(num_groups, history):
    members = list(history.keys())
    random.shuffle(members)

    groups = [[] for i in range(num_groups)]    
    current_index = 0

    while True:
        current_member = members.pop(0)

        if current_index == num_groups:
            current_index = 0

        if have_history(current_member, groups[current_index], history):
            return (False, groups)
        else:
            groups[current_index].append(current_member)
            current_index += 1

        if len(members) == 0:
            return (True, groups)


def have_history(new, group, history):
    for member in group:
        if new in history[member] or member in history[new]:
            return True
    return False


while True:
    result = create_groups(4, history)

    if result[0] == True:
        print(result[1])
        break
