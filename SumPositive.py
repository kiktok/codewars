def positive_sum(arr):
    s = 0

    for i, x in enumerate(arr):
        s += arr[i] if arr[i] > 0 else 0
        print(i, x)
    return s


print(positive_sum([1, 2, -2, 3, 4, 5, -9, -10]))
#print(positive_sum([-2, -5, -6]))
