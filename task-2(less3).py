def inp(**kwargs):
    return " ".join(kwargs.values())
m1 = input("Введите ваше имя: ")
m2 = input("Введите вашу фамилию: ")
m3 = input("Введите ваш год рождения: ")
m4 = input("Введите ваш город проживания: ")
m5 = input("Введите ваш email: ")
m6 = input("Введите ваш телефон: ")
print(inp(a=m1, b=m2, c=m3, d=m4, e=m5, f=m6))
