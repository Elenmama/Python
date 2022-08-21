class ComplexNum:

    def __init__(self, vesh_num, mnim_num):
        self.vesh_num = vesh_num
        self.mnim_num = mnim_num

    def __add__(self, other):
        return ComplexNum(self.vesh_num + other.vesh_num, self.mnim_num + other.mnim_num)

    def __mul__(self, other):
        return ComplexNum((self.vesh_num * other.vesh_num - self.mnim_num * other.mnim_num),
                          (self.vesh_num * other.mnim_num + other.vesh_num * self.mnim_num))

    def __str__(self):
        return f"{self.vesh_num}, {self.mnim_num}"


q = ComplexNum(2, 3)
w = ComplexNum(2, 3)
a = q + w
print(a)
a = q * w
print(a)
