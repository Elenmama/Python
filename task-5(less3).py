def q():
    a = 0
    o = False
    while True:
        o = False
        s = input("Введите числа, или введите * для выхода: ").split()
        for n in s:
            try:
                a += int(n if n != "*" else 0)
            except:
                    o = True
        if o:
            print("тут есть нежелелательные элементы!")
        print(a)
        if "*" in s:
            return
print(q())
