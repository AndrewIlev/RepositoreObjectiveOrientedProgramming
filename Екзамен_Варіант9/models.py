from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class Dish(ABC):
    def __init__(self, name: str, cooking_time_min: int):
        self.name = name
        self.cooking_time_min = cooking_time_min

    @abstractmethod
    def get_nutrition(self) -> Dict[str, Any]:
        pass

class VeganDish(Dish):
    def __init__(self, name: str, cooking_time_min: int, calories: int):
        super().__init__(name, cooking_time_min)
        self.calories = calories

    def get_nutrition(self) -> Dict[str, Any]:
        return {"calories": self.calories, "type": "vegan"}

class MeatDish(Dish):
    def __init__(self, name: str, cooking_time_min: int, calories: int, protein_g: float):
        super().__init__(name, cooking_time_min)
        self.calories = calories
        self.protein_g = protein_g

    def get_nutrition(self) -> Dict[str, Any]:
        return {"calories": self.calories, "protein_g": self.protein_g, "type": "meat"}

class CookBook:
    def __init__(self):
        # Інкапсуляція: приватний словник
        self.__recipes: Dict[str, Dish] = {}

    def add(self, dish: Dish):
        self.__recipes[dish.name] = dish

    def find(self, name: str) -> Optional[Dish]:
        return self.__recipes.get(name)

    def list_all(self):
        print("--- Всі рецепти у книзі ---")
        for name, dish in self.__recipes.items():
            # Поліморфізм у дії
            print(f"Страва: {name} | Час: {dish.cooking_time_min} хв | Харчова цінність: {dish.get_nutrition()}")