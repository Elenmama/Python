from itertools import count, cycle


def gen(a):
    for i in count(a):
        if i == a + 10:
            break
        yield i


for i in gen(int(input())):
    print(i)


def gen2(a):
    coun = 0
    for i in cycle(list(a)):
        if coun == 25:
            break
        yield i
        coun += 1


for i in gen2(input().split()):
    print(i)
