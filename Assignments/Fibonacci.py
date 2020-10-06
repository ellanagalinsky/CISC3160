def num(max):
    x, y = 0, 1

    while x < max:
        yield x
        x, y = y, x + y
print(sum(lambda n: % 2 == 0, num(4000000)))