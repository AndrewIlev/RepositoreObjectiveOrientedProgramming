from models import CookBook, VeganDish, MeatDish
from agent import RecipeAgent, AGENT_PROMPT

if __name__ == "__main__":
    # 1. Швидкий тест працездатності ООП
    test_book = CookBook()
    test_book.add(VeganDish("Броколі на пару", 10, 50))
    test_book.add(MeatDish("Котлети", 30, 450, 25.0))
    test_book.list_all()
    
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦІЯ РОБОТИ AI-АГЕНТА")
    print("="*50)

    # 2. Запуск демонстрації Агента
    agent = RecipeAgent(AGENT_PROMPT)
    
    # 3 запитання згідно з ТЗ
    agent.process_query("Привіт! Розкажи мені про Салат з тофу.", "Салат з тофу")
    agent.process_query("Скільки білка у Стейку рібай?", "Стейк рібай")
    agent.process_query("У вас є рецепт борщу?", "Борщ")