from models.Characters import Character
import random

class Cleric(Character):
    
    def __init__(self, hp: int, damage: int, armor: int, mana: int):
        super().__init__(self, hp, damage, armor, mana)
        self.weapon = "Divine sunlight"

    def attack(self, target: Character) -> str:
        # Calcula o dano causado
        damagePoints = (self.damage - target.armor)
        # Diminui a vida do personagem se o dano for > 0 e se o alvo tiver vida suficiente
        target.hp = target.hp - damagePoints if not damagePoints else target.hp if (target.hp - damagePoints) > 0 else 0

        return f'''
              Cleric burned {target.__name__} with {self.weapon}, dealing {damagePoints} damage!\n
              Target life is {target.hp} now.
              '''
        
    def heal(self) -> str:
        # Se cura num intervalo inteiro de 5 a 10 (clérigo se cura mais)
        self.hp += random.randint(5,15)
        if self.hp > 100:
            self.hp = 100

        return f'Cleric asked for divine help and healed to {self.hp} hp!'

    def special(self, target=0) -> str:
        if self.mana == 100:
            # Especial do clérigo: se cura muito
            self.hp += random.randint(20, 30)
            if self.hp > 100:
                self.hp = 100
        
            return f'Cleric achieved her godess greatest interest, and healed an extreme amount of hp, reaching to {self.hp}!'
        else:
            return f'Not enough mana! You got only {self.mana} points'