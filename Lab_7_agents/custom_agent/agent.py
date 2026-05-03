from google.adk.agents.llm_agent import Agent

def safe_divide(a: float, b: float) -> dict:
    """
    Ділить два числа з перевіркою на нуль.
    Args:
        a: Ділене
        b: Дільник
    Returns:
        dict: Результат ділення або повідомлення про помилку
    """
    if b == 0:
        return {"error": "Ділення на нуль неможливе", "result": None}
    return {"result": a / b, "error": None}

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='safe_calculator_agent',
    description="Агент-калькулятор з безпечним діленням.",
    instruction="""Ти точний фінансовий та математичний асистент. 
    Твої правила:
    1. Використовуй інструмент safe_divide для операцій ділення.
    2. Якщо інструмент повертає помилку, поясни користувачу чому це сталося ввічливо.
    3. Відповідай виключно українською мовою.
    4. Завжди структуруй відповіді.""",
    tools=[safe_divide],
)