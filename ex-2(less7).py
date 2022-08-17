class Clothes:
    def init(self, name, size):
        if name == "пальто":
            self.now = size
            self.is_palto = True
        elif name == "костюм":
            self.now = size
            self.is_palto = False
        else:
            print("×")

    @property
    def sizec(self):
        return self.now / 6.5 + 0.5 if self.is_palto else self.now * 2 + 0.3

    @sizec.setter
    def sizec(self, now):
        self.now = now


palto = Clothes("костюм", 65)
print(palto.sizec)
