import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        print(random.choice(my_list))

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        print(total_damage)
        return total_damage  

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        print(total_block)
        return total_block

    def take_damage(self, damage):
        total_blocked = self.defend()
        actual_damage = max(damage - total_blocked, 0)
        self.current_health -= actual_damage
        if self.current_health < 0:
            self.current_health = 0
        print(self.current_health)
        return actual_damage

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    


    
if __name__ == "__main__":
    my_hero = Hero("Cyclops", 150)
    # print(my_hero.name)
    # print(my_hero.current_health) 
    # my_opponent = Hero("Spider-Man", 200)
    # my_hero.battle(my_opponent)
    # my_hero.add_ability(Ability("Laser Shooter Eyes", 20))
    # my_hero.add_ability(Ability("Punch Dimension", 15))
    # my_hero.add_ability(Ability("Psionic Wave", 45))
    # my_hero.attack()
    my_hero.add_armor(Armor("Expensive Glasses", 30))
    my_hero.add_armor(Armor("Yellow and Blue Suit", 30))
    my_hero.add_armor(Armor("Boots", 10))
    # my_hero.defend()
    my_hero.take_damage(20)
