from models import Animal


class Dog(Animal):

    def __init__(self, name, age, voice, food, color, house="Будке"):
        super().__init__(name, age, voice, food)
        self.color = color
        self.house = house

    def animal_color(self):
        print(f"{self.name} имеет цвет {self.color}")

    def animal_horse(self):
        print(f"{self.name} живет в {self.house}")
