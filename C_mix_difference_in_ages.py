def difference_in_ages(members):
    max = members[0]
    min = members[0]

    for i, v in enumerate(members):
        if members[i] > max:
            max = members[i]
        elif members[i] < min:
            min = members[i]

        # if s > members[i] and l <= members[i]:
        #     l = members[i]
        #
        # else:
        #     s = members[i]
    print(min, max, max-min)


difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88])
