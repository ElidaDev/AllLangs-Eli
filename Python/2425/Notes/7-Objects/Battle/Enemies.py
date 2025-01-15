class Sith:
    def __init__(self, name="Sith Acolyte"):
        self.name = name
        self.health = 70
        self.attack = 18
        self.defense = 5
    def takeDamage(self, damage):
        damageTaken = max(damage - self.defense, 0)
        self.health -= damageTaken
        return damageTaken
    def isAlive(self):
        return self.health > 0
    
class Empire:
    def __init__(self, name="Imperial Officer"):
        self.name = name
        self.health = 60
        self.attack = 12
        self.defense = 3
    def takeDamage(self, damage):
        damageTaken = max(damage - self.defense, 0)
        self.health -= damageTaken
        return damageTaken
    def isAlive(self):
        return self.health > 0






