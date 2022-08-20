from random import choice


class Car:
    directions = ["запад", "восток", "юг", "север", "югозапад", "юговосток", "северовосток", "северозапад"]

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction=None):
        print(
            f"{self.name} повернула {direction}" if direction != None else f"{self.name} повернула {choice(self.directions)}")

    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} превышает скорость на {self.speed - 60} км/ч (лимит 60 км/ч)")
        else:
            print(f"{self.name} машины {self.speed} км/ч")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} превышает скорость на {self.speed - 40} км/ч (лимит 40 км/ч)")
        else:
            print(f"{self.name} машины {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


t = TownCar(60, "black", "mazda")
t.go()
t.stop()
t.turn("направо")
t.show_speed()
t = TownCar(63, "black", "mazda")
t.go()
t.stop()
t.turn("направо")
t.show_speed()

w = WorkCar(40, "red", "w3zm")
w.go()
w.stop()
w.turn("налево")
w.show_speed()
w = WorkCar(45, "red", "w3zm")
w.go()
w.stop()
w.turn("налево")
w.show_speed()

e = SportCar(200, "red", "Formula 1")
e.go()
e.stop()
e.turn("направо")
e.show_speed()

r = PoliceCar(150, "blue", "POl")
r.go()
r.stop()
r.turn("направо")
r.show_speed()
