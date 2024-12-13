from models.Characters.Character import Character

class Weapon():

    def attack(self, damage: int, target: Character):
        # Diminui a vida do personagem se o dano for > 0 e se o alvo tiver vida suficiente
        target.hp = target.hp - damage if damage else target.hp if (target.hp - damage) > 0 else 0