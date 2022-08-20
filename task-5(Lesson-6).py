class Stationary:
    def __init__(self, title="something"):
        self.title = title

    def draw(self):
        print(f"starting draw {self.title}")


class Pen(Stationary):
    def draw(self):
        print(f"start drawing {self.title} with pen")

class Pencil(Stationary):
    def draw(self):
        print(f"start drawing {self.title} with pencil")

class Handle(Stationary):
    def draw(self):
        print(f"start drawing {self.title} with handle")

s = Stationary()
s1 = Stationary("(⓿_⓿)")
p = Pen()
p1 = Pen("🖊️")
r = Pencil()
r1 = Pencil("✏")
h = Handle()
h1 = Handle("0️⃣")
allq = [s, s1, p, p1, r, r1, h, h1]
for q in allq:
    q.draw()
