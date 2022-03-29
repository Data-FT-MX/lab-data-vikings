#Soldier
class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    
##attack() method
    def attack(self):
        return self.strenght

#recive_damage method
    def receive_damage(self, damage):
        self.health -=damage

# Viking
class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name=name
        super().__init__(health,strength)

#recive_damage method
    def receive_damage(self, damage):
        if self.health >0
            print(self.name + " has recived {damage} points of damage")
        else:
            print(self.name + " has died in act of combat.")
        
        
#New Method battle_cry(self)
    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    super().__init__(health,strength)
        
#recive_damage method
    def receive_damage(self, damage):
        if self.health >0
            print(self.name + " has recived {damage} points of damage")
        else:
            print(self.name + " has died in act of combat.")

# War


#class War:
#pass
