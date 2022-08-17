class Cell:
    def _init_(self, yacheiki):
        self.yacheiki = yacheiki

    def _add_(self, other):
        new_yacheiki = self.yacheiki + other.yacheiki
        self.yacheiki = 0
        other.yacheiki = 0
        return Cell(new_yacheiki)

    def _sub_(self, other):
        if self.yacheiki != other.yacheiki:
            if self.yacheiki > other.yacheiki:
                self.yacheiki -= other.yacheiki
            else:
                other.yacheiki -= self.yacheiki
        else:
            print("од. кол-во ячеек")

    def _mul_(self, other):
        new_yacheiki = self.yacheiki * other.yacheiki
        self.yacheiki = 0
        other.yacheiki = 0
        return Cell(new_yacheiki)

    def _truediv_(self, other):
        new_yacheiki = self.yacheiki // other.yacheiki
        self.yacheiki = 0
        other.yacheiki = 0
        return Cell(new_yacheiki)

    def make_order(self, rows):
        return "\n".join(['*' * rows for _ in range(self.yacheiki // rows)]) + str(
            "\n" + "*" * (self.yacheiki % rows) if self.yacheiki % rows > 0 else "")


q = Cell(12)
w = Cell(13)
s = q + w
print(s.yacheiki)
q = Cell(12)
w = Cell(13)
q - w
print(w.yacheiki)
q = Cell(12)
w = Cell(13)
f = w * q
print(f.yacheiki)
q = Cell(12)
w = Cell(13)
g = w / q
print(g.yacheiki)
q = Cell(12)
w = Cell(13)
print(q.make_order(5))
