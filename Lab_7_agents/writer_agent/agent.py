from google.adk.agents.llm_agent import Agent

def create_content(theme: str) -> dict:
    """Створює креативний контент на тему"""
    return {
        "status": "success",
        "theme": theme,
        "content": "Креативний контент"
    }

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='writer_agent',
    description="Креативний агент з оригінальними ідеями.",
    instruction="Ти креативний письменник, який генерує оригінальні та захоплюючі ідеї. Будь творчим та нетрадиційним. Використовуй образні вирази та метафори. Відповідай українською мовою.",
    tools=[create_content],
)
