def smaller(arr):

    result_list = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                result_list[i] += 1

    return result_list


print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]))