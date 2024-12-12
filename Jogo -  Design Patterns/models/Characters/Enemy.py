from models import Character
import random

class Cleric(Character):
    
    def __init__(self, hp, damage, armor):
        super().__init__(self, hp, damage, armor)
        self.weapon = "Divine sunlight"

    def attack(self, target: Character):
        # Calcula o dano causado
        damage = (self.attack - target.armor)
        # Diminui a vida do personagem se o dano for > 0 e se o alvo tiver vida suficiente
        target.hp = target.hp - damage if not damage else target.hp if (target.hp - damage) > 0 else 0

        print(f'''
              Cleric burned {target.__name__} with {self.weapon}, dealing {damage} damage!\n
              Target life is {target.hp} now
              ''')
        
    def heal(self):
        # Se cura num intervalo inteiro de 3 a 10
        self.hp += random.randint(3,10)
        if self.hp > 100:
            self.hp = 100

        print(f'Cleric asked for divine help and healed to {self.hp} hp!')

    def special(self):
        self.hp += random.randint(20, 30)
        if self.hp > 100:
            self.hp = 100
        
        print(f'Cleric achieved her godess greatest interest, and healed an extreme amount of hp, reaching to {self.hp}!')