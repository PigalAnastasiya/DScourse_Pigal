import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
class Animal:
    def __init__(self, name, age, voice, food):
        self.name = name
        self.age = age
        self.voice = voice
        self.food = food
        

    def voice_animal(self):
         print (f"{self.name} издает звук {self.voice}")


    def animal_eating(self):
        print(f"{self.name} каждый день ест {self.food}")

    def animal_age(self):
        if int(self.age) >= 10:
            print(f"{self.name} пожилое животное, нуждается в особом уходе")
        elif int(self.age) >2 and int(self.age) <10:
            print(f"{self.name} половозрелое животное")
        else:
            print(f"{self.name} еще ребенок")
