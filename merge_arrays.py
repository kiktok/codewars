def merge_arrays(arr1, arr2):
    for i in range(len(arr1)):
        print(arr1[i], end =" ")

    arr1.extend(arr2)
    print("\n")
    arr1.sort()

    for i in range(len(arr1)):
        count = arr1.count(arr1[i])

        print(arr1[i], end=" ")


merge_arrays([1,3,5,7,9], [10,8,6,4,2])