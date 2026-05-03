from google.adk.agents.llm_agent import Agent

def assist_user(request: str) -> dict:
    """Допомагає користувачу з запитом"""
    return {
        "status": "success",
        "request": request,
        "assistance": "Допомога надана"
    }

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='assistant_agent',
    description="Асистент із збалансованими відповідями.",
    instruction="Ти корисний асистент, який надає збалансовані та розумні відповіді. Будь дружелюбний та корисний. Відповідай українською мовою.",
    tools=[assist_user],
)
