from models import Animal
import time
from models.animal import benchmark,func_writting

'''Sub-class of the Animal class. Describes the property and behavior of cats. '''

class Cat(Animal):
      
      def __init__(self, name, age, voice, food, weight,color):
        super().__init__(name, age, voice, food, weight)
        self.color = color

      def animal_color(self)->None:
        print(f"{self.get_name} имеет цвет {self.color}")

     
      def calculate_speed(self)->int:
        speed_func = lambda x: x*self.speed_factor
        return speed_func(self.weight)
        
      def description(self)->None:
        print( f"Это кошка. {self.get_name} развивает скорость {self.calculate_speed()} \nПараметры: {vars(self)}\n")
       
      @benchmark
      @func_writting
      def move(self):
        time.sleep(1)
        print(f"{self.get_name} развивает скорость {self.calculate_speed()}")
        return self.calculate_speed()
      
      def children_animal(self, other):
        if (isinstance(self, Cat) and isinstance(other, Cat)):
          children_name = self.get_name + other.get_name
          children_color = self.color + other.color
          children_age = 1
          children_voice = "myrrr"
          children_food = "milk"
          children_weight = 8
          return Cat(children_name, children_age, children_voice, children_food, children_weight, children_color)
        else:
           print("Breeding is impossible different classes")
      