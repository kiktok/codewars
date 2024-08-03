global f


def maskify(cc):
    global f
    if len(cc) == 0:
        return ''
    if len(cc) <= 3:
        return cc
    else:
        full = []
        l4 = cc[-4:]
        for i in cc[:-4]:
            full.append(i.replace(i, "#"))

            f = ''.join(full)
        return f + l4


print(maskify('1234567890'))
