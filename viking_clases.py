# Soldier
class Soldier:
    def __init__(self, health, strength):
        # add code here
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def receive_damage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return(self.name + " received "+ str(damage)+" points of damage")
        else:
            return(self.name + " has died in act of combat")

    
    def battle_cry(self):
        return("Odin Owns You All!")
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)


    def receive_damage(self,damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return("A Saxon has received "+ str(damage)+" points of damage")
        else:
            return("A Saxon has died in combat")

