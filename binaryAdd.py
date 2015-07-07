def add(a, b):
    c = (len(a) + 1) * [None]
    i = len(a) - 1
    r = 0
    while(i >= 0):
        c[i+1] = (a[i] + b[i] + r) % 2
        r = (a[i] + b[i] + r) / 2
        i -= 1
    c[0] = r
    return c

print(add([1,1], [1,1]))
