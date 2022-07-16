def int_func2(a):
    b = ""
    for i in range(len(a.split())):
        b += a.split()[i][0].upper() + a.split()[i][1:] + " "
    return b
print(int_func2(input()))
