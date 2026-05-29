import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Завантаження змінних оточення з файлу .env
load_dotenv()

# ==========================================
# 1. OOP КЛАСИ (Демонстрація 4-х парадигм)
# ==========================================

# АБСТРАКЦІЯ
class Dish(ABC):
    def __init__(self, name: str, cooking_time_min: int):
        self.name = name
        self.cooking_time_min = cooking_time_min

    @abstractmethod
    def get_nutrition(self) -> dict:
        pass

# НАСЛІДУВАННЯ ТА ПОЛІМОРФІЗМ
class VeganDish(Dish):
    def __init__(self, name: str, cooking_time_min: int, calories: int):
        super().__init__(name, cooking_time_min)
        self.calories = calories

    def get_nutrition(self) -> dict:
        return {"calories": self.calories, "type": "vegan"}

class MeatDish(Dish):
    def __init__(self, name: str, cooking_time_min: int, calories: int, protein_g: float):
        super().__init__(name, cooking_time_min)
        self.calories = calories
        self.protein_g = protein_g

    def get_nutrition(self) -> dict:
        return {"calories": self.calories, "protein_g": self.protein_g, "type": "meat"}

# ІНКАПСУЛЯЦІЯ
class CookBook:
    def __init__(self):
        self.__recipes: dict[str, Dish] = {}

    def add(self, dish: Dish):
        self.__recipes[dish.name.lower()] = dish

    def find(self, name: str) -> Dish | None:
        return self.__recipes.get(name.lower(), None)


# ==========================================
# 2. ІНСТРУМЕНТ ДЛЯ AI АГЕНТА (TOOL)
# ==========================================

def get_recipe_info(dish_name: str) -> dict:
    """
    Повертає інформацію про страву (час приготування, калорійність та тип) за її назвою.
    
    Args:
        dish_name: Назва страви (наприклад, 'Борщ український', 'Хумус')
    """
    cookbook = CookBook()
    cookbook.add(MeatDish("Борщ український", 90, 350, 25.5))
    cookbook.add(MeatDish("Стейк", 20, 450, 40.0))
    cookbook.add(VeganDish("Хумус", 15, 166))
    cookbook.add(VeganDish("Салат Грецький", 10, 120))
    cookbook.add(MeatDish("Котлета по-київськи", 40, 420, 28.0))
    cookbook.add(VeganDish("Гарбузовий суп", 30, 95))

    # Шукаємо частковий збіг у назві
    for registered_name in cookbook._CookBook__recipes.keys():
        if registered_name in dish_name.lower():
            dish = cookbook.find(registered_name)
            return {
                "found": True,
                "name": dish.name,
                "cooking_time_min": dish.cooking_time_min,
                "nutrition": dish.get_nutrition()
            }
            
    return {"found": False}


# ==========================================
# 3. ВИЗНАЧЕННЯ AI АГЕНТА
# ==========================================

system_instruction = (
    "Ти — професійний кулінарний помічник. Твоє завдання — надавати користувачеві "
    "інформацію про рецепти, калорійність, час приготування та тип страв, а також давати "
    "корисні рекомендації щодо збалансованого харчування. "
    "Обов'язково використовуй інструмент get_recipe_info для пошуку точних даних про страви з бази даних. "
    "Якщо страви немає в базі, пропонуй альтернативу з тих страв, що є в інструменті. "
    "Завжди відповідай виключно українською мовою, будь привітним та лаконічним."
)

# Ініціалізація клієнта
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Об'єкт root_agent для ADK сумісності
root_agent = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[get_recipe_info],
        temperature=0.7,
    )
)


# ==========================================
# 4. ІНТЕРАКТИВНИЙ ЧАТ (Введення з клавіатури)
# ==========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🤖 РЕЦЕПТУРНИЙ АГЕНТ ЗАПУЩЕНИЙ У ЖИВОМУ РЕЖИМІ")
    print("👉 Напишіть 'вихід' або 'exit' для завершення роботи.")
    print("="*50 + "\n")
    
    # Створюємо живу сесію чату, яка пам'ятає контекст розмови
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=[get_recipe_info]
        )
    )
    
    while True:
        try:
            # Очікуємо введення запиту від користувача
            user_input = input("👤 Ви: ")
            
            # Перевірка на вихід з програми
            if user_input.strip().lower() in ['вихід', 'exit', 'quit']:
                print("\n🤖 До побачення! Смачного харчування! 👋")
                break
                
            # Пропускаємо порожні натискання Enter
            if not user_input.strip():
                continue
                
            # Надсилаємо твоє питання в Gemini
            response = chat.send_message(user_input)
            
            # Виводимо відповідь штучного інтелекту
            print(f"🤖 Агент: {response.text}")
            print("-" * 50)
            
        except KeyboardInterrupt:
            # Обробка Ctrl+C для гарного виходу
            print("\n🤖 Роботу завершено. До зустрічі!")
            break
        except Exception as e:
            print(f"❌ Виникла помилка: {e}")
            print("-" * 50)