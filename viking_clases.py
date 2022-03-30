import unittest
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
        if self.health <= 0:
            return("{0} has died in act of combat".format(
            self.name))
        else:
            return(("{0} has received {1} points of damage".format(
            self.name,
            damage)))
    
    def battle_cry(self):
        return("Odin Owns You All!")


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return("A Saxon has died in combat")
        else:
            return(("A Saxon has received {0} points of damage".format(
            damage)))


# War
class War:
    viking_army = []
    saxon_army = []
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
              
    def add_viking(self, Viking):
        self.viking_army.append(Viking)
        
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)
                       
    def viking_attack(self):
        random_saxon = random.choice(self.saxon_army)
        random_viking = random.choice(self.viking_army)
        
        saxon_status = random_saxon.receive_damage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxon_army = list(filter(lambda saxon: saxon if saxon not in self.saxon_army else False, self.saxon_army ))
        return saxon_status
        
    def saxon_attack(self):
        random_saxon = random.choice(self.saxon_army)
        random_viking = random.choice(self.viking_army)
        
        viking_status = random_viking.receive_damage(random_saxon.strength)
        if random_viking.health <= 0:
            self.viking_army = list(filter(lambda viking: viking if viking not in self.viking_army else False, self.viking_army))
        return viking_status
        
        
    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        
        if len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        if len(self.saxon_army) == 1 and len(self.viking_army) == 1:
            return "Vikings and Saxons are still in the thick of battle."
        
    

