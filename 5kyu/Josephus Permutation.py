def josephus(items, k):
    new_items = []
    counter = 0
    curr_k = k
    i = 0
    while items:
        if curr_k > len(items):
            curr_k = curr_k - len(items)
            while i < len(new_items):
                items.pop(i)
                i += 1
            counter = 0
        else:
            new_items.append(items[curr_k - 1])
            curr_k += k
            counter += 1

    return new_items


print(josephus([True, False, True, False, True, False, True, False, True], 9))


