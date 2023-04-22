def pick_peaks(arr):
    pic_list = []
    index_list = []
    # for i in range(1, len(arr) - 1):
    #     if arr[i - 1] <= arr[i] > arr[i + 1]:
    #         index_list.append(i)
    #         pic_list.append(arr[i])
    #     elif arr[i - 1] < arr[i] >= arr[i + 1]:
    #         index_list.append(i)
    #         pic_list.append(arr[i])

    count = 0
    for i in range(1, len(arr) - 1):
        if arr[count] >= arr[i]:
            count = i
        else:
            if arr[count] < arr[i] < arr[i] and i - count == 1:
                index_list.append(i)
                pic_list.append(arr[i])

    return index_list, pic_list


print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))


