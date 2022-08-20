from time import sleep as s


class TrafficLight:
    __colour = ["\033[41m   \033[0m", "\033[43m   \033[0m", "\033[42m   \033[0m", "\033[40m   \033[0m"]

    def run(self):
        while True:
            print("\r(" + self.__colour[0] + ")" + "(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")", end='')
            s(7)
            print("\r(" + self.__colour[0] + ")" + "(" + self.__colour[1] + ")" + "(" + self.__colour[3] + ")", end='')
            s(2)
            print("\r(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")" + "(" + self.__colour[2] + ")", end='')
            s(7)
            print("\r(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")", end='')
            s(0.5)
            print("\r(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")" + "(" + self.__colour[2] + ")", end='')
            s(0.5)
            print("\r(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")", end='')
            s(0.5)
            print("\r(" + self.__colour[3] + ")" + "(" + self.__colour[3] + ")" + "(" + self.__colour[2] + ")", end='')
            s(0.5)
            print("\r(" + self.__colour[3] + ")" + "(" + self.__colour[1] + ")" + "(" + self.__colour[3] + ")", end='')
            s(2)

t = TrafficLight()
t.run()
