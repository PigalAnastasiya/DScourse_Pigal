import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

from models import Cat
from models import Dog
from models import Fish

cat_first = Cat("Jase", "5", " 'Mayy'", "fish","WHITE")
dog_first = Dog("Рекс", 15, " 'Гав'", "мясо","СЕРЫЙ")
fish_first = Fish("Гуппи", "личинок")

cat_first.animal_eating()
cat_first.animal_age()
cat_first.voice_animal()
cat_first.animal_color()

print(" ")

dog_first.animal_eating()
dog_first.animal_age()
dog_first.voice_animal()
dog_first.animal_color()
dog_first.animal_horse()

print(" ")

fish_first.animal_eating()
fish_first.voice_animal()
