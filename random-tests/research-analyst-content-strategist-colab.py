"""
research-analyst-content-strategist-colab
needed "pip install google-serp-api" before running the code, unsure why
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
import openai
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
print(os.environ["OPENAI_API_KEY"])
print(os.environ["SERPER_API_KEY"])

openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'

from langchain_openai import ChatOpenAI

# NOTE: local llm use: to find which model names you have, use cli tool:  `ollama list`
# ensure its being served
llm = ChatOpenAI(
      model='llama3',
      base_url="http://localhost:11434/v1",
      api_key="NA"
)

search_tool = SerperDevTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=llm
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=False,
  llm =llm
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
  expected_output="Full analysis report in bullet points",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
