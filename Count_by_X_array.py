global s

def count_by(x, n):
    s = []
    for i in range(1, n + 1):
         s.append(i * x)
    return s

# best
# def cb(x, n):
#     return [i * x for i in range(1, n+1)]

print(count_by(4, 5))