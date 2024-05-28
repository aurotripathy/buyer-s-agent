"""
buyer-s-agent
needed "pip install google-serp-api" before running the code, unsure why
TODO 
get crime data
query zillow
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
import openai
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import chainlit as cl
from chainlit import run_sync
from crewai import Agent, Task, Crew
from crewai_tools import tool
from tools.zillow_tool import ZillowTool

load_dotenv()  # take environment variables from .env.
print(os.environ["OPENAI_API_KEY"])
print(os.environ["SERPER_API_KEY"])

openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'


# NOTE: local llm use: to find which model names you have, use cli tool:  `ollama list`
# ensure its being served
llm = ChatOpenAI(
      model='llama3',
      base_url="http://localhost:11434/v1",
      api_key="NA"
)

search_tool = SerperDevTool()
zillow_tool = ZillowTool()

# Define your agents with roles and goals
buyer = Agent(
  role='First Time Buyer of a Home in the SF Bay Area',
  goal="""Work with a NAR certified Buyer's agent to find a home you love and can afford. 
  Make sure to give the buyer's agent the zipcode or city where you want to buy your home.""",
  backstory="""You have a family of wife and two kids and a stable well-paying job.
  You are looking or a home with three bedrooms in a safe meightborhood and good public schools.""",
  verbose=True,
  allow_delegation=False,
  llm=llm
)

buyers_agent = Agent(
  role="NAR Certified Buyer's Agent",
  goal='Look for homes that meet the criteria of your client.',
  backstory="""You are aggresive, conscientious. and ethical.""",
  verbose=True,
  allow_delegation=False,
  tools=[zillow_tool],
  llm=llm
)

# Create tasks for your agents
buyer_task = Task(
  description="""Specify your requirements to the buyer's agent and clearly and consicely as you can.
  Make sure to check with a human if the requirements are complete before finalizing your answer.""",
  expected_output="Your home purchase requirements as bullet points.",
  agent=buyer,
  human_input=True
)

look_for_homes_task = Task(
  description="""Based on the inputs provided by the buyer, search the internet for homes. 
  You can ask the buyer for additional information when you think the buyer has not provided sufficient information.""",
  expected_output="Curated list of N=5 homes with concise details. Each item on the list must not excee 30 words",
  agent=buyers_agent
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[buyer, buyers_agent],
  tasks=[buyer_task, look_for_homes_task],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
