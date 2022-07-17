def maxsum(a, b, c):
    q = [a, b, c]
    q.pop(q.index(min(q)))
    return q[0] + q[1]


while True:
    try:
        e = list(map(int, input("Введите 3 числа: ").split()))
        if len(e) == 3:
            print(maxsum(e[0], e[1], e[2]))
            break
        else:
            print("это больше 3-х чисел!" if len(e) > 3 else "это меньше 3-х чисел!")
    except:
        print("это не числа!")
