from models import Character

class Weapon():

    def __init__(self, character: Character):
        self.character = character

    def attack(damage: int, target: Character):
        # Diminui a vida do personagem se o dano for > 0 e se o alvo tiver vida suficiente
        target.hp = target.hp - damage if not damage else target.hp if (target.hp - damage) > 0 else 0

