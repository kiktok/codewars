def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()

    arr3 = []
    for i in arr1:
        if i not in arr3:
            arr3.append(i)

    return arr3

print(merge_arrays([-100, -34, -27, -27, -8, 5, 5, 6, 12, 23, 25, 56, 56, 124, 213, 325, 325, 601], []))