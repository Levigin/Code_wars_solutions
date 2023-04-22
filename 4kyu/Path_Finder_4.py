steps = [0, 0, 2]


def i_am_here(path):
    newp = get_path(path)
    print(newp)
    for i in newp:
        if i == 'l':
            steps[2] = (steps[2] - 1) % 4
        elif i == 'r':
            steps[2] = (steps[2] + 1) % 4
        elif i == 'L':
            steps[2] = (steps[2] - 2) % 4
        elif i == 'R':
            steps[2] = (steps[2] + 2) % 4
        else:
            if steps[2] == 1:
                steps[1] -= i
            elif steps[2] == 2:
                steps[0] -= i
            elif steps[2] == 3:
                steps[1] += i
            elif steps[2] == 0:
                steps[0] += i
    return steps[:2]


def get_path(path):
    l = []
    i = 0
    j = 0

    while i < len(path):
        if path[i].isdigit():
            while j < len(path) and path[j].isdigit():
                j += 1
            l.append(int(path[i: j]))
            i = j
        else:
            l.append(path[i])
            i += 1
            j = i
    return l
