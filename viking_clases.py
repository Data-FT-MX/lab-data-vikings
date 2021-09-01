
import random   

################################

class Soldier():
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health-=damage

################################

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0    : return "{} has received {} points of damage".format(self.name, damage)
        elif self.health<=0 : return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"



################################


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0    : return "A Saxon has received {} points of damage".format(damage)
        elif self.health<=0 : return "A Saxon has died in combat"



################################



class War():
    def __init__(self):
        self.viking_army=[]
        self.saxon_army=[]

    def addViking(self, Viking):
        self.viking_army.append(Viking)

    def addSaxon(self, Saxon):
        self.saxon_army.append(Saxon)

    def vikingAttack(self):
        Sax=random.choice(self.saxon_army)
        Vik=random.choice(self.viking_army)
        sax_life=Sax.receiveDamage(Vik.strength)
        if Sax.health<=0: self.saxon_army.remove(Sax)
        return sax_life

    def saxonAttack(self):
        Vik=random.choice(self.viking_army)
        Sax=random.choice(self.saxon_army)
        vik_life=Vik.receiveDamage(Sax.strength)
        if Vik.health<=0: self.viking_army.remove(Vik)
        return vik_life

    def showStatus(self):
        if self.viking_army==[]: return "Saxons have fought for their lives and survive another day..."
        if self.saxon_army==[] : return "Vikings have won the war of the century!"
        if self.viking_army!=[] and self.saxon_army!=[] : return "Vikings and Saxons are still in the thick of battle."



