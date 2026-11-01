import random


class CardGame:
    CARD_NAMES = (
        "Flame Dragon",
        "Ice Golem",
        "Thunder Phoenix",
        "Shadow Assassin",
        "Earth Titan",
    )

    def __init__(self) -> None:
        self.name = random.choice(self.CARD_NAMES)
        self.attack = random.randint(1, 10)
        self.health = random.randint(20, 40)

    def hit_another_card(self, other_card: object) -> int | None:
        if not isinstance(other_card, CardGame):
            return None
        damage = self.__calculate_critical_damage(self.attack)
        other_card.health -= damage
        return damage

    @staticmethod
    def __calculate_critical_damage(base_damage: int) -> int:
        roll = random.random()
        if roll < 3 / 7:
            return base_damage * 2
        if roll < 0.1 + 3 / 7:
            return base_damage // 2
        if roll < 0.15 + 3 / 7:
            return 0
        return base_damage

    def incorrect_interraction(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("Значення повинно бути цілим числом!")
        if value < 0:
            raise ValueError("Значення не може бути від'ємним!")
        return value * 2

    def example_with_input(self) -> int | None:
        user_input = input("Введіть число: ")
        try:
            number = int(user_input)
        except ValueError:
            return 1
        print(f"Ви ввели число: {number}")
        return None

    @staticmethod
    def compare_input_arguments_original(a: int, b: int) -> int | None:
        if a > b:
            return a
        if a < b:
            return b
        return None

    @staticmethod
    def compare_input_arguments_reduced(a: int, b: int) -> int | None:
        return max(a, b) if a != b else None


class SingleCardGame(CardGame):
    RARITY_LEVELS = ("Common", "Rare", "Epic", "Legendary")

    def __init__(self, rarity: str, unic_prefix: str = "Epic") -> None:
        super().__init__()
        self.name = f"{unic_prefix} Single Card with rarity {rarity}"
        self.attack = 5
        self.health = 30
        self.rarity = rarity if rarity in self.RARITY_LEVELS else "Common"

    def increment(self) -> None:
        self.attack += 1
        self.health += 10

    def decrement(self) -> None:
        self.attack -= 1
        self.health -= 10
