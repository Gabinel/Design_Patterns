from models.Characters import Character, Weapon
import random

class Wizard(Character):
    
    def __init__(self, hp: int, damage: int, armor: int, weapon: Weapon):
        super().__init__(self, hp, damage, armor)
        self.weapon = weapon
        self.weaponName = 'Fire Ball'

    def attack(self, target: Character) -> str:
        # Calcula o dano causado
        damagePoints = (self.damage - target.armor)

        self.weapon.attack(damagePoints, target)

        return f'''
              Wizard cast a spell on {target.__name__} with {self.weaponName}, dealing {damagePoints} damage!\n
              Target life is {target.hp} now.
              '''
        
    def heal(self) -> str:
        # Se cura num intervalo inteiro de 3 a 10
        self.hp += random.randint(3,10)
        if self.hp > 100:
            self.hp = 100

        return f'The Wizard recalls his knowledges in search of a healing spell, and successfully heals to {self.hp} hp!'

    def special(self, target: Character) -> str:
        if self.mana == 100:
            damagePoints = 30

            self.weapon.attack(damagePoints, target)
            return f'The Wizard communes with the higher planes, and summons a giant Fire Ball, that causes enormous {damagePoints} damage!'
        else:
            return f'Not enough mana! You got only {self.mana} points'