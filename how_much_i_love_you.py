def how_much_i_love_you(nb_petals):
    petal = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']

    p = nb_petals % len(petal)  # 0,1,2,3,4,5
    if p == 0:
        p = len(petal)

    for i, v in enumerate(petal, 1):  # 1,2,3,4,5,6
        if p == i:
            return i, v

