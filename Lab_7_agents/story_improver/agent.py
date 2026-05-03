from google.adk.agents.workflow import LoopAgent
from google.adk.agents.llm_agent import Agent

def exit_loop(quality_score: int) -> dict:
    """Виходить з циклу якщо оцінка якості більше 8"""
    return {"exit": quality_score > 8}

improver = Agent(
    name="improver", 
    instruction="Покращуй історію та оцінюй її. Виклич exit_loop(score).", 
    tools=[exit_loop],
    model="gemini-2.5-flash"
)

root_agent = LoopAgent(
    name="story_improver",
    agent=improver
)