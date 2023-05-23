from models import Animal


class Fish(Animal):
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def voice_animal(self):
        print(f"{self.name} не издает звуки")
