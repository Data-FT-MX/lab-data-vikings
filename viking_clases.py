# Soldier
import random

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
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self,viking):
        self.viking_army.append(viking)
    
    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        random_saxon = random.choice(self.saxon_army)
        random_viking = random.choice(self.viking_army)
  
        saxon_status = random_saxon.receive_damage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxon_army = [saxon for saxon in self.saxon_army if saxon not in self.saxon_army]
        return saxon_status
    
    def saxon_attack(self):
        random_saxon = random.choice(self.saxon_army)
        random_viking = random.choice(self.viking_army)

        viking_status = random_viking.receive_damage(random_saxon.strength)
        if random_viking.health <=0:
            self.viking_army = [viking for viking in self.viking_army if viking not in self.viking_army]
        return viking_status

    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        
        if len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        if len(self.viking_army) == 1 and len(self.saxon_army) == 1:
            return "Vikings and Saxons are still in the thick of battle."