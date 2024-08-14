def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()

    for i in range(len(arr1)):
        count = arr1.count(i)
        if count > 1:
            arr1.pop(arr1.index(i))
            count = 1
    # print(arr1, end =" ")
    return arr1

print(merge_arrays([-100, -34, -27, -27, -8, 5, 6, 12, 23, 25, 56, 56, 124, 213, 325, 325, 601], []))