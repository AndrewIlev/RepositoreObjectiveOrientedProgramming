from abc import ABC, abstractmethod
from random import randint, choice


class Item(ABC):

    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass


class Sword(Item):

    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"⚔ {self.name} наносить {current_attack} шкоди"

    def sharpening(self):
        self._sharp += 2
        print("Меч заточено!")

class Axe(Item):

    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power

    def attack(self, another_item):
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"🪓 {self.name} наносить {current_attack} шкоди"


class Bow(Item):

    def __init__(self, name, attack_power: int, range_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another_item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return f"🏹 {self.name} наносить {current_attack} шкоди"

    def reload(self):
        self.range_power += 1
        print("Лук перезаряджено! Дальність збільшена.")


def random_weapon():
    weapons = [
        Sword("Ескалібур", 100),
        Axe("Кратос", 95),
        Bow("Легендарний Лук", 80, 5)
    ]
    return choice(weapons)


if __name__ == "__main__":

    player = random_weapon()
    enemy = random_weapon()

    print(f"Твоя зброя: {player.name}")
    print(f"Зброя ворога: {enemy.name}")

    while player.health > 0 and enemy.health > 0:

        print("\n1 - Атакувати")
        print("2 - Підсилення")

        action = input("Обери дію: ")

        if action == "1":
            print(player.attack(enemy))
        elif action == "2":
            if isinstance(player, Sword):
                player.sharpening()
            elif isinstance(player, Bow):
                player.reload()
            else:
                print("Ця зброя не має підсилення")

        if enemy.health <= 0:
            print("Ти переміг!")
            break

        print(enemy.attack(player))

        print(f"Твоє HP: {player.health}")
        print(f"HP ворога: {enemy.health}")

        if player.health <= 0:
            print("Ти програв!")
            break
        