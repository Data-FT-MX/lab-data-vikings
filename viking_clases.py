# Soldier
class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health -=  damage

# Viking


class Viking(Soldier):
    def __init__(self, name,health, strength):
        self.name = name
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health -=  damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon



class Saxon(Soldier):
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        # super().__init__(health, strength)
    def receive_damage(self, damage):
        self.health -=  damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
# War


class War:
    pass
