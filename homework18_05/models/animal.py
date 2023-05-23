#import sys
import random
#sys.stdin.reconfigure(encoding='utf-8')
#sys.stdout.reconfigure(encoding='utf-8')
from abc import ABC, abstractmethod
import time
import functools


def benchmark(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        return_value = func(*args,**kwargs)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end-start))
    return wrapper

def func_writting (func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
       result = func(*args,**kwargs)
       with open("homework18_05/data/function_result.txt", "a") as file:
              file.write(f"{func.__name__}: {result}\n")
       return result     
    return wrapper

''' An abstract class that describes the properties and behavior of animals'''

class Animal(ABC):
    def __init__(self, name:str, age:int, voice:str, food:str, weight:int,speed_factor = 0.5)->None: 
        self.__name = name
        self.__age = age
        self.voice = voice
        self.food = food
        self.weight = weight
        self.__tail = random.randint(0,10)
        self.speed_factor = speed_factor

    @property
    def get_name(self)->None:
        return f"{self.__name}"
    
    @property
    def get_age(self)->None:
        return f"Возраст: {self.__age}"
    
    @get_age.setter
    def name(self, value:int)->None:
        if 0 < int(value) < 50:
            self.__age = value
        else:
            print("Недопустимый возраст")
    
    @abstractmethod
    def calculate_speed(self):
        pass
    @abstractmethod
    def move(self):
        pass 

    @abstractmethod
    def description(self):
        pass

    def display_info(self)->None:
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")

    
    def voice_animal(self)->None:
        print (f"{self.__name} издает звук {self.voice}")

    def animal_eating(self)->None:
        print(f"{self.__name} каждый день ест {self.food}")


    def get_tail_info(self)->None:
        print (f"Длина хвоста {self.__tail} см")   

    
               
    
    

   
    
        