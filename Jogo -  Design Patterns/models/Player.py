from models.Characters import Character

# Classe composite (contém os personagens do jogo)
class Player(Character):

    def __init__(self):
        self.party = []
    
    # Todos os personagens da party atacam
    def attack(self, target: Character):
        for character in self.party:
            character.attack(target)

    # Todos os personagens se curam
    def heal(self):
        for character in self.party:
            character.heal()

    # Todos usam o poder especial
    def special(self, target: Character):
        for character in self.party:
            character.special(target)

    # -- Métodos de acesso da lista --
    # Adiciona um personagem à party
    def add(self, character: Character):
        self.party.append(character)

    # Remove um personagem da party
    def remove(self, character: Character):
        self.party.remove(character)