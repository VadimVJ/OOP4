from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука"

class Fighter:
    def __init__(self):
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

class Monster:
    pass

# Пример использования
fighter = Fighter()
sword = Sword()
bow = Bow()

fighter.changeWeapon(sword)
print("Боец выбирает меч.")
print(fighter.weapon.attack())
print("Монстр побежден!")

fighter.changeWeapon(bow)
print("Боец выбирает лук.")
print(fighter.weapon.attack())
print("Монстр побежден!")