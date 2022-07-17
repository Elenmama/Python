def my_func(x, y):
    if x > 0 and y < 0:
        ans = 1
        for i in range(abs(y)):
            ans *= x
        return 1/ans
    else:
        return False
s = ""
while True:
    try:
        s = list(map(int, input("Введите два числа, первое из которых действительное положительное число, а второе из которых целое отрицательное число: ").split()))
        if len(s) != 2:
            print("это больше двух чисел!" if len(s) > 2 else "это меньше двух чисел!")
        else:
            if my_func(s[0], s[1]) == False:
                print("эти числа не соответствуют условиям!")
            else:
                print(my_func(s[0], s[1]))
                break
    except:
        print("это не числа!")
