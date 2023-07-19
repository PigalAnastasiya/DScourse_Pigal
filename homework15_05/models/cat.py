
from models import Animal


class Cat(Animal):
    def __init__(self, name, age, voice, food, color):
        super().__init__(name, age, voice, food)
        self.color = color

    def animal_color(self):
        print(f"{self.name} имеет цвет {self.color}")
