from random import randint

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

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battle_cry(self):
        return 'Odin Owns You All!'


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health = self.health - damage

        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'


# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, viking):
        self.viking_army.append(viking)

    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        viking_idx = randint(0, len(self.viking_army) - 1)
        saxon_idx = randint(0, len(self.saxon_army) - 1)
        
        res = self.saxon_army[saxon_idx].receive_damage(self.viking_army[viking_idx].strength)

        if self.saxon_army[saxon_idx].health <= 0:
            self.saxon_army.pop(saxon_idx)
        
        return res

    def saxon_attack(self):
        viking_idx = randint(0, len(self.viking_army) - 1)
        saxon_idx = randint(0, len(self.saxon_army) - 1)

        res = self.viking_army[viking_idx].receive_damage(self.saxon_army[saxon_idx].strength)

        if self.viking_army[viking_idx].health <= 0:
            self.viking_army.pop(viking_idx)

        return res

    def show_status(self):
        if len(self.saxon_army) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.viking_army) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
