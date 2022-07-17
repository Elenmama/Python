def fact(a):
    ind = 1
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            ind *= j
        yield ind
        ind = 1


a = [i for i in fact(int(input()))]
print(a)
