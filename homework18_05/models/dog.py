from models import Animal
import time
from models.animal import benchmark,func_writting

'''Sub-class of the Animal class. Describes the property and behavior of dogs. '''
 
class Dog(Animal):

    def __init__(self, name, age, voice, food, weight, color, house="Будке"):
        super().__init__(name, age, voice, food, weight)
        self.color = color
        self.house = house

    def animal_color(self)->None:
        print(f"{self.name} имеет цвет {self.color}")

    def animal_house(self)->None:
        print(f"{self.name} живет в {self.house}")

    def description(self)->None:
        print (f"Это собака. {self.get_name} развивает скорость {self.calculate_speed()} \nПараметры: {vars(self)}")
        
    def calculate_speed(self)->float:
        speed_func = lambda x: x*self.speed_factor
        return speed_func(self.weight)

    @benchmark
    @func_writting
    def move(self)->float:
        time.sleep(1)
        print(f"{self.get_name} развивает скорость {self.calculate_speed()}")
        return self.calculate_speed()
    
    def children_animal(self, other):
        if (isinstance(self, Dog) and isinstance(self, Dog)):
            children_name = self.get_name + other.get_name
            children_color = self.color + other.color
            children_age = 1
            children_voice = "rrrrr"
            children_food = "milk"
            children_weight = 13
            return Dog(children_name, children_age, children_voice, children_food, children_weight, children_color)
        else:
            print("Breeding is impossible different classes")