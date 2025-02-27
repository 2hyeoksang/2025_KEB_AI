class Pokemon:
    def __init__(self, name):
        self.name = name

    def walks(self):
        print("walking..")

    def attack(self, target):
        print(f"{self.name} attack {target.name}!")


class Pikachu(Pokemon):
    pass

class Agumon:
    def __init__(self, name):
        self.name = name

agumon = Agumon('아구몬')
pikachu = Pikachu('피카츄')
pikachu.attack(agumon)