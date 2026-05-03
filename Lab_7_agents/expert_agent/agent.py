from google.adk.agents.llm_agent import Agent

def analyze_text(text: str) -> dict:
    """Аналізує текст та повертає факти"""
    return {
        "status": "success",
        "text": text,
        "analysis": "Аналіз тексту"
    }

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='expert_agent',
    description="Експертний агент з точними відповідями.",
    instruction="Ти експерт, який надає точні, детальні та фактичні відповіді. Уникай припущень. Відповідай українською мовою.",
    tools=[analyze_text],
)
