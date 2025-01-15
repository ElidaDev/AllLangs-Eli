import random

class Wookie:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.rageMeter = 1
    
    def takeDamage(self,damage):
        damageTaken = max(damage-self.defense,0)
        self.health -= damageTaken
        return damageTaken

    def isAlive(self):
        return self.health > 0
        
    def rageAttack(self):
        self.rageMeter +=10
        return self.attack + self.rageMeter
    
class Droid:
    def __init__(self, name="Droid"):
        self.name = name
        self.health = 80
        self.attack = 15
        self.defense = 5
        self.energyReserve = 30
    def takeDamage(self, damage):
        damageTaken = max(damage - self.defense, 0)
        self.health -= damageTaken
        return damageTaken
    def isAlive(self):
        return self.health > 0
    def recharge(self):
        self.energyReserve = max(self.energyReserve - 10, 0)
        self.health += 10
        return 10
    
class RebelSoldier:
    def __init__(self, name="Rebel Soldier"):
        self.name = name
        self.health = 100
        self.attack = 12
        self.defense = 8
    def takeDamage(self, damage):
        damageTaken = max(damage - self.defense, 0)
        self.health -= damageTaken
        return damageTaken
    def isAlive(self):
        return self.health > 0
    def grenadeThrow(self):
        return random.randint(10, 25)






