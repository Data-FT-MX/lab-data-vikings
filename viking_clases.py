import random



#---------------- Soldier ----------------------------#

class Soldier:
    def __init__(self, health, strength):
        '''Caracteristicas del Guerrero'''
        self.health = health
        self.strength = strength

    def attack(self):
        '''Accioón de ataque, devuelve la fuerza del Guerrero'''
        return self.strength
        
    def receive_damage(self, damage):
        '''Vida del guerrero luego de recibir daño'''
        #self.health -= damage
        self.health = self.health - damage
    

#--------------------- Viking ------------------------#

class Viking(Soldier):
    def __init__(self, name, health, strength):
        '''caracteristicas del vikingo, recibe 3 arg, nombre, vida y fuerza'''
        self.name = name 
        self.health = health
        self.strength = strength
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()

    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0 : 
            return f'{self.name} has received {damage} points of damage'
        else: 
            return f'{self.name} has died in act of combat'
    
    def battle_cry(self):
        return 'Odin Owns You All!'
        

#---------------------------- Saxon -------------------------


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        '''Saxon is still alive'''
        if self.health > 0 : 
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat' 

        


# War


class War:
    
    #Atributos
    def __init__(self):
        self.Viking_army = []
        self.Saxon_army = []

    #Metodos 
    
    def add_viking(self, Viking):
        self.Viking_army.append(Viking)
    
    def add_saxon(self, Saxon): 
        self.Saxon_army.append(Saxon)
    
    def viking_attack(self): 
        pass
        
        




