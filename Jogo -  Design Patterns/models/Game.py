from models import Character, Weapon, Enemy, Player, Wizard, Cleric
from models.Characters import Knight

class Game():
    def __init__(self, characters: Player, enemy: Enemy, rounds):
        self.characters = characters
        self.enemy = enemy
        self.rounds = rounds

    def menu_game(self, character: Character):
        print(f"""
            === STATUS ===
            Health: {character.hp}
            Mana: {character.mana}
            Armor: {character.armor}
            ================
        """)
        print("=== MENU ===")
        print("1. Attack")
        print("2. Heal")
        print("3. Use Special")
        choice = input("Choose your action: ")
        
        if choice == "1":
            character.attack(self.enemy)
        
        elif choice == "2":
            character.heal()
        
        elif choice == "3":
            character.special()
        
        else:
            print("\nInvalid choice. Please try again.")


    def play(self):
        for character in self.characters:
            menu_game(character)