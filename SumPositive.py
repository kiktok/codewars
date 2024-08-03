def positive_sum(arr):
    s = 0
    i = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            s += arr[i]
        else:
            i += 1

    # arr[i] > 0
    return s


print(positive_sum([1, 2, -2, 3, 4, 5, -9]))
#print(positive_sum([-2, -5, -6]))
