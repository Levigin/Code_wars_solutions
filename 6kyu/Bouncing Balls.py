def bouncing_ball(h, bounce, window):
    if 1 < bounce < 0 or window > h / 2 or h < 0:
        return -1

    counter = 0
    flag = True
    while flag:
        counter += 1
        h *= bounce
        if h <= window:
            flag = False
        else:
            counter += 1

    return counter


print(bouncing_ball(2, 0.5, 1))
