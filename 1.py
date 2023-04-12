'''
class Slime:
    def __init__(self, i, r, v, c):
        self.imya = i
        self.rost = r
        self.ves = v
        self.cvet = c
        
    def ispug(self, anotherSlime):
        if self.rost < anotherSlime.rost:
            return True
        else:
            return False

slime = Slime("Ыыы", 10, 20, "Зелёный")
slime2 = Slime("Чо", 20, 40, "Синий")


if slime2.ispug(slime):
    print("чоооо")
else:
    print("ыыы")
    
'''
tovari = ["", ""]

class NPS:
    def __init__(self, i, r, z, p, t, u)
        self.imya = i
        self.rost = r
        self.zdorovie = z
        self.professia = p
        self.spisokTovarov = t
        self.spisokUslug = u
        
        
    def Hi(self):
        print("Меня зовут" + self.name)
        
NPC1 = NPC("Чо", 20, 25, 1, )




