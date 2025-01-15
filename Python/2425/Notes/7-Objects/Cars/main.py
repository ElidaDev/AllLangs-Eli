import car
import sys
sys.path.insert(0,'../')
from ..Player.player import Player

murica = car.Car("America","Tank","2048","Pure Gold")
truck = car.Car("Very","Fast","2248","Pure Gold")
poor = car.Car("Lamborghini","Aventador","2077","Pure Gold")
tacoTruck= car.Car("Taco","Truck","0001","Neon Pink")

myCharacter = Player.player(20,2,51,"Test")

print(myCharacter.stats())
print(murica.description())
print(truck.description())
print(poor.description())
print(tacoTruck.description())