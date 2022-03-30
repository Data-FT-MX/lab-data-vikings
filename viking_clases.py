# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > damage:
            return print("{0} has received {1} points of damage".format(
                self.name, 
                self.damage))
        else:
            return print("{0} has died in act of combat".format(
                self.name))

    def battle_cry(self):
            return ("Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > damage:
            return print("{0} has received {1} points of damage".format(
                self.name, 
                self.damage))
        else:
            return print("{0} has died in act of combat".format(
                self.name))

# War


class War:
    
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []
    
    def add_viking(self, Viking):
        __init__.viking_army.append(Viking)
    
    def add_saxon(self, Viking):
        __init__.saxon_army.append(Viking)
    
    def viking_attach():
        pass
    
    def saxon_attack():
        pass
    
    def show_status():
        pass
    