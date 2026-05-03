from google.adk.agents.workflow import SequentialAgent
from google.adk.agents.llm_agent import Agent

coder = Agent(name="coder", instruction="Ти програміст. Напиши код на запит.", model="gemini-2.5-flash")
reviewer = Agent(name="reviewer", instruction="Ти рев'юер. Знайди помилки в коді.", model="gemini-2.5-flash")
refactorer = Agent(name="refactorer", instruction="Виправ код на основі рев'ю.", model="gemini-2.5-flash")

root_agent = SequentialAgent(
    name="code_pipeline",
    agents=[coder, reviewer, refactorer]
)