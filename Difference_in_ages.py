def difference_in_ages(members):
    a = max(members)
    b = min(members)

    return [b, a, a-b]


print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))