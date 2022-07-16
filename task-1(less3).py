def dividing(a, b):
    if b == 0:
        return False
    else:
        return a / b
s = 0
while True:
    try:
        s = list(map(float, input("Введите два числа: ").split()))
        if dividing(s[0], s[1]):
            print(dividing(s[0], s[1]))
            break
        else:
            print("Нельзя делить на ноль!")
    except:
        print("это не числа!")
