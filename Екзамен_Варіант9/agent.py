from typing import Dict, Any
from models import CookBook, VeganDish, MeatDish

def get_recipe_info(dish_name: str) -> Dict[str, Any]:
    """Інструмент (tool) для пошуку страв у CookBook."""
    cookbook = CookBook()
    
    # Наповнення бази даних
    cookbook.add(VeganDish("Салат з тофу", 15, 120))
    cookbook.add(VeganDish("Гарбузовий суп", 40, 250))
    cookbook.add(MeatDish("Стейк рібай", 25, 700, 55.0))
    cookbook.add(MeatDish("Курка з рисом", 45, 500, 40.5))

    dish = cookbook.find(dish_name)
    if dish:
        info = dish.get_nutrition()
        info["cooking_time_min"] = dish.cooking_time_min
        info["found"] = True
        return info
    return {"found": False}

AGENT_PROMPT = (
    "Ти є кулінарним помічником. Ти надаєш інформацію про рецепти, "
    "калорійність та тип страви, а також даєш рекомендації щодо харчування. "
    "Відповідаєш українською мовою."
)

class RecipeAgent:
    def __init__(self, prompt: str):
        self.prompt = prompt

    def process_query(self, user_question: str, dish_to_search: str):
        print(f"\n Користувач: {user_question}")
        print("  [Агент викликає tool: get_recipe_info(...)]")
        
        tool_result = get_recipe_info(dish_to_search)
        
        print("🤖 Агент:")
        if tool_result.get("found"):
            dish_type_ua = "веганська" if tool_result["type"] == "vegan" else "м'ясна"
            response = (f"Я знайшов цю страву! Це {dish_type_ua} страва. "
                        f"Вона готується {tool_result['cooking_time_min']} хвилин і містить {tool_result['calories']} ккал. ")
            
            if "protein_g" in tool_result:
                response += f"Також у ній міститься {tool_result['protein_g']} г білка. "
            
            if tool_result["type"] == "vegan":
                response += "Це чудовий легкий вибір для розвантаження організму."
            else:
                response += "Ця страва чудово підійде для відновлення сил завдяки високому вмісту білка."
            print(response)
        else:
            print(f"На жаль, я не знайшов страву '{dish_to_search}' у базі рецептів. Можливо, підказати щось інше?")