class Division(Exception):

    def _init_(self, msg):
        self.msg = msg


try:
    q = int(input("введите делимое>"))
    w = int(input("введите делитель>"))
    try:
        int(q) / int(w)
    except ZeroDivisionError:
        raise Division("division by zero")
except ValueError:
    print("Вы ввели не число")
except Division as err:
    print(err)
