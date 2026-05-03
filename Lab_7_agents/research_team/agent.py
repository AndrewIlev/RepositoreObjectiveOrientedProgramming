from google.adk.agents.workflow import ParallelAgent
from google.adk.agents.llm_agent import Agent

tech_researcher = Agent(name="tech", instruction="Досліди технологічні тренди.", model="gemini-2.5-flash")
econ_researcher = Agent(name="econ", instruction="Досліди економічні тренди.", model="gemini-2.5-flash")
social_researcher = Agent(name="social", instruction="Досліди соціальні тренди.", model="gemini-2.5-flash")

root_agent = ParallelAgent(
    name="research_team",
    agents=[tech_researcher, econ_researcher, social_researcher]
)