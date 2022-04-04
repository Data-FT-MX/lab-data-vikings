import random
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
    
    
    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health= self.health-damage


# Viking
class Viking(Soldier):
    
    def __init__(self,name, health ,strength):
        self.name= name
        super().__init__(health, strength)
    
    def receive_damage(self, damage):
        self.health= self.health-damage
        if self.health>0:
            return "{0} has received {1} points of damage".format(self.name, damage)
        else:
            return "{0} has died in act of combat".format(self.name)
       
    def battle_cry(self):
        return  "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health, strength)
    
    def receive_damage(self, damage):
        self.health= self.health - damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War
class War:
    
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
        
    def add_viking(self,i):
        self.viking_army.append(i)
    
    def add_saxon(self, i):
        self.saxon_army.append(i)
    
        
    def viking_attack(self):
        self.ran_sol_sax=random.choice(self.saxon_army)
        self.ran_sol_sax.receive_damage(random.choice(self.viking_army).strength)
        if self.ran_sol_sax.health<=0:
            self.saxon_army.remove(self.ran_sol_sax)
            return self.ran_sol_sax.receive_damage(random.choice(self.viking_army).strength)
        else:
            return self.ran_sol_sax.receive_damage(random.choice(self.viking_army).strength)
    
    def saxon_attack(self):
        self.ran_sol_vik=random.choice(self.viking_army)
        self.ran_sol_vik.receive_damage(random.choice(self.saxon_army).strength)
        if self.ran_sol_vik.health<=0:
            self.viking_army.remove(self.ran_sol_vik)
            return self.ran_sol_vik.receive_damage(random.choice(self.saxon_army).strength)
        else:
            return self.ran_sol_vik.receive_damage(random.choice(self.saxon_army).strength)
        
    def show_status(self):
        if len(self.saxon_army)==0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


    