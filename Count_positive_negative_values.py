def count_positives_sum_negatives(arr):
    p = 0
    n = 0

    if arr == 0 or arr == []:
        return []
    else:
        for i, v in enumerate(arr):
            p += 1 if arr[i] > 0 else 0
            n += arr[i] if arr[i] < 0 else 0
    return [p, n]


print(count_positives_sum_negatives([1,2,-3,3,-1]))
# print(count_positives_sum_negatives([]))
# p += 1 if arr[i] > 0 else 0
# n += arr[i] if arr[i] < 0 else 0
