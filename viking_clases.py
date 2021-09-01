import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
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
        self.health -= damage
        
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        elif self.health <= 0:
            return f'{self.name} has died in act of combat'
            
    def battle_cry(self):
        return f'Odin Owns You All!'
 

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receive_damage(self, damage):
        self.health -= damage
        
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        elif self.health <= 0:
            return f'A Saxon has died in combat'
        
# War
class War():

    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    
    def add_viking(self, viking):
        self.viking_army.append(viking)
        
    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)
        
    def viking_attack(self):
        vik = random.choice(self.viking_army)
        sax = random.choice(self.saxon_army)
        
        x = sax.receive_damage(vik.strength)
        if sax.health <= 0:
            self.saxon_army.remove(sax) 
        return x

    def saxon_attack(self):
        vik = random.choice(self.viking_army)
        sax = random.choice(self.saxon_army)
        
        x = vik.receive_damage(sax.strength)
        if vik.health <= 0:
            self.viking_army.remove(vik)
        return x
    
    def show_status(self):
        if len(self.saxon_army) == 0:
            return f'Vikings have won the war of the century!'
        elif len(self.viking_army) == 0:
            return f'Saxons have fought for their lives and survive another day...'
        elif len(self.viking_army) > 0 and len(self.saxon_army) > 0:
            return f'Vikings and Saxons are still in the thick of battle.'