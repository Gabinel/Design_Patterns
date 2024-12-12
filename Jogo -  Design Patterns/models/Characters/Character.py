# Classe abstrata que vai compor os personagens do jogo

class Character:

    def __init__(self, hp: int, damage: int, armor: int, mana: int):
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.mana = mana
    
    def attack(self, target):
        pass

    def heal(self):
        pass

    def special(self, target):
        pass