def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
    # if numbers == []:
    #     return 0
    # else:


    # another way
    # s = 0
    # a = 0
    # for i, v in enumerate(numbers):
    # # for i in range(len(numbers)):
    #     s += numbers[i]
    #     a = s / len(numbers)
    # return a

print(find_average([1,2,3]))
