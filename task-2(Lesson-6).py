class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def full_mass(self, weight=25, tolshina=5): 
        return f"{self.length} м * {self.width} м * {weight} кг * {tolshina} см = {int((self.length * self.width *weight * tolshina) / 1000)} т" 

r = Road(20, 5000)
print(r.full_mass())
